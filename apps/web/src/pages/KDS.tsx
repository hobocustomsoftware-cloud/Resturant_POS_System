export default function KDS() {
  return (
    <div className="p-6 bg-gray-900 min-h-screen">
      <h1 className="text-2xl font-bold mb-4 text-white">Kitchen Display System</h1>
      <div className="grid grid-cols-3 gap-4">
        <div className="bg-yellow-100 p-4 rounded">
          <h2 className="font-bold mb-3">Pending</h2>
          <p className="text-gray-600">No orders</p>
        </div>
        <div className="bg-blue-100 p-4 rounded">
          <h2 className="font-bold mb-3">Preparing</h2>
          <p className="text-gray-600">No orders</p>
        </div>
        <div className="bg-green-100 p-4 rounded">
          <h2 className="font-bold mb-3">Ready</h2>
          <p className="text-gray-600">No orders</p>
        </div>
      </div>
    </div>
  )
}
