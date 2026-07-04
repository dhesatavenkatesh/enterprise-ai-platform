import { create } from "zustand"

type User = {
  email: string
  role: string
}

type AuthStore = {
  token: string | null
  user: User | null
  login: (token: string, user: User) => void
  logout: () => void
}

export const useAuthStore = create<AuthStore>((set) => ({
  token: localStorage.getItem("access_token"),
  user: null,

  login: (token, user) => {
    localStorage.setItem("access_token", token)
    set({ token, user })
  },

  logout: () => {
    localStorage.removeItem("access_token")
    set({ token: null, user: null })
  },
}))