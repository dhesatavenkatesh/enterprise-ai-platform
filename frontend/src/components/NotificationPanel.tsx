import { Bell } from "lucide-react"
import { useWorkspaceStore } from "@/store/workspaceStore"

export default function NotificationPanel() {
  const notifications = useWorkspaceStore((state) => state.notifications)

  return (
    <div className="fixed right-5 top-5 z-40 rounded-xl border border-slate-800 bg-slate-900 p-4 text-white shadow-xl">
      <div className="mb-3 flex items-center gap-2">
        <Bell className="h-4 w-4" />
        <h2 className="font-semibold">Notifications</h2>
      </div>

      <div className="space-y-2">
        {notifications.map((item) => (
          <div
            key={item.id}
            className="rounded-lg bg-slate-800 px-3 py-2 text-sm text-slate-300"
          >
            {item.message}
          </div>
        ))}
      </div>
    </div>
  )
}