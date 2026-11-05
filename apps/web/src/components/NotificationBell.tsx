import { useState } from 'react'
import { useNotifications, useMarkRead } from '@/hooks/useNotifications'
import { Bell } from 'lucide-react'

export default function NotificationBell() {
  const [open, setOpen] = useState(false)
  const { data } = useNotifications()
  const markRead = useMarkRead()
  const notifications = data?.results || data || []
  const unread = notifications.filter((n: any) => !n.read).length

  return (
    <div className="relative">
      <button onClick={() => setOpen(!open)} className="relative p-2">
        <Bell size={20} />
        {unread > 0 && <span className="absolute -top-1 -right-1 bg-red-600 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center">{unread}</span>}
      </button>
      {open && (
        <div className="absolute right-0 mt-2 w-80 bg-white shadow-lg rounded border max-h-96 overflow-auto z-50">
          <div className="p-3 border-b font-semibold">Notifications</div>
          {notifications.slice(0, 10).map((n: any) => (
            <div key={n.id} onClick={() => markRead.mutate(n.id)} className={`p-3 border-b cursor-pointer hover:bg-gray-50 ${!n.read ? 'bg-blue-50' : ''}`}>
              <div className="font-medium text-sm">{n.title}</div>
              <div className="text-xs text-gray-600">{n.message}</div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
