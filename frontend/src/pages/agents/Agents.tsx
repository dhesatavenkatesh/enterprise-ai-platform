import { useState } from "react"
import {
  Activity,
  Bot,
  Brain,
  Play,
  RefreshCw,
  Square,
  Wrench,
} from "lucide-react"

type AgentStatus = "Running" | "Stopped" | "Idle"

type Agent = {
  id: number
  name: string
  role: string
  status: AgentStatus
  health: number
  runningTasks: number
  toolUsage: number
  sessions: number
  lastExecution: string
}

const initialAgents: Agent[] = [
  {
    id: 1,
    name: "HR Agent",
    role: "HR Automation",
    status: "Running",
    health: 98,
    runningTasks: 4,
    toolUsage: 128,
    sessions: 12,
    lastExecution: "2 minutes ago",
  },
  {
    id: 2,
    name: "Payroll Agent",
    role: "Payroll Automation",
    status: "Idle",
    health: 96,
    runningTasks: 0,
    toolUsage: 84,
    sessions: 5,
    lastExecution: "10 minutes ago",
  },
  {
    id: 3,
    name: "Knowledge Agent",
    role: "Enterprise Search",
    status: "Running",
    health: 99,
    runningTasks: 8,
    toolUsage: 342,
    sessions: 24,
    lastExecution: "Just now",
  },
  {
    id: 4,
    name: "Project Agent",
    role: "Project Management",
    status: "Stopped",
    health: 88,
    runningTasks: 0,
    toolUsage: 65,
    sessions: 0,
    lastExecution: "1 hour ago",
  },
]

export default function Agents() {
  const [agents, setAgents] = useState(initialAgents)
  const [selectedAgent, setSelectedAgent] = useState<Agent | null>(null)

  const updateStatus = (id: number, status: AgentStatus) => {
    setAgents((currentAgents) =>
      currentAgents.map((agent) =>
        agent.id === id ? { ...agent, status } : agent
      )
    )
  }

  const runningAgents = agents.filter(
    (agent) => agent.status === "Running"
  ).length

  const runningTasks = agents.reduce(
    (total, agent) => total + agent.runningTasks,
    0
  )

  const totalToolUsage = agents.reduce(
    (total, agent) => total + agent.toolUsage,
    0
  )

  const averageHealth = Math.round(
    agents.reduce((total, agent) => total + agent.health, 0) /
      agents.length
  )

  return (
    <main className="min-h-screen bg-slate-950 p-6 text-white">
      <div className="mx-auto max-w-7xl">
        <header className="mb-8">
          <p className="text-sm text-slate-400">
            BlackRoth Enterprise AI
          </p>

          <h1 className="text-3xl font-bold">
            AI Agent Dashboard
          </h1>

          <p className="mt-2 text-slate-400">
            Monitor and control enterprise AI agents.
          </p>
        </header>

        <section className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          <MetricCard
            title="Active Agents"
            value={runningAgents}
            icon={<Bot />}
          />

          <MetricCard
            title="Running Tasks"
            value={runningTasks}
            icon={<Activity />}
          />

          <MetricCard
            title="Average Health"
            value={`${averageHealth}%`}
            icon={<Brain />}
          />

          <MetricCard
            title="Tool Usage"
            value={totalToolUsage}
            icon={<Wrench />}
          />
        </section>

        <section className="mt-6 grid gap-6 lg:grid-cols-2">
          {agents.map((agent) => (
            <article
              key={agent.id}
              className="rounded-xl border border-slate-800 bg-slate-900 p-6"
            >
              <div className="flex items-start justify-between">
                <div>
                  <h2 className="text-xl font-semibold">
                    {agent.name}
                  </h2>

                  <p className="mt-1 text-sm text-slate-400">
                    {agent.role}
                  </p>
                </div>

                <StatusBadge status={agent.status} />
              </div>

              <div className="mt-6 grid grid-cols-2 gap-4">
                <AgentStat
                  label="Health"
                  value={`${agent.health}%`}
                />

                <AgentStat
                  label="Running Tasks"
                  value={agent.runningTasks}
                />

                <AgentStat
                  label="Tool Usage"
                  value={agent.toolUsage}
                />

                <AgentStat
                  label="Active Sessions"
                  value={agent.sessions}
                />
              </div>

              <div className="mt-5">
                <div className="mb-2 flex justify-between text-sm">
                  <span className="text-slate-400">
                    Agent Health
                  </span>

                  <span>{agent.health}%</span>
                </div>

                <div className="h-2 rounded-full bg-slate-800">
                  <div
                    className="h-2 rounded-full bg-green-500"
                    style={{ width: `${agent.health}%` }}
                  />
                </div>
              </div>

              <p className="mt-4 text-sm text-slate-500">
                Last execution: {agent.lastExecution}
              </p>

              <div className="mt-6 flex flex-wrap gap-2">
                <button
                  onClick={() => updateStatus(agent.id, "Running")}
                  className="flex items-center gap-2 rounded-lg bg-green-600 px-3 py-2 text-sm hover:bg-green-700"
                >
                  <Play className="h-4 w-4" />
                  Start
                </button>

                <button
                  onClick={() => updateStatus(agent.id, "Stopped")}
                  className="flex items-center gap-2 rounded-lg bg-red-600 px-3 py-2 text-sm hover:bg-red-700"
                >
                  <Square className="h-4 w-4" />
                  Stop
                </button>

                <button
                  onClick={() => updateStatus(agent.id, "Running")}
                  className="flex items-center gap-2 rounded-lg bg-blue-600 px-3 py-2 text-sm hover:bg-blue-700"
                >
                  <RefreshCw className="h-4 w-4" />
                  Restart
                </button>

                <button
                  onClick={() => setSelectedAgent(agent)}
                  className="flex items-center gap-2 rounded-lg bg-slate-800 px-3 py-2 text-sm hover:bg-slate-700"
                >
                  <Brain className="h-4 w-4" />
                  View Memory
                </button>
              </div>
            </article>
          ))}
        </section>

        <section className="mt-6 grid gap-6 lg:grid-cols-2">
          <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">
              Agent Logs
            </h2>

            <div className="mt-4 space-y-3 font-mono text-sm text-slate-400">
              <p>[10:30:21] HR Agent started leave workflow.</p>
              <p>[10:31:05] Knowledge Agent called hybrid search.</p>
              <p>[10:32:42] Payroll Agent completed validation.</p>
              <p>[10:35:12] Project Agent stopped.</p>
            </div>
          </div>

          <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">
              Execution History
            </h2>

            <div className="mt-4 space-y-3">
              <ExecutionItem
                agent="HR Agent"
                task="Leave Approval"
                status="Success"
              />

              <ExecutionItem
                agent="Knowledge Agent"
                task="Document Search"
                status="Success"
              />

              <ExecutionItem
                agent="Project Agent"
                task="Project Update"
                status="Failed"
              />
            </div>
          </div>
        </section>

        {selectedAgent && (
          <section className="mt-6 rounded-xl border border-blue-800 bg-slate-900 p-6">
            <div className="flex items-center justify-between">
              <div>
                <h2 className="text-xl font-semibold">
                  {selectedAgent.name} Memory
                </h2>

                <p className="mt-2 text-slate-400">
                  Current enterprise context and recent activity.
                </p>
              </div>

              <button
                onClick={() => setSelectedAgent(null)}
                className="rounded-lg bg-slate-800 px-4 py-2"
              >
                Close
              </button>
            </div>

            <div className="mt-5 rounded-lg bg-slate-950 p-4 text-sm text-slate-300">
              <p>Role: {selectedAgent.role}</p>
              <p>Status: {selectedAgent.status}</p>
              <p>Active sessions: {selectedAgent.sessions}</p>
              <p>Recent tool calls: {selectedAgent.toolUsage}</p>
              <p>Last execution: {selectedAgent.lastExecution}</p>
            </div>
          </section>
        )}
      </div>
    </main>
  )
}

