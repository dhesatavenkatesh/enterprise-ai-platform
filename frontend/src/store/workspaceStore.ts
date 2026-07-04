import { create } from "zustand"

type Notification = {
  id: number
  message: string
  type: "info" | "success" | "warning" | "error"
}

type WorkspaceStore = {
  darkMode: boolean
  commandOpen: boolean
  notifications: Notification[]
  toggleDarkMode: () => void
  setCommandOpen: (open: boolean) => void
  addNotification: (notification: Notification) => void
}

export const useWorkspaceStore = create<WorkspaceStore>((set) => ({
  darkMode: true,
  commandOpen: false,
  notifications: [
    {
      id: 1,
      message: "Workflow WF001 is waiting for approval",
      type: "warning",
    },
    {
      id: 2,
      message: "Knowledge Base indexed successfully",
      type: "success",
    },
  ],

  toggleDarkMode: () =>
    set((state) => ({
      darkMode: !state.darkMode,
    })),

  setCommandOpen: (open) =>
    set({
      commandOpen: open,
    }),

  addNotification: (notification) =>
    set((state) => ({
      notifications: [notification, ...state.notifications],
    })),
}))