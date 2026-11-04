export default function HoldListModal({ open, onClose }: any) {
  if (!open) return null
  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center">
      <div className="bg-white rounded w-[400px] p-6">
        <h2 className="text-xl font-bold mb-4">Hold Orders</h2>
        <p className="text-gray-600 mb-4">No hold orders</p>
        <button onClick={onClose} className="w-full bg-gray-200 py-2 rounded">Close</button>
      </div>
    </div>
  )
}
