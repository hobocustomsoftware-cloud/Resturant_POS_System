export default function ReportsDaily() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Daily Report</h1>
      <div className="grid grid-cols-4 gap-4 mb-6">
        <div className="bg-white p-4 rounded shadow"><div className="text-gray-600">Sales</div><div className="text-2xl font-bold">0 MMK</div></div>
        <div className="bg-white p-4 rounded shadow"><div className="text-gray-600">Purchases</div><div className="text-2xl font-bold">0 MMK</div></div>
        <div className="bg-white p-4 rounded shadow"><div className="text-gray-600">Expenses</div><div className="text-2xl font-bold">0 MMK</div></div>
        <div className="bg-white p-4 rounded shadow"><div className="text-gray-600">Net</div><div className="text-2xl font-bold">0 MMK</div></div>
      </div>
      <div className="bg-white rounded shadow p-6">
        <h2 className="font-bold mb-3">Expenses by Group</h2>
        <div className="space-y-2">
          <div className="flex justify-between"><span>Bar</span><span>0 MMK</span></div>
          <div className="flex justify-between"><span>Kitchen</span><span>0 MMK</span></div>
          <div className="flex justify-between"><span>BBQ</span><span>0 MMK</span></div>
          <div className="flex justify-between"><span>General</span><span>0 MMK</span></div>
        </div>
      </div>
    </div>
  )
}
