import { create } from 'zustand'

interface CartItem {
  id: string
  name: string
  price: number
  qty: number
}

interface CartStore {
  items: CartItem[]
  addItem: (item: any) => void
  removeItem: (index: number) => void
  clear: () => void
}

export const useCartStore = create<CartStore>((set) => ({
  items: [],
  addItem: (item) => set((state) => {
    const existing = state.items.findIndex((i) => i.id === item.id)
    if (existing >= 0) {
      const items = [...state.items]
      items[existing].qty += 1
      return { items }
    }
    return { items: [...state.items, { id: item.id, name: item.name, price: item.price, qty: 1 }] }
  }),
  removeItem: (index) => set((state) => ({ items: state.items.filter((_, i) => i !== index) })),
  clear: () => set({ items: [] }),
}))
