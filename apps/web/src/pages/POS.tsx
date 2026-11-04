import { useState } from 'react'
import CategoryTabs from '@/components/pos/CategoryTabs'
import ItemGrid from '@/components/pos/ItemGrid'
import Cart from '@/components/pos/Cart'
import OrderTypeTabs from '@/components/pos/OrderTypeTabs'
import PaymentModal from '@/components/pos/PaymentModal'
import HoldListModal from '@/components/pos/HoldListModal'
import { useCartStore } from '@/stores/cart'
import { Link } from 'react-router-dom'

const mockCategories = [
  { id: 1, name: 'Food' },
  { id: 2, name: 'Drinks' },
  { id: 3, name: 'Dessert' },
]

const mockItems = [
  { id: '1', name: 'Fried Rice', price: 5000, category: 1 },
  { id: '2', name: 'Noodles', price: 4500, category: 1 },
  { id: '3', name: 'Coke', price: 1000, category: 2 },
  { id: '4', name: 'Ice Cream', price: 1500, category: 3 },
]

export default function POS() {
  const [activeCategory, setActiveCategory] = useState(null)
  const [orderType, setOrderType] = useState('dine_in')
  const [showPay, setShowPay] = useState(false)
  const [showHold, setShowHold] = useState(false)
  const { items, addItem, removeItem, clear } = useCartStore()
  
  const filteredItems = activeCategory
    ? mockItems.filter((i) => i.category === activeCategory)
    : mockItems

  const total = items.reduce((sum: number, i: any) => sum + Number(i.price) * Number(i.qty), 0)

  return (
    <div className="h-screen bg-gray-100 flex flex-col">
      <header className="bg-white border-b px-6 py-3 flex justify-between items-center">
        <h1 className="text-xl font-bold">POS</h1>
        <div className="flex gap-2">
          <Link to="/tables" className="px-3 py-1 bg-gray-200 rounded text-sm">Tables</Link>
          <button onClick={() => setShowHold(true)} className="px-3 py-1 bg-gray-200 rounded text-sm">Hold Orders</button>
          <Link to="/kds" className="px-3 py-1 bg-gray-200 rounded text-sm">KDS</Link>
          <Link to="/admin" className="px-3 py-1 bg-gray-200 rounded text-sm">Admin</Link>
        </div>
      </header>
      <div className="flex-1 grid grid-cols-3 gap-4 p-4 overflow-hidden">
        <div className="col-span-2 bg-white rounded shadow p-4 overflow-auto">
          <OrderTypeTabs value={orderType} onChange={setOrderType} />
          <CategoryTabs categories={mockCategories} active={activeCategory} onChange={setActiveCategory} />
          <ItemGrid items={filteredItems} onAdd={addItem} />
        </div>
        <div className="bg-white rounded shadow p-4 flex flex-col">
          <div className="flex justify-between mb-3">
            <h2 className="font-bold">Cart</h2>
            <span className="text-sm text-gray-600">{orderType.replace('_', ' ')}</span>
          </div>
          <div className="flex-1 overflow-auto">
            <Cart items={items} onRemove={removeItem} onClear={clear} />
          </div>
          <div className="border-t pt-3">
            <button onClick={() => setShowPay(true)} disabled={items.length === 0} className="w-full bg-green-600 text-white py-2 rounded disabled:bg-gray-400">PAY {total} MMK</button>
          </div>
        </div>
      </div>
      <PaymentModal open={showPay} total={total} onClose={() => setShowPay(false)} />
      <HoldListModal open={showHold} onClose={() => setShowHold(false)} />
    </div>
  )
}
