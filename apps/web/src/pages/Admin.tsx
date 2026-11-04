import { Routes, Route } from 'react-router-dom'
import Sidebar from '@/components/admin/Sidebar'
import { useItems, useCategories, usePurchases, useExpenses, useTables, useUsers } from '@/hooks/useApi'

const Dashboard = () => (
  <div>
    <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
    <div className="grid grid-cols-4 gap-4">
      <div className="p-4 bg-white rounded shadow"><div className="text-gray-600 text-sm">Products</div><div className="text-2xl font-bold">-</div></div>
      <div className="p-4 bg-white rounded shadow"><div className="text-gray-600 text-sm">Orders</div><div className="text-2xl font-bold">-</div></div>
      <div className="p-4 bg-white rounded shadow"><div className="text-gray-600 text-sm">Purchases</div><div className="text-2xl font-bold">-</div></div>
      <div className="p-4 bg-white rounded shadow"><div className="text-gray-600 text-sm">Expenses</div><div className="text-2xl font-bold">-</div></div>
    </div>
  </div>
)

const ItemsPage = () => {
  const { data } = useItems()
  const items = data?.results || data || []
  return (
    <div>
      <div className="flex justify-between mb-4">
        <h1 className="text-2xl font-bold">Products/Items</h1>
        <button className="px-4 py-2 bg-blue-600 text-white rounded">Add Item</button>
      </div>
      <div className="bg-white rounded shadow overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50"><tr><th className="text-left p-3">Name</th><th className="text-left p-3">Price</th><th className="text-left p-3">SKU</th></tr></thead>
          <tbody>
            {items.map((i: any) => <tr key={i.id} className="border-t"><td className="p-3">{i.name}</td><td className="p-3">{i.price}</td><td className="p-3">{i.sku}</td></tr>)}
          </tbody>
        </table>
      </div>
    </div>
  )
}

const CategoriesPage = () => {
  const { data } = useCategories()
  const cats = data?.results || data || []
  return (
    <div>
      <div className="flex justify-between mb-4">
        <h1 className="text-2xl font-bold">Categories</h1>
        <button className="px-4 py-2 bg-blue-600 text-white rounded">Add Category</button>
      </div>
      <div className="bg-white rounded shadow overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50"><tr><th className="text-left p-3">Name</th></tr></thead>
          <tbody>
            {cats.map((c: any) => <tr key={c.id} className="border-t"><td className="p-3">{c.name}</td></tr>)}
          </tbody>
        </table>
      </div>
    </div>
  )
}

const PurchasesPage = () => {
  const { data } = usePurchases()
  const items = data?.results || data || []
  return (
    <div>
      <div className="flex justify-between mb-4">
        <h1 className="text-2xl font-bold">Purchases/GRN</h1>
        <button className="px-4 py-2 bg-blue-600 text-white rounded">New Purchase</button>
      </div>
      <div className="bg-white rounded shadow overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50"><tr><th className="text-left p-3">Invoice</th><th className="text-left p-3">Total</th><th className="text-left p-3">Status</th></tr></thead>
          <tbody>
            {items.map((p: any) => <tr key={p.id} className="border-t"><td className="p-3">{p.invoice_no}</td><td className="p-3">{p.total}</td><td className="p-3">{p.status}</td></tr>)}
          </tbody>
        </table>
      </div>
    </div>
  )
}

const ExpensesPage = () => {
  const { data } = useExpenses()
  const items = data?.results || data || []
  return (
    <div>
      <div className="flex justify-between mb-4">
        <h1 className="text-2xl font-bold">Expenses (Bar/Kitchen/BBQ/General)</h1>
        <button className="px-4 py-2 bg-blue-600 text-white rounded">Add Expense</button>
      </div>
      <div className="bg-white rounded shadow overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50"><tr><th className="text-left p-3">Amount</th><th className="text-left p-3">Payee</th><th className="text-left p-3">Notes</th></tr></thead>
          <tbody>
            {items.map((e: any) => <tr key={e.id} className="border-t"><td className="p-3">{e.amount}</td><td className="p-3">{e.payee}</td><td className="p-3">{e.notes}</td></tr>)}
          </tbody>
        </table>
      </div>
    </div>
  )
}

const StockPage = () => {
  const { data } = useStock()
  const items = data?.results || data || []
  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Stock/Inventory</h1>
      <div className="bg-white rounded shadow overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50"><tr><th className="text-left p-3">Item</th><th className="text-left p-3">Quantity</th></tr></thead>
          <tbody>
            {items.map((s: any) => <tr key={s.id} className="border-t"><td className="p-3">{s.item}</td><td className="p-3">{s.quantity}</td></tr>)}
          </tbody>
        </table>
      </div>
    </div>
  )
}

const TablesPage = () => {
  const { data } = useTables()
  const items = data?.results || data || []
  return (
    <div>
      <div className="flex justify-between mb-4">
        <h1 className="text-2xl font-bold">Tables</h1>
        <button className="px-4 py-2 bg-blue-600 text-white rounded">Add Table</button>
      </div>
      <div className="bg-white rounded shadow overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50"><tr><th className="text-left p-3">Name</th><th className="text-left p-3">Capacity</th><th className="text-left p-3">Status</th></tr></thead>
          <tbody>
            {items.map((t: any) => <tr key={t.id} className="border-t"><td className="p-3">{t.name}</td><td className="p-3">{t.capacity}</td><td className="p-3">{t.status}</td></tr>)}
          </tbody>
        </table>
      </div>
    </div>
  )
}

const UsersPage = () => {
  const { data } = useUsers?.() || { data: null }
  const items = data?.results || data || []
  return (
    <div>
      <div className="flex justify-between mb-4">
        <h1 className="text-2xl font-bold">Users & Roles</h1>
        <button className="px-4 py-2 bg-blue-600 text-white rounded">Add User</button>
      </div>
      <div className="bg-white rounded shadow overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50"><tr><th className="text-left p-3">Username</th><th className="text-left p-3">Email</th></tr></thead>
          <tbody>
            {items.map((u: any) => <tr key={u.id} className="border-t"><td className="p-3">{u.username}</td><td className="p-3">{u.email}</td></tr>)}
          </tbody>
        </table>
      </div>
    </div>
  )
}

export default function Admin() {
  return (
    <div className="flex">
      <Sidebar />
      <main className="flex-1 p-6 bg-gray-100 min-h-screen">
        <Routes>
          <Route index element={<Dashboard />} />
          <Route path="products" element={<ItemsPage />} />
          <Route path="categories" element={<CategoriesPage />} />
          <Route path="purchases" element={<PurchasesPage />} />
          <Route path="sales" element={<div className="p-4 bg-white rounded">Sales/Orders</div>} />
          <Route path="expenses" element={<ExpensesPage />} />
          <Route path="stock" element={<StockPage />} />
          <Route path="tables" element={<TablesPage />} />
          <Route path="users" element={<UsersPage />} />
          <Route path="settings" element={<div className="p-4 bg-white rounded">Settings</div>} />
          <Route path="reports" element={<div className="p-4 bg-white rounded">Reports</div>} />
        </Routes>
      </main>
    </div>
  )
}
