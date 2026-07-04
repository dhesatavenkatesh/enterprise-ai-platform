import { useEffect } from "react"
import { useNavigate } from "react-router-dom"
import { useWorkspaceStore } from "@/store/workspaceStore"

const commands = [
  { label: "Go to Dashboard", path: "/dashboard" },
  { label: "Open AI Chat", path: "/chat" },
  { label: "Open Knowledge Base", path: "/knowledge" },
  { label: "Open Agents", path: "/agents" },
  { label: "Open Workflows", path: "/workflows" },
  { label: "Open Analytics", path: "/analytics" },
  { label: "Open Admin", path: "/admin" },
  { label: "Open Settings", path: "/settings" },
]

export default function CommandPalette() {
  const navigate = useNavigate()
  const open = useWorkspaceStore((state) => state.commandOpen)
  const setOpen = useWorkspaceStore((state) => state.setCommandOpen)

  useEffect(() => {
    const handler = (event: KeyboardEvent) => {
      if (event.ctrlKey && event.key.toLowerCase() === "k") {
        event.preventDefault()
        setOpen(!open)
      }

      if (event.key === "Escape") {
        setOpen(false)
      }
    }

    window.addEventListener("keydown", handler)
    return () => window.removeEventListener("keydown", handler)
  }, [open, setOpen])

  if (!open) return null

  return (
    <div className="fixed inset-0 z-[100] flex items-start justify-center bg-black/70 pt-28">
      <div className="w-full max-w-xl rounded-xl border border-slate-700 bg-slate-900 p-4 shadow-2xl">
        <input
          autoFocus
          placeholder="Search commands..."
          className="w-full rounded-lg bg-slate-800 px-4 py-3 text-white outline-none"
        />

        <div className="mt-4 space-y-2">
          {commands.map((command) => (
            <button
              key={command.path}
              onClick={() => {
                navigate(command.path)
                setOpen(false)
              }}
              className="w-full rounded-lg px-4 py-3 text-left text-slate-300 hover:bg-slate-800"
            >
              {command.label}
            </button>
          ))}
        </div>

        <p className="mt-4 text-xs text-slate-500">
          Press Esc to close
        </p>
      </div>
    </div>
  )
}