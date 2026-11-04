export default function CategoryTabs({ categories = [], active, onChange }: any) {
  return (
    <div className="flex gap-2 overflow-x-auto mb-4">
      <button
        onClick={() => onChange(null)}
        className={`px-4 py-2 rounded ${active === null ? 'bg-blue-600 text-white' : 'bg-gray-200'}`}
      >
        All
      </button>
      {categories.map((cat: any) => (
        <button
          key={cat.id}
          onClick={() => onChange(cat.id)}
          className={`px-4 py-2 rounded whitespace-nowrap ${active === cat.id ? 'bg-blue-600 text-white' : 'bg-gray-200'}`}
        >
          {cat.name}
        </button>
      ))}
    </div>
  )
}
