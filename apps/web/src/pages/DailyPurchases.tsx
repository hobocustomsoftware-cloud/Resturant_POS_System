export default function DailyPurchases() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Daily Purchases (GRN)</h1>
      <div className="bg-white rounded shadow p-6 mb-4">
        <div className="grid grid-cols-3 gap-4 mb-4">
          <input className="border p-2 rounded" placeholder="Supplier" />
          <input className="border p-2 rounded" placeholder="Invoice No" />
          <input type="date" className="border p-2 rounded" />
        </div>
        <button className="bg-blue-600 text-white px-4 py-2 rounded mb-4">Add Item</button>
        <div className="border rounded p-4 text-gray-600 text-center">Add purchase items here</div>
        <div className="mt-4 flex justify-end">
          <button className="bg-green-600 text-white px-6 py-2 rounded">Save & Receive (Add to Stock)</button>
        </div>
      </div>
    </div>
  )
}
