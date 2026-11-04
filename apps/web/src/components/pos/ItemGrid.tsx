export default function ItemGrid({ items = [], onAdd }: any) {
  return (
    <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
      {items.map((item: any) => (
        <button
          key={item.id}
          onClick={() => onAdd(item)}
          className="p-4 border rounded hover:bg-blue-50 text-left"
        >
          <div className="font-medium">{item.name}</div>
          <div className="text-blue-600">{item.price} MMK</div>
        </button>
      ))}
    </div>
  )
}
