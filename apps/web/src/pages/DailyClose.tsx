export default function DailyClose() {
  const items = [
    { name: 'Fried Rice', system: 50, actual: '', diff: 0 },
    { name: 'Coke', system: 100, actual: '', diff: 0 },
  ]
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Close Shop - Stock Reconciliation</h1>
      <div className="bg-white rounded shadow p-6 mb-4">
        <h2 className="font-bold mb-3">Cash Count</h2>
        <div className="grid grid-cols-2 gap-4 mb-4">
          <div>
            <label className="block mb-1">System Cash</label>
            <input disabled className="w-full border p-2 rounded bg-gray-100" value="50000" />
          </div>
          <div>
            <label className="block mb-1">Actual Cash Count</label>
            <input className="w-full border p-2 rounded" placeholder="Enter actual cash" />
          </div>
        </div>
      </div>
      <div className="bg-white rounded shadow p-6 mb-4">
        <h2 className="font-bold mb-3">Stock Check (System vs Actual)</h2>
        <table className="w-full">
          <thead>
            <tr className="border-b">
              <th className="text-left p-2">Item</th>
              <th className="text-left p-2">System Qty</th>
              <th className="text-left p-2">Actual Qty</th>
              <th className="text-left p-2">Difference</th>
              <th className="text-left p-2">Reason</th>
            </tr>
          </thead>
          <tbody>
            {items.map((item, idx) => (
              <tr key={idx} className="border-b">
                <td className="p-2">{item.name}</td>
                <td className="p-2">{item.system}</td>
                <td className="p-2"><input className="border p-1 rounded w-24" /></td>
                <td className="p-2">0</td>
                <td className="p-2"><input className="border p-1 rounded w-full" placeholder="Reason if different" /></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <button className="bg-red-600 text-white px-6 py-2 rounded">Close Shop</button>
    </div>
  )
}
