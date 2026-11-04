import { Link } from 'react-router-dom'

export default function Sidebar() {
  return (
    <aside className="w-64 bg-gray-900 text-white h-screen p-4">
      <h2 className="text-xl font-bold mb-6">Admin Panel</h2>
      <nav className="flex flex-col gap-2">
        <Link to="/admin" className="p-2 hover:bg-gray-800 rounded">Dashboard</Link>
        <Link to="/admin/products" className="p-2 hover:bg-gray-800 rounded">Products/Items</Link>
        <Link to="/admin/categories" className="p-2 hover:bg-gray-800 rounded">Categories</Link>
        <Link to="/admin/purchases" className="p-2 hover:bg-gray-800 rounded">Purchases/GRN</Link>
        <Link to="/admin/sales" className="p-2 hover:bg-gray-800 rounded">Sales/Orders</Link>
        <Link to="/admin/expenses" className="p-2 hover:bg-gray-800 rounded">Expenses (Bar/Kitchen/BBQ)</Link>
        <Link to="/admin/stock" className="p-2 hover:bg-gray-800 rounded">Stock/Inventory</Link>
        <Link to="/admin/tables" className="p-2 hover:bg-gray-800 rounded">Tables</Link>
        <Link to="/admin/users" className="p-2 hover:bg-gray-800 rounded">Users/Roles</Link>
        <Link to="/admin/settings" className="p-2 hover:bg-gray-800 rounded">Settings</Link>
        <Link to="/admin/reports" className="p-2 hover:bg-gray-800 rounded">Reports</Link>
      </nav>
    </aside>
  )
}
