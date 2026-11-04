import { useState } from 'react'
import CategoryTabs from '@/components/pos/CategoryTabs'
import ItemGrid from '@/components/pos/ItemGrid'
import OrderTypeTabs from '@/components/pos/OrderTypeTabs'
import PaymentModal from '@/components/pos/PaymentModal'
import HoldListModal from '@/components/pos/HoldListModal'
import { useCartStore } from '@/stores/cart'
import { useCategories, useItems } from '@/hooks/useApi'
import { Link } from 'react-router-dom'

export default function POS() {
  const [activeCategory, setActiveCategory] = useState(null)
  const [orderType, setOrderType] = useState('dine_in')
  const [showPay, setShowPay] = useState(false)
  const [showHold, setShowHold] = useState(false)
  const { items, addItem, removeItem, clear } = useCartStore()
  
  const { data: categoriesData } = useCategories()
  const { data: itemsData } = useItems(activeCategory ? { category: activeCategory } : {})
  
  const categories = categoriesData?.results || categoriesData || []
  const items = itemsData?.results || itemsData || []

  const total = items.reduce((sum: number, i: any) => sum + Number(i.price) * Number(i.qty), 0)

  return (
    <div className="h-screen bg-gray-100 flex flex-col">
      <header className="bg-white border-b px-6 py-3 flex justify-between items-center">
        <h1 className="text-xl font-bold">POS</h1>
        <div className="flex gap-2">
          <Link to="/tables" className="px-3 py-1 bg-gray-200 rounded text-sm">Tables</Link>
          <button onClick={() => setShowHold(true)} className="px-3 py-1 bg-gray-200 rounded text-sm">Hold</button>
          <Link to="/kds" className="px-3 py-1 bg-gray-200 rounded text-sm">KDS</Link>
          <Link to="/daily/opening" className="px-3 py-1 bg-gray-200 rounded text-sm">Daily</Link>
          <Link to="/admin" className="px-3 py-1 bg-gray-200 rounded text-sm">Admin</Link>
        </div>
      </header>
      <div className="flex-1 grid grid-cols-3 gap-4 p-4 overflow-hidden">
        <div className="col-span-2 bg-white rounded shadow p-4 overflow-auto">
          <OrderTypeTabs value={orderType} onChange={setOrderType} />
          <CategoryTabs categories={categories} active={activeCategory} onChange={setActiveCategory} />
          <ItemGrid items={items} onAdd={(item: any) => addItem(item)} />
        </div>
        <div className="bg-white rounded shadow p-4 flex flex-col">
          <div className="flex justify-between mb-3">
            <h2 className="font-bold">Cart</h2>
            <span className="text-sm text-gray-600">{orderType.replace('_', ' ')}</span>
          </div>
          <div className="flex-1 overflow-auto">
            {items.length === 0 ? (
              <p className="text-gray-500 text-center mt-8">No items</p>
            ) : (
              <div>
                {items.map((item: any, idx: number) => (
                  <div key={idx} className="flex justify-between border-b py-2">
                    <div>
                      <div className="font-medium">{item.name}</div>
                      <div className="text-sm text-gray-600">{item.price} x {item.qty}</div>
                    </div>
                    <button onClick={() => removeItem(idx)} className="text-red-600 text-sm">Remove</button>
                  </div>
                ))}
              </div>
            )}
          </div>
          <div className="border-t pt-3">
            <div className="flex justify-between font-bold mb-2"><span>Total</span><span>{total} MMK</span></div>
            <button onClick={() => setShowPay(true)} disabled={items.length === 0} className="w-full bg-green-600 text-white py-2 rounded disabled:bg-gray-400">Payment</button>
            <button onClick={clear} className="w-full mt-2 bg-gray-200 py-2 rounded">Clear</button>
          </div>
        </div>
      </div>
      <PaymentModal open={showPay} total={total} orderType={orderType} onClose={() => setShowPay(false)} />
      <HoldListModal open={showHold} onClose={() => setShowHold(false)} />
    </div>
  )
}
