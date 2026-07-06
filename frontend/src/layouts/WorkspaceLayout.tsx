import { useState } from "react"
import { NavLink, Outlet, useNavigate } from "react-router-dom"
import {
  BarChart3,
  Bot,
  BrainCircuit,
  FileText,
  GitBranch,
  LayoutDashboard,
  LogOut,
  Menu,
  Moon,
  Settings,
  Shield,
  User,
  X,
} from "lucide-react"

import CommandPalette from "@/components/CommandPalette"
import NotificationPanel from "@/components/NotificationPanel"
import { useWorkspaceStore } from "@/store/workspaceStore"
import { useAuthStore } from "@/store/authStore"

const navigation = [
  { name: "Dashboard", path: "/dashboard", icon: LayoutDashboard },
  { name: "AI Chat", path: "/chat", icon: BrainCircuit },
  { name: "Knowledge", path: "/knowledge", icon: FileText },
  { name: "Agents", path: "/agents", icon: Bot },
  { name: "Workflows", path: "/workflows", icon: GitBranch },
  { name: "Analytics", path: "/analytics", icon: BarChart3 },
  { name: "Admin", path: "/admin", icon: Shield },
  { name: "Settings", path: "/settings", icon: Settings },
  { name: "Profile", path: "/profile", icon: User },
]

export default function WorkspaceLayout() {
  const [sidebarOpen, setSidebarOpen] = useState(false)

  const logout = useAuthStore((state) => state.logout)
  const toggleDarkMode = useWorkspaceStore((state) => state.toggleDarkMode)

  const navigate = useNavigate()

  const handleLogout = () => {
    logout()
    navigate("/login")
  }

  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <CommandPalette />
      <NotificationPanel />

      <button
        onClick={() => setSidebarOpen(true)}
        className="fixed left-4 top-4 z-40 rounded-lg bg-slate-800 p-2 lg:hidden"
        aria-label="Open navigation"
      >
        <Menu className="h-5 w-5" />
      </button>

      {sidebarOpen && (
        <button
          className="fixed inset-0 z-40 bg-black/60 lg:hidden"
          onClick={() => setSidebarOpen(false)}
          aria-label="Close navigation overlay"
        />
      )}

      <aside
        className={`fixed inset-y-0 left-0 z-50 flex w-64 flex-col border-r border-slate-800 bg-slate-900 transition-transform lg:translate-x-0 ${
          sidebarOpen ? "translate-x-0" : "-translate-x-full"
        }`}
      >
        <div className="flex h-20 items-center justify-between border-b border-slate-800 px-5">
          <div>
            <h1 className="font-bold">BlackRoth AI</h1>
            <p className="text-xs text-slate-400">Enterprise Workspace</p>
          </div>

          <button
            onClick={() => setSidebarOpen(false)}
            className="lg:hidden"
            aria-label="Close navigation"
          >
            <X className="h-5 w-5" />
          </button>
        </div>

        <nav className="flex-1 space-y-1 overflow-y-auto p-4">
          {navigation.map((item) => {
            const Icon = item.icon

            return (
              <NavLink
                key={item.path}
                to={item.path}
                onClick={() => setSidebarOpen(false)}
                className={({ isActive }) =>
                  `flex items-center gap-3 rounded-lg px-4 py-3 text-sm transition ${
                    isActive
                      ? "bg-blue-600 text-white"
                      : "text-slate-400 hover:bg-slate-800 hover:text-white"
                  }`
                }
              >
                <Icon className="h-5 w-5" />
                {item.name}
              </NavLink>
            )
          })}
        </nav>

        <div className="border-t border-slate-800 p-4">
          <button
            onClick={toggleDarkMode}
            className="mb-2 flex w-full items-center gap-3 rounded-lg px-4 py-3 text-sm text-slate-400 hover:bg-slate-800 hover:text-white"
          >
            <Moon className="h-5 w-5" />
            Dark Mode
          </button>

          <button
            onClick={handleLogout}
            className="flex w-full items-center gap-3 rounded-lg px-4 py-3 text-sm text-red-400 hover:bg-red-500/10"
          >
            <LogOut className="h-5 w-5" />
            Logout
          </button>
        </div>
      </aside>

      <div className="lg:pl-64">
        <Outlet />
      </div>
    </div>
  )
}