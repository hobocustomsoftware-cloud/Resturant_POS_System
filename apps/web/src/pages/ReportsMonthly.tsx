export default function ReportsMonthly() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Monthly Report</h1>
      <div className="bg-white rounded shadow p-6">
        <h2 className="font-bold mb-3">Profit & Loss</h2>
        <div className="space-y-2">
          <div className="flex justify-between"><span>Revenue</span><span>0 MMK</span></div>
          <div className="flex justify-between"><span>COGS</span><span>0 MMK</span></div>
          <div className="flex justify-between"><span>Gross Profit</span><span>0 MMK</span></div>
          <div className="flex justify-between"><span>Expenses</span><span>0 MMK</span></div>
          <div className="flex justify-between font-bold border-t pt-2"><span>Net Profit</span><span>0 MMK</span></div>
        </div>
      </div>
    </div>
  )
}
