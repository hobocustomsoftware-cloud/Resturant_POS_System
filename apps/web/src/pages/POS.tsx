import { useState } from 'react'
import CategoryTabs from '@/components/pos/CategoryTabs'
import ItemGrid from '@/components/pos/ItemGrid'
import Cart from '@/components/pos/Cart'
import { useCartStore } from '@/stores/cart'

const mockCategories = [
  { id: 1, name: 'Food' },
  { id: 2, name: 'Drinks' },
  { id: 3, name: 'Dessert' },
]

const mockItems = [
  { id: '1', name: 'Fried Rice', price: 5000, category: 1 },
  { id: '2', name: 'Noodles', price: 4500, category: 1 },
  { id: '3', name: 'Coke', price: 1000, category: 2 },
]

export default function POS() {
  const [activeCategory, setActiveCategory] = useState(null)
  const { items, addItem, removeItem, clear } = useCartStore()
  
  const filteredItems = activeCategory
    ? mockItems.filter((i) => i.category === activeCategory)
    : mockItems

  return (
    <div className="h-screen bg-gray-100 flex flex-col">
      <header className="bg-white border-b px-6 py-3 flex justify-between">
        <h1 className="text-xl font-bold">Restaurant POS</h1>
        <div className="flex gap-4">
          <button className="px-4 py-2 bg-gray-200 rounded">Tables</button>
          <button className="px-4 py-2 bg-gray-200 rounded">Hold Orders</button>
          <button className="px-4 py-2 bg-gray-200 rounded">KDS</button>
        </div>
      </header>
      <div className="flex-1 grid grid-cols-3 gap-4 p-4 overflow-hidden">
        <div className="col-span-2 bg-white rounded shadow p-4 overflow-auto">
          <CategoryTabs categories={mockCategories} active={activeCategory} onChange={setActiveCategory} />
          <ItemGrid items={filteredItems} onAdd={addItem} />
        </div>
        <div className="bg-white rounded shadow p-4">
          <Cart items={items} onRemove={removeItem} onClear={clear} />
        </div>
      </div>
    </div>
  )
}
