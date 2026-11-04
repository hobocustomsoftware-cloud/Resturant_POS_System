export default function Tables() {
  const tables = Array.from({ length: 12 }, (_, i) => ({ id: i + 1, name: `Table ${i + 1}`, status: i % 3 === 0 ? 'occupied' : 'available' }))
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Tables - Floor Layout</h1>
      <div className="grid grid-cols-4 md:grid-cols-6 gap-4">
        {tables.map((t) => (
          <button
            key={t.id}
            className={`p-6 rounded text-center ${t.status === 'occupied' ? 'bg-red-200' : t.status === 'reserved' ? 'bg-yellow-200' : 'bg-green-200'}`}
          >
            <div className="font-bold">{t.name}</div>
            <div className="text-sm">{t.status}</div>
          </button>
        ))}
      </div>
      <div className="flex gap-4 mt-6 text-sm">
        <div className="flex items-center gap-2"><div className="w-4 h-4 bg-green-200"></div> Available</div>
        <div className="flex items-center gap-2"><div className="w-4 h-4 bg-red-200"></div> Occupied</div>
        <div className="flex items-center gap-2"><div className="w-4 h-4 bg-yellow-200"></div> Reserved</div>
      </div>
    </div>
  )
}
