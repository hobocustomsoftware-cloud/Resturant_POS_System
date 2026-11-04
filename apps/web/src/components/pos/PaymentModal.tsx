export default function PaymentModal({ open, total, onClose }: any) {
  if (!open) return null
  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center">
      <div className="bg-white rounded w-[500px] p-6">
        <h2 className="text-xl font-bold mb-4">Payment</h2>
        <div className="mb-4">
          <div className="flex justify-between mb-2"><span>Total</span><span>{total} MMK</span></div>
          <input className="w-full border p-2 mb-2" placeholder="Discount (Amount)" />
          <input className="w-full border p-2 mb-2" placeholder="Service Charge" />
        </div>
        <div className="grid grid-cols-3 gap-2 mb-4">
          <button className="p-3 border rounded">Cash</button>
          <button className="p-3 border rounded">Card</button>
          <button className="p-3 border rounded">QR</button>
        </div>
        <input className="w-full border p-2 mb-2" placeholder="Cash Received" />
        <div className="flex justify-between mb-4"><span>Change</span><span>0 MMK</span></div>
        <div className="flex gap-2">
          <button className="flex-1 bg-green-600 text-white py-2 rounded">Complete</button>
          <button onClick={onClose} className="flex-1 bg-gray-200 py-2 rounded">Cancel</button>
        </div>
      </div>
    </div>
  )
}
