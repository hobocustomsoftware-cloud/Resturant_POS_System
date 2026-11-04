export default function OrderTypeTabs({ value, onChange }: any) {
  const types = [
    { key: 'dine_in', label: 'Dine In' },
    { key: 'take_away', label: 'Take Away' },
    { key: 'delivery', label: 'Delivery' },
  ]
  return (
    <div className="flex gap-2 mb-3">
      {types.map((t) => (
        <button
          key={t.key}
          onClick={() => onChange(t.key)}
          className={`px-3 py-1 rounded text-sm ${value === t.key ? 'bg-blue-600 text-white' : 'bg-gray-200'}`}
        >
          {t.label}
        </button>
      ))}
    </div>
  )
}
