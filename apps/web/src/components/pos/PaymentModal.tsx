import { useState } from 'react'
import { useCreateOrderFull, useCompleteOrder } from '@/hooks/useApi'
import { useCartStore } from '@/stores/cart'
import toast from 'react-hot-toast'

export default function PaymentModal({ open, total, onClose, orderType }: any) {
  const [method, setMethod] = useState('cash')
  const [discount, setDiscount] = useState(0)
  const [received, setReceived] = useState('')
  const createOrder = useCreateOrderFull()
  const completeOrder = useCompleteOrder()
  const { items, clear } = useCartStore()

  if (!open) return null

  const finalTotal = total - Number(discount)
  const change = received ? Number(received) - finalTotal : 0

  const handlePay = async () => {
    try {
      const orderRes = await createOrder.mutateAsync({
        order_no: `ORD-${Date.now()}`,
        type: orderType || 'dine_in',
        subtotal: total,
        discount: discount,
        tax: 0,
        service_charge: 0,
        total: finalTotal,
        status: 'pending'
      })
      await completeOrder.mutateAsync(orderRes.data.id)
      toast.success('Order completed')
      clear()
      onClose()
    } catch (e) {
      toast.error('Payment failed')
    }
  }

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white rounded w-[500px] p-6">
        <h2 className="text-xl font-bold mb-4">Payment</h2>
        <div className="mb-4 space-y-2">
          <div className="flex justify-between"><span>Subtotal</span><span>{total} MMK</span></div>
          <div className="flex justify-between items-center">
            <span>Discount</span>
            <input type="number" value={discount} onChange={(e) => setDiscount(e.target.value)} className="border p-1 w-32 text-right" />
          </div>
          <div className="flex justify-between font-bold border-t pt-2"><span>Total</span><span>{finalTotal} MMK</span></div>
        </div>
        <div className="grid grid-cols-3 gap-2 mb-4">
          <button onClick={() => setMethod('cash')} className={`p-3 border rounded ${method === 'cash' ? 'bg-blue-600 text-white' : ''}`}>Cash</button>
          <button onClick={() => setMethod('card')} className={`p-3 border rounded ${method === 'card' ? 'bg-blue-600 text-white' : ''}`}>Card</button>
          <button onClick={() => setMethod('qr')} className={`p-3 border rounded ${method === 'qr' ? 'bg-blue-600 text-white' : ''}`}>QR</button>
        </div>
        {method === 'cash' && (
          <div className="mb-4">
            <input type="number" value={received} onChange={(e) => setReceived(e.target.value)} className="w-full border p-2 mb-2" placeholder="Cash Received" />
            <div className="flex justify-between"><span>Change</span><span>{change >= 0 ? change : 0} MMK</span></div>
          </div>
        )}
        <div className="flex gap-2">
          <button onClick={handlePay} disabled={createOrder.isPending || completeOrder.isPending} className="flex-1 bg-green-600 text-white py-2 rounded disabled:bg-gray-400">Complete Payment</button>
          <button onClick={onClose} className="flex-1 bg-gray-200 py-2 rounded">Cancel</button>
        </div>
      </div>
    </div>
  )
}
