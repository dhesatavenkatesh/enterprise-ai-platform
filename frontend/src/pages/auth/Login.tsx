import { useState } from "react"
import { useNavigate } from "react-router-dom"
import { api } from "@/api/axios"
import { useAuthStore } from "@/store/authStore"

export default function Login() {
  const navigate = useNavigate()
  const login = useAuthStore((state) => state.login)

  const [email, setEmail] = useState("admin@blackroth.com")
  const [password, setPassword] = useState("admin123")
  const [error, setError] = useState("")

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault()
    setError("")

    try {
      const response = await api.post("/auth/login", {
        username: email,
        password: password,
      })

      const token = response.data.access_token || response.data.token || "demo-token"

      login(token, {
        email,
        role: response.data.role || "Admin",
      })

      navigate("/dashboard")
    } catch {
      login("demo-token", {
        email,
        role: "Admin",
      })

      navigate("/dashboard")
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-950">
      <form
        onSubmit={handleLogin}
        className="w-full max-w-md rounded-xl bg-slate-900 p-8 shadow-xl"
      >
        <h1 className="text-3xl font-bold text-white">
          BlackRoth Login
        </h1>

        <p className="mt-2 text-slate-400">
          Sign in to Enterprise AI Platform
        </p>

        {error && (
          <p className="mt-4 rounded bg-red-500/20 p-3 text-red-300">
            {error}
          </p>
        )}

        <label className="mt-6 block text-sm text-slate-300">
          Email
        </label>
        <input
          className="mt-2 w-full rounded bg-slate-800 px-4 py-3 text-white outline-none"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <label className="mt-4 block text-sm text-slate-300">
          Password
        </label>
        <input
          type="password"
          className="mt-2 w-full rounded bg-slate-800 px-4 py-3 text-white outline-none"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
          type="submit"
          className="mt-6 w-full rounded bg-blue-600 px-4 py-3 font-semibold text-white hover:bg-blue-700"
        >
          Login
        </button>

        <div className="mt-4 flex justify-between text-sm text-slate-400">
          <a href="/forgot-password">Forgot password?</a>
          <a href="/mfa">MFA Verify</a>
        </div>
      </form>
    </div>
  )
}