export default function POS() {
  return (
    <div className="p-6 h-screen bg-gray-100">
      <h1 className="text-2xl font-bold mb-4">POS - UTA Style</h1>
      <div className="grid grid-cols-3 gap-4 h-[calc(100vh-100px)]">
        <div className="col-span-2 bg-white rounded shadow p-4">Menu Items</div>
        <div className="bg-white rounded shadow p-4">Cart / Order</div>
      </div>
    </div>
  )
}
