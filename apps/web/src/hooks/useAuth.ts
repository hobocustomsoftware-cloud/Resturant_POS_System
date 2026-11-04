import { create } from 'zustand'

interface AuthState {
  token: string | null
  setToken: (token: string | null) => void
}

export const useAuthStore = create<AuthState>((set) => ({
  token: localStorage.getItem('access_token'),
  setToken: (token) => {
    if (token) localStorage.setItem('access_token', token)
    else localStorage.removeItem('access_token')
    set({ token })
  },
}))
