export default function Receipt({ order }: any) {
  return (
    <div className="w-[300px] p-4 font-mono text-xs">
      <div className="text-center mb-2">
        <div className="font-bold">RESTAURANT NAME</div>
        <div>Address / Phone</div>
      </div>
      <div className="border-t border-b py-2 mb-2">
        <div>Order: {order?.order_no || '-'}</div>
        <div>Date: {new Date().toLocaleString()}</div>
      </div>
      <div className="mb-2">
        {(order?.items || []).map((item: any, idx: number) => (
          <div key={idx} className="flex justify-between">
            <span>{item.name} x{item.qty || 1}</span>
            <span>{item.total || item.price}</span>
          </div>
        ))}
      </div>
      <div className="border-t pt-2">
        <div className="flex justify-between font-bold"><span>Total</span><span>{order?.total || 0} MMK</span></div>
      </div>
      <div className="text-center mt-4">Thank You!</div>
    </div>
  )
}
