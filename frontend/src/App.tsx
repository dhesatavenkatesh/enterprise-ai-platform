import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom"

import Login from "@/pages/auth/Login"
import ForgotPassword from "@/pages/auth/ForgotPassword"
import ResetPassword from "@/pages/auth/ResetPassword"
import MFA from "@/pages/auth/MFA"

import Dashboard from "@/pages/dashboard/Dashboard"
import Chat from "@/pages/chat/Chat"
import Knowledge from "@/pages/knowledge/Knowledge"
import Agents from "@/pages/agents/Agents"
import Workflows from "@/pages/workflows/Workflows"
import Admin from "@/pages/admin/Admin"
import Analytics from "@/pages/analytics/Analytics"
import Settings from "@/pages/settings/Settings"
import Profile from "@/pages/profile/Profile"

import ProtectedRoute from "@/components/ProtectedRoute"
import OfflineBanner from "@/components/OfflineBanner"
import WorkspaceLayout from "@/layouts/WorkspaceLayout"

function App() {
  return (
    <BrowserRouter>
      <OfflineBanner />

      <Routes>
        <Route path="/" element={<Navigate to="/login" replace />} />

        <Route path="/login" element={<Login />} />
        <Route path="/forgot-password" element={<ForgotPassword />} />
        <Route path="/reset-password" element={<ResetPassword />} />
        <Route path="/mfa" element={<MFA />} />

        <Route
          element={
            <ProtectedRoute>
              <WorkspaceLayout />
            </ProtectedRoute>
          }
        >
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/chat" element={<Chat />} />
          <Route path="/knowledge" element={<Knowledge />} />
          <Route path="/agents" element={<Agents />} />
          <Route path="/workflows" element={<Workflows />} />
          <Route path="/analytics" element={<Analytics />} />
          <Route path="/admin" element={<Admin />} />
          <Route path="/settings" element={<Settings />} />
          <Route path="/profile" element={<Profile />} />
        </Route>

        <Route path="*" element={<Navigate to="/login" replace />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App