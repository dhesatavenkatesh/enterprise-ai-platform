import { User } from "lucide-react"

export default function Profile() {
  return (
    <main className="min-h-screen bg-slate-950 p-6 text-white">
      <div className="mx-auto max-w-5xl">
        <header className="mb-8">
          <p className="text-sm text-slate-400">
            BlackRoth Enterprise AI
          </p>

          <h1 className="text-3xl font-bold">
            Profile
          </h1>

          <p className="mt-2 text-slate-400">
            Manage your enterprise profile and account information.
          </p>
        </header>

        <section className="rounded-xl border border-slate-800 bg-slate-900 p-6">
          <div className="flex items-center gap-4">
            <div className="rounded-full bg-blue-600 p-4">
              <User className="h-8 w-8" />
            </div>

            <div>
              <h2 className="text-xl font-semibold">
                Enterprise User
              </h2>

              <p className="text-slate-400">
                BlackRoth AI Platform
              </p>
            </div>
          </div>
        </section>
      </div>
    </main>
  )
}