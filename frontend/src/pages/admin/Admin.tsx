import { useState } from "react"
import { Settings, Shield, Trash2, UserPlus, Users } from "lucide-react"

type User = {
  id: number
  name: string
  email: string
  role: string
  status: string
}

const initialUsers: User[] = [
  {
    id: 1,
    name: "D. Venkatesh",
    email: "venky@blackroth.com",
    role: "Admin",
    status: "Active",
  },
  {
    id: 2,
    name: "HR User",
    email: "hr@blackroth.com",
    role: "HR",
    status: "Active",
  },
  {
    id: 3,
    name: "Employee User",
    email: "employee@blackroth.com",
    role: "Employee",
    status: "Inactive",
  },
]

export default function Admin() {
  const [users, setUsers] = useState(initialUsers)
  const [model, setModel] = useState("GPT-4")
  const [temperature, setTemperature] = useState(0.3)
  const [tokenLimit, setTokenLimit] = useState(4000)

  const deleteUser = (id: number) => {
    setUsers((prev) => prev.filter((user) => user.id !== id))
  }

  const addUser = () => {
    const newUser = {
      id: Date.now(),
      name: "New User",
      email: "newuser@blackroth.com",
      role: "Employee",
      status: "Active",
    }

    setUsers((prev) => [...prev, newUser])
  }

  return (
    <main className="min-h-screen bg-slate-950 p-6 text-white">
      <div className="mx-auto max-w-7xl">
        <header className="mb-8">
          <p className="text-sm text-slate-400">
            BlackRoth Enterprise AI
          </p>
          <h1 className="text-3xl font-bold">
            Admin Console
          </h1>
          <p className="mt-2 text-slate-400">
            Manage users, roles, AI settings, permissions, and audit logs.
          </p>
        </header>

        <section className="mb-6 grid gap-4 md:grid-cols-4">
          <Metric title="Total Users" value={users.length} />
          <Metric title="Active Users" value={users.filter((u) => u.status === "Active").length} />
          <Metric title="Roles" value="4" />
          <Metric title="Audit Events" value="128" />
        </section>

        <section className="grid gap-6 lg:grid-cols-2">
          <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
            <div className="mb-5 flex items-center justify-between">
              <div>
                <h2 className="flex items-center gap-2 text-xl font-semibold">
                  <Users className="h-5 w-5" />
                  User Management
                </h2>
                <p className="mt-1 text-sm text-slate-400">
                  Create, update, delete users and assign roles.
                </p>
              </div>

              <button
                onClick={addUser}
                className="flex items-center gap-2 rounded bg-blue-600 px-4 py-2 text-sm hover:bg-blue-700"
              >
                <UserPlus className="h-4 w-4" />
                Add User
              </button>
            </div>

            <div className="space-y-3">
              {users.map((user) => (
                <div
                  key={user.id}
                  className="flex items-center justify-between rounded-lg bg-slate-800 p-4"
                >
                  <div>
                    <p className="font-medium">{user.name}</p>
                    <p className="text-sm text-slate-400">{user.email}</p>
                    <p className="mt-1 text-xs text-slate-500">
                      Role: {user.role} | Status: {user.status}
                    </p>
                  </div>

                  <button
                    onClick={() => deleteUser(user.id)}
                    className="rounded bg-red-600 p-2 hover:bg-red-700"
                  >
                    <Trash2 className="h-4 w-4" />
                  </button>
                </div>
              ))}
            </div>
          </div>

          <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="flex items-center gap-2 text-xl font-semibold">
              <Shield className="h-5 w-5" />
              Role Management
            </h2>

            <div className="mt-5 space-y-4">
              {["Admin", "HR", "Manager", "Employee"].map((role) => (
                <div
                  key={role}
                  className="rounded-lg bg-slate-800 p-4"
                >
                  <p className="font-medium">{role}</p>
                  <p className="mt-1 text-sm text-slate-400">
                    Permissions: View, Search, Chat
                    {role === "Admin" ? ", Manage Users, Delete, Configure AI" : ""}
                    {role === "HR" ? ", Approve Documents, HR Workflows" : ""}
                    {role === "Manager" ? ", Approve Requests, View Reports" : ""}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section className="mt-6 grid gap-6 lg:grid-cols-2">
          <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="flex items-center gap-2 text-xl font-semibold">
              <Settings className="h-5 w-5" />
              AI Settings
            </h2>

            <div className="mt-5 space-y-5">
              <div>
                <label className="text-sm text-slate-400">
                  Model Selection
                </label>
                <select
                  value={model}
                  onChange={(e) => setModel(e.target.value)}
                  className="mt-2 w-full rounded bg-slate-800 px-4 py-3 outline-none"
                >
                  <option>GPT-4</option>
                  <option>GPT-4o</option>
                  <option>Claude</option>
                  <option>Local LLM</option>
                </select>
              </div>

              <div>
                <label className="text-sm text-slate-400">
                  Temperature: {temperature}
                </label>
                <input
                  type="range"
                  min="0"
                  max="1"
                  step="0.1"
                  value={temperature}
                  onChange={(e) => setTemperature(Number(e.target.value))}
                  className="mt-2 w-full"
                />
              </div>

              <div>
                <label className="text-sm text-slate-400">
                  Token Limit
                </label>
                <input
                  type="number"
                  value={tokenLimit}
                  onChange={(e) => setTokenLimit(Number(e.target.value))}
                  className="mt-2 w-full rounded bg-slate-800 px-4 py-3 outline-none"
                />
              </div>

              <div>
                <label className="text-sm text-slate-400">
                  Prompt Template
                </label>
                <textarea
                  defaultValue="Answer using enterprise knowledge and include citations."
                  className="mt-2 h-28 w-full rounded bg-slate-800 px-4 py-3 outline-none"
                />
              </div>
            </div>
          </div>

          <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">
              Audit Logs
            </h2>

            <div className="mt-5 space-y-3 font-mono text-sm text-slate-400">
              <p>[09:10:20] Admin created user HR User.</p>
              <p>[09:25:44] HR approved document HR Policy.pdf.</p>
              <p>[10:05:12] Employee accessed AI Chat.</p>
              <p>[10:32:03] Payroll tool call executed.</p>
              <p>[11:00:18] Security event: token refreshed.</p>
            </div>
          </div>
        </section>
      </div>
    </main>
  )
}

function Metric({
  title,
  value,
}: {
  title: string
  value: string | number
}) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-5">
      <p className="text-sm text-slate-400">{title}</p>
      <p className="mt-3 text-3xl font-bold">{value}</p>
    </div>
  )
}
