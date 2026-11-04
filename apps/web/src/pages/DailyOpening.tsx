import { useState } from 'react'

export default function DailyOpening() {
  const [openingCash, setOpeningCash] = useState('')
  return (
    <div className="p-6 max-w-2xl">
      <h1 className="text-2xl font-bold mb-4">Daily Opening</h1>
      <div className="bg-white rounded shadow p-6">
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
        <button className="bg-blue-600 text-white px-6 py-2 rounded">Start Day</button>
        <p className="text-sm text-gray-600 mt-4">Opening balance will carry over for today's sales and purchases tracking</p>
      </div>
    </div>
  )
}