function MetricCard({
  title,
  value,
  icon,
}: {
  title: string
  value: string | number
  icon: React.ReactNode
}) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-5">
      <div className="flex items-center justify-between">
        <p className="text-sm text-slate-400">{title}</p>
        <div className="text-slate-400">{icon}</div>
      </div>

      <p className="mt-3 text-3xl font-bold">{value}</p>
    </div>
  )
}

function AgentStat({
  label,
  value,
}: {
  label: string
  value: string | number
}) {
  return (
    <div className="rounded-lg bg-slate-800 p-3">
      <p className="text-xs text-slate-400">{label}</p>
      <p className="mt-1 font-semibold">{value}</p>
    </div>
  )
}

function StatusBadge({ status }: { status: AgentStatus }) {
  const style =
    status === "Running"
      ? "bg-green-500/20 text-green-300"
      : status === "Idle"
        ? "bg-yellow-500/20 text-yellow-300"
        : "bg-red-500/20 text-red-300"

  return (
    <span className={`rounded-full px-3 py-1 text-xs ${style}`}>
      {status}
    </span>
  )
}

function ExecutionItem({
  agent,
  task,
  status,
}: {
  agent: string
  task: string
  status: string
}) {
  return (
    <div className="flex items-center justify-between rounded-lg bg-slate-800 p-4">
      <div>
        <p className="font-medium">{task}</p>
        <p className="text-sm text-slate-400">{agent}</p>
      </div>

      <span
        className={
          status === "Success"
            ? "text-green-400"
            : "text-red-400"
        }
      >
        {status}
      </span>
    </div>
  )
}