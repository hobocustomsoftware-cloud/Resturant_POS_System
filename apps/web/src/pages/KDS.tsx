import { useEffect, useState } from 'react'
import { useOrders } from '@/hooks/useApi'

export default function KDS() {
  const { data } = useOrders()
  const orders = (data?.results || data || []).filter((o: any) => ['pending', 'preparing', 'ready'].includes(o.status))
  const [pending, setPending] = useState<any[]>([])
  const [preparing, setPreparing] = useState<any[]>([])
  const [ready, setReady] = useState<any[]>([])

  useEffect(() => {
    setPending(orders.filter((o: any) => o.status === 'pending'))
    setPreparing(orders.filter((o: any) => o.status === 'preparing'))
    setReady(orders.filter((o: any) => o.status === 'ready'))
  }, [data])

  return (
    <div className="p-6 bg-gray-900 min-h-screen">
      <h1 className="text-2xl font-bold mb-4 text-white">Kitchen Display System</h1>
      <div className="grid grid-cols-3 gap-4">
        <div className="bg-yellow-100 p-4 rounded">
          <h2 className="font-bold mb-3">Pending ({pending.length})</h2>
          {pending.map((o: any) => (
            <div key={o.id} className="bg-white p-2 mb-2 rounded">#{o.order_no} - {o.total}</div>
          ))}
        </div>
        <div className="bg-blue-100 p-4 rounded">
          <h2 className="font-bold mb-3">Preparing ({preparing.length})</h2>
          {preparing.map((o: any) => (
            <div key={o.id} className="bg-white p-2 mb-2 rounded">#{o.order_no} - {o.total}</div>
          ))}
        </div>
        <div className="bg-green-100 p-4 rounded">
          <h2 className="font-bold mb-3">Ready ({ready.length})</h2>
          {ready.map((o: any) => (
            <div key={o.id} className="bg-white p-2 mb-2 rounded">#{o.order_no} - {o.total}</div>
          ))}
        </div>
      </div>
    </div>
  )
}
