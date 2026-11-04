import { useState } from 'react'
import { useOpenDay, useDailyCurrent } from '@/hooks/useApi'
import toast from 'react-hot-toast'

export default function DailyOpening() {
  const [openingCash, setOpeningCash] = useState('')
  const [branch, setBranch] = useState('1')
  const openDay = useOpenDay()
  const { data: current } = useDailyCurrent()

  const handleOpen = () => {
    openDay.mutate({ branch, opening_cash: openingCash }, {
      onSuccess: () => toast.success('Day opened'),
      onError: () => toast.error('Failed to open day')
    })
  }

  return (
    <div className="p-6 max-w-2xl">
      <h1 className="text-2xl font-bold mb-4">Daily Opening</h1>
      {current?.status === 'open' && (
        <div className="bg-green-100 p-4 rounded mb-4">Day is already open</div>
      )}
      <div className="bg-white rounded shadow p-6">
        <div className="mb-4">
          <label className="block mb-2 font-medium">Branch</label>
          <input value={branch} onChange={(e) => setBranch(e.target.value)} className="w-full border p-2 rounded" />
        </div>
        <div className="mb-4">
          <label className="block mb-2 font-medium">Opening Cash (MMK)</label>
          <input
            type="number"
            value={openingCash}
            onChange={(e) => setOpeningCash(e.target.value)}
            className="w-full border p-2 rounded"
            placeholder="Enter opening cash amount"
          />
        </div>
        <button onClick={handleOpen} disabled={openDay.isPending} className="bg-blue-600 text-white px-6 py-2 rounded disabled:bg-gray-400">
          {openDay.isPending ? 'Opening...' : 'Start Day'}
        </button>
        <p className="text-sm text-gray-600 mt-4">Opening balance will be used for cash reconciliation at end of day</p>
      </div>
    </div>
  )
}
