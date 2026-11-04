import { Routes, Route, Link } from 'react-router-dom'

const AdminHome = () => (
  <div className="p-6">
    <h1 className="text-2xl font-bold mb-4">Custom Admin Panel</h1>
    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
      <Link to="/admin/products" className="p-4 border rounded hover:bg-gray-50">Products</Link>
      <Link to="/admin/categories" className="p-4 border rounded hover:bg-gray-50">Categories</Link>
      <Link to="/admin/purchases" className="p-4 border rounded hover:bg-gray-50">Purchases</Link>
      <Link to="/admin/sales" className="p-4 border rounded hover:bg-gray-50">Sales</Link>
      <Link to="/admin/expenses" className="p-4 border rounded hover:bg-gray-50">Expenses (Bar/Kitchen/BBQ)</Link>
      <Link to="/admin/stock" className="p-4 border rounded hover:bg-gray-50">Stock</Link>
      <Link to="/admin/users" className="p-4 border rounded hover:bg-gray-50">Users/Roles</Link>
      <Link to="/admin/reports" className="p-4 border rounded hover:bg-gray-50">Reports</Link>
    </div>
  </div>
)

export default function Admin() {
  return (
    <Routes>
      <Route index element={<AdminHome />} />
      <Route path="*" element={<AdminHome />} />
    </Routes>
  )
}
