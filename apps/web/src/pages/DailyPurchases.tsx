import { usePurchases, useReceivePurchase } from '@/hooks/useApi'
import toast from 'react-hot-toast'

export default function DailyPurchases() {
  const { data: purchasesData } = usePurchases?.() || { data: null }
  const receive = useReceivePurchase()
  const purchases = purchasesData?.results || purchasesData || []

  const handleReceive = (id: string) => {
    receive.mutate(id, {
      onSuccess: () => toast.success('Purchase received - stock updated'),
      onError: () => toast.error('Failed')
    })
  }

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Daily Purchases (GRN)</h1>
      <div className="bg-white rounded shadow overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50">
            <tr>
              <th className="text-left p-3">Invoice</th>
              <th className="text-left p-3">Supplier</th>
              <th className="text-left p-3">Total</th>
              <th className="text-left p-3">Status</th>
              <th className="text-left p-3">Action</th>
            </tr>
          </thead>
          <tbody>
            {purchases.map((p: any) => (
              <tr key={p.id} className="border-t">
                <td className="p-3">{p.invoice_no}</td>
                <td className="p-3">{p.supplier}</td>
                <td className="p-3">{p.total}</td>
                <td className="p-3">{p.status}</td>
                <td className="p-3">
                  {p.status !== 'received' && (
                    <button onClick={() => handleReceive(p.id)} className="px-3 py-1 bg-green-600 text-white rounded text-sm">Receive & Add to Stock</button>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}
