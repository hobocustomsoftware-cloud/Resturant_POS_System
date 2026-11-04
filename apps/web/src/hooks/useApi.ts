import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import api from '@/lib/api'

export const useCategories = () => useQuery({ queryKey: ['categories'], queryFn: () => api.get('/catalog/categories/').then(r => r.data) })
export const useItems = (params?: any) => useQuery({ queryKey: ['items', params], queryFn: () => api.get('/catalog/items/', { params }).then(r => r.data) })
export const useTables = () => useQuery({ queryKey: ['tables'], queryFn: () => api.get('/sales/tables/').then(r => r.data) })
export const useOrders = () => useQuery({ queryKey: ['orders'], queryFn: () => api.get('/sales/orders/').then(r => r.data) })
export const useStock = () => useQuery({ queryKey: ['stock'], queryFn: () => api.get('/inventory/stock/').then(r => r.data) })
export const useExpenses = () => useQuery({ queryKey: ['expenses'], queryFn: () => api.get('/expenses/expenses/').then(r => r.data) })
export const useDailyCurrent = () => useQuery({ queryKey: ['daily-current'], queryFn: () => api.get('/daily/sessions/current/').then(r => r.data) })

export const useCreateOrder = () => {
  const qc = useQueryClient()
  return useMutation({
    mutationFn: (data: any) => api.post('/sales/orders/', data),
    onSuccess: () => qc.invalidateQueries({ queryKey: ['orders'] })
  })
}

export const useCompleteOrder = () => {
  const qc = useQueryClient()
  return useMutation({
    mutationFn: (id: string) => api.post(`/sales/orders/${id}/complete/`),
    onSuccess: () => qc.invalidateQueries({ queryKey: ['orders'] })
  })
}

export const useReceivePurchase = () => {
  const qc = useQueryClient()
  return useMutation({
    mutationFn: (id: string) => api.post(`/purchases/purchases/${id}/receive/`),
    onSuccess: () => qc.invalidateQueries({ queryKey: ['stock'] })
  })
}

export const useOpenDay = () => {
  const qc = useQueryClient()
  return useMutation({
    mutationFn: (data: any) => api.post('/daily/sessions/open/', data),
    onSuccess: () => qc.invalidateQueries({ queryKey: ['daily-current'] })
  })
}

export const useCloseDay = () => {
  const qc = useQueryClient()
  return useMutation({
    mutationFn: (id: string) => api.post(`/daily/sessions/${id}/close/`),
    onSuccess: () => qc.invalidateQueries({ queryKey: ['daily-current'] })
  })
}

export const usePurchases = () => useQuery({ queryKey: ['purchases'], queryFn: () => api.get('/purchases/purchases/').then(r => r.data) })
