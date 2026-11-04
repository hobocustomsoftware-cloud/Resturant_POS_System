import { Routes, Route } from 'react-router-dom'
import Sidebar from '@/components/admin/Sidebar'

const Dashboard = () => (
  <div>
    <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
    <div className="grid grid-cols-4 gap-4">
      <div className="p-4 bg-white rounded shadow">Sales Today</div>
      <div className="p-4 bg-white rounded shadow">Purchases</div>
      <div className="p-4 bg-white rounded shadow">Expenses</div>
      <div className="p-4 bg-white rounded shadow">Stock Alerts</div>
    </div>
  </div>
)

const CRUDPage = ({ title }: { title: string }) => (
  <div>
    <h1 className="text-2xl font-bold mb-4">{title}</h1>
    <button className="mb-4 px-4 py-2 bg-blue-600 text-white rounded">Add New</button>
    <div className="bg-white rounded shadow p-4">List will be here</div>
  </div>
)

export default function Admin() {
  return (
    <div className="flex">
      <Sidebar />
      <main className="flex-1 p-6 bg-gray-100 min-h-screen">
        <Routes>
          <Route index element={<Dashboard />} />
          <Route path="products" element={<CRUDPage title="Products/Items" />} />
          <Route path="categories" element={<CRUDPage title="Categories" />} />
          <Route path="purchases" element={<CRUDPage title="Purchases/GRN" />} />
          <Route path="sales" element={<CRUDPage title="Sales/Orders" />} />
          <Route path="expenses" element={<CRUDPage title="Expenses - Bar/Kitchen/BBQ/General" />} />
          <Route path="stock" element={<CRUDPage title="Stock/Inventory" />} />
          <Route path="tables" element={<CRUDPage title="Tables" />} />
          <Route path="users" element={<CRUDPage title="Users & Roles" />} />
          <Route path="settings" element={<CRUDPage title="Settings" />} />
          <Route path="reports" element={<CRUDPage title="Reports" />} />
        </Routes>
      </main>
    </div>
  )
}
