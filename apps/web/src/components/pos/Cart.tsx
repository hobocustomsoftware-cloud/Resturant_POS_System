export default function Cart({ items = [], onRemove, onClear }: any) {
  const total = items.reduce((sum: number, i: any) => sum + Number(i.price) * Number(i.qty), 0)
  return (
    <div className="h-full flex flex-col">
      <h2 className="font-bold mb-4">Order</h2>
      <div className="flex-1 overflow-auto">
        {items.map((item: any, idx: number) => (
          <div key={idx} className="flex justify-between border-b py-2">
            <div>
              <div>{item.name}</div>
              <div className="text-sm text-gray-600">{item.price} x {item.qty}</div>
            </div>
            <button onClick={() => onRemove(idx)} className="text-red-600">X</button>
          </div>
        ))}
      </div>
      <div className="border-t pt-4">
        <div className="flex justify-between font-bold mb-4">
          <span>Total</span>
          <span>{total} MMK</span>
        </div>
        <button className="w-full bg-green-600 text-white py-2 rounded mb-2">Pay</button>
        <button onClick={onClear} className="w-full bg-gray-200 py-2 rounded">Clear</button>
      </div>
    </div>
  )
}
