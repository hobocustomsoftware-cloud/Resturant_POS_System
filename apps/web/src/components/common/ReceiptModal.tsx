import Receipt from '@/pages/Receipt'

export default function ReceiptModal({ open, order, onClose }: any) {
  if (!open) return null
  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center">
      <div className="bg-white rounded p-4">
        <Receipt order={order} />
        <div className="flex gap-2 mt-4">
          <button onClick={() => window.print()} className="flex-1 bg-blue-600 text-white py-2 rounded">Print</button>
          <button onClick={onClose} className="flex-1 bg-gray-200 py-2 rounded">Close</button>
        </div>
      </div>
    </div>
  )
}
