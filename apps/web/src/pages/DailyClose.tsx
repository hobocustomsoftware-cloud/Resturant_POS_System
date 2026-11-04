import { useStock, useDailyCurrent, useCloseDay } from '@/hooks/useApi'
import { useState } from 'react'
import toast from 'react-hot-toast'

export default function DailyClose() {
  const { data: stockData } = useStock()
  const { data: current } = useDailyCurrent()
  const closeDay = useCloseDay()
  const stock = stockData?.results || stockData || []
  const [cashCount, setCashCount] = useState('')
  const [recons, setRecons] = useState<any>({})

  const handleChange = (id: string, field: string, value: any) => {
    setRecons({ ...recons, [id]: { ...recons[id], [field]: value } })
  }

  const handleClose = () => {
    if (!current?.session?.id) return toast.error('No open session')
    const reconciliations = stock.map((s: any) => ({
      item_id: s.item,
      item_name: s.item,
      system_qty: s.quantity,
      actual_qty: recons[s.id]?.actual_qty || s.quantity,
      difference: Number(recons[s.id]?.actual_qty || s.quantity) - Number(s.quantity),
      reason: recons[s.id]?.reason || ''
    }))
    closeDay.mutate({ id: current.session.id, data: { reconciliations, cash_count: cashCount } } as any, {
      onSuccess: () => toast.success('Day closed with reconciliation'),
      onError: () => toast.error('Failed to close')
    })
  }

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Close Shop - Stock Reconciliation</h1>
      <div className="bg-white rounded shadow p-6 mb-4">
        <h2 className="font-bold mb-3">Cash Count</h2>
        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block mb-1">System Cash</label>
            <input disabled className="w-full border p-2 rounded bg-gray-100" value="0" />
          </div>
          <div>
            <label className="block mb-1">Actual Cash Count</label>
            <input value={cashCount} onChange={(e) => setCashCount(e.target.value)} className="w-full border p-2 rounded" placeholder="Enter actual cash" />
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
            {stock.map((s: any) => (
              <tr key={s.id} className="border-b">
                <td className="p-2">{s.item}</td>
                <td className="p-2">{s.quantity}</td>
                <td className="p-2"><input onChange={(e) => handleChange(s.id, 'actual_qty', e.target.value)} className="border p-1 rounded w-24" /></td>
                <td className="p-2">-</td>
                <td className="p-2"><input onChange={(e) => handleChange(s.id, 'reason', e.target.value)} className="border p-1 rounded w-full" placeholder="Reason if different" /></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <button onClick={handleClose} disabled={closeDay.isPending} className="bg-red-600 text-white px-6 py-2 rounded disabled:bg-gray-400">
        {closeDay.isPending ? 'Closing...' : 'Close Shop'}
      </button>
    </div>
  )
}
