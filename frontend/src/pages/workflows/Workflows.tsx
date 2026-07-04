import { useState } from "react"
import {
  CheckCircle,
  Clock,
  GitBranch,
  RotateCcw,
  XCircle,
} from "lucide-react"

type WorkflowStatus = "Running" | "Completed" | "Failed" | "Cancelled"

type Workflow = {
  id: string
  name: string
  requestedBy: string
  status: WorkflowStatus
  currentStep: string
  progress: number
}

const initialWorkflows: Workflow[] = [
  {
    id: "WF001",
    name: "Leave Approval",
    requestedBy: "EMP101",
    status: "Running",
    currentStep: "Manager Approval",
    progress: 60,
  },
  {
    id: "WF002",
    name: "Payroll Generation",
    requestedBy: "ADMIN",
    status: "Completed",
    currentStep: "Confirmation",
    progress: 100,
  },
  {
    id: "WF003",
    name: "Document Approval",
    requestedBy: "HR001",
    status: "Failed",
    currentStep: "Validation",
    progress: 40,
  },
]

export default function Workflows() {
  const [workflows, setWorkflows] = useState(initialWorkflows)

  const retryWorkflow = (id: string) => {
    setWorkflows((prev) =>
      prev.map((workflow) =>
        workflow.id === id
          ? {
              ...workflow,
              status: "Running",
              currentStep: "Retry Queue",
              progress: 50,
            }
          : workflow
      )
    )
  }

  return (
    <main className="min-h-screen bg-slate-950 p-6 text-white">
      <div className="mx-auto max-w-7xl">
        <header className="mb-8">
          <p className="text-sm text-slate-400">
            BlackRoth Enterprise AI
          </p>
          <h1 className="text-3xl font-bold">
            Workflow Management
          </h1>
          <p className="mt-2 text-slate-400">
            Monitor workflows, approvals, retry queues, timelines, and logs.
          </p>
        </header>

        <section className="mb-6 grid gap-4 md:grid-cols-4">
          <MetricCard
            title="Running Workflows"
            value={workflows.filter((w) => w.status === "Running").length}
          />

          <MetricCard
            title="Completed"
            value={workflows.filter((w) => w.status === "Completed").length}
          />

          <MetricCard
            title="Failed"
            value={workflows.filter((w) => w.status === "Failed").length}
          />

          <MetricCard
            title="Retry Queue"
            value={workflows.filter((w) => w.currentStep === "Retry Queue").length}
          />
        </section>

        <section className="rounded-xl border border-slate-800 bg-slate-900">
          <div className="border-b border-slate-800 p-5">
            <h2 className="text-xl font-semibold">
              Workflow List
            </h2>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-left text-sm">
              <thead className="bg-slate-800 text-slate-300">
                <tr>
                  <th className="p-4">Workflow ID</th>
                  <th className="p-4">Name</th>
                  <th className="p-4">Requested By</th>
                  <th className="p-4">Status</th>
                  <th className="p-4">Current Step</th>
                  <th className="p-4">Progress</th>
                  <th className="p-4">Action</th>
                </tr>
              </thead>

              <tbody>
                {workflows.map((workflow) => (
                  <tr key={workflow.id} className="border-t border-slate-800">
                    <td className="p-4 font-mono">{workflow.id}</td>
                    <td className="p-4">{workflow.name}</td>
                    <td className="p-4">{workflow.requestedBy}</td>
                    <td className="p-4">
                      <StatusBadge status={workflow.status} />
                    </td>
                    <td className="p-4">{workflow.currentStep}</td>
                    <td className="p-4">
                      <div className="w-40">
                        <div className="mb-1 text-xs text-slate-400">
                          {workflow.progress}%
                        </div>
                        <div className="h-2 rounded-full bg-slate-800">
                          <div
                            className="h-2 rounded-full bg-blue-500"
                            style={{ width: `${workflow.progress}%` }}
                          />
                        </div>
                      </div>
                    </td>
                    <td className="p-4">
                      {workflow.status === "Failed" ? (
                        <button
                          onClick={() => retryWorkflow(workflow.id)}
                          className="flex items-center gap-2 rounded bg-blue-600 px-3 py-2 text-sm hover:bg-blue-700"
                        >
                          <RotateCcw className="h-4 w-4" />
                          Retry
                        </button>
                      ) : (
                        <span className="text-slate-500">
                          No action
                        </span>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>

        <section className="mt-6 grid gap-6 lg:grid-cols-2">
          <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">
              Approval Queue
            </h2>

            <div className="mt-4 space-y-3">
              <ApprovalItem
                title="Leave Approval"
                requester="EMP101"
                approver="Manager"
              />

              <ApprovalItem
                title="Policy Approval"
                requester="HR001"
                approver="Admin"
              />

              <ApprovalItem
                title="Payroll Approval"
                requester="Finance"
                approver="Admin"
              />
            </div>
          </div>

          <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">
              Workflow Timeline
            </h2>

            <div className="mt-5 space-y-4">
              <TimelineItem
                icon={<CheckCircle className="h-5 w-5 text-green-400" />}
                title="Check Leave Balance"
                status="Completed"
              />

              <TimelineItem
                icon={<CheckCircle className="h-5 w-5 text-green-400" />}
                title="Validate Dates"
                status="Completed"
              />

              <TimelineItem
                icon={<Clock className="h-5 w-5 text-yellow-400" />}
                title="Manager Approval"
                status="In Progress"
              />

              <TimelineItem
                icon={<GitBranch className="h-5 w-5 text-slate-400" />}
                title="HR Notification"
                status="Pending"
              />
            </div>
          </div>
        </section>

        <section className="mt-6 rounded-xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">
            Workflow Logs
          </h2>

          <div className="mt-4 space-y-2 font-mono text-sm text-slate-400">
            <p>[10:10:02] Workflow WF001 started.</p>
            <p>[10:10:10] Leave balance checked successfully.</p>
            <p>[10:10:18] Date validation completed.</p>
            <p>[10:11:03] Waiting for manager approval.</p>
            <p>[10:12:40] Workflow WF003 failed at validation step.</p>
          </div>
        </section>
      </div>
    </main>
  )
}

function MetricCard({
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

function StatusBadge({ status }: { status: WorkflowStatus }) {
  const style =
    status === "Running"
      ? "bg-blue-500/20 text-blue-300"
      : status === "Completed"
        ? "bg-green-500/20 text-green-300"
        : status === "Failed"
          ? "bg-red-500/20 text-red-300"
          : "bg-slate-500/20 text-slate-300"

  return (
    <span className={`rounded-full px-3 py-1 text-xs ${style}`}>
      {status}
    </span>
  )
}

function ApprovalItem({
  title,
  requester,
  approver,
}: {
  title: string
  requester: string
  approver: string
}) {
  return (
    <div className="rounded-lg bg-slate-800 p-4">
      <p className="font-medium">{title}</p>
      <p className="mt-1 text-sm text-slate-400">
        Requester: {requester}
      </p>
      <p className="text-sm text-slate-400">
        Approver: {approver}
      </p>
    </div>
  )
}

function TimelineItem({
  icon,
  title,
  status,
}: {
  icon: React.ReactNode
  title: string
  status: string
}) {
  return (
    <div className="flex items-center gap-3">
      {icon}
      <div>
        <p className="font-medium">{title}</p>
        <p className="text-sm text-slate-400">{status}</p>
      </div>
    </div>
  )
}