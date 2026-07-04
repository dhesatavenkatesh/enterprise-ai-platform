import {
  Activity,
  Bot,
  Clock3,
  Database,
  GitBranch,
  MessageSquare,
  Users,
  WalletCards,
} from "lucide-react"

import {
  Area,
  AreaChart,
  Bar,
  BarChart,
  CartesianGrid,
  Line,
  LineChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Progress } from "@/components/ui/progress"
import { useAuthStore } from "@/store/authStore"

const dailyRequests = [
  { day: "Mon", requests: 320 },
  { day: "Tue", requests: 480 },
  { day: "Wed", requests: 410 },
  { day: "Thu", requests: 620 },
  { day: "Fri", requests: 760 },
  { day: "Sat", requests: 430 },
  { day: "Sun", requests: 520 },
]

const aiUsage = [
  { time: "08:00", usage: 120 },
  { time: "10:00", usage: 260 },
  { time: "12:00", usage: 340 },
  { time: "14:00", usage: 510 },
  { time: "16:00", usage: 470 },
  { time: "18:00", usage: 620 },
]

const costData = [
  { month: "Jan", cost: 120 },
  { month: "Feb", cost: 180 },
  { month: "Mar", cost: 150 },
  { month: "Apr", cost: 240 },
  { month: "May", cost: 290 },
  { month: "Jun", cost: 260 },
]

const retrievalData = [
  { metric: "Recall@5", score: 92 },
  { metric: "Precision@5", score: 89 },
  { metric: "MRR", score: 94 },
  { metric: "Citation", score: 96 },
]

const stats = [
  {
    title: "Active AI Sessions",
    value: "128",
    description: "+12% from yesterday",
    icon: MessageSquare,
  },
  {
    title: "Active Users",
    value: "342",
    description: "28 online now",
    icon: Users,
  },
  {
    title: "Running Agents",
    value: "18",
    description: "All systems healthy",
    icon: Bot,
  },
  {
    title: "Knowledge Base Size",
    value: "24.8 GB",
    description: "12,540 documents",
    icon: Database,
  },
  {
    title: "Today's Queries",
    value: "4,862",
    description: "+8.4% today",
    icon: Activity,
  },
  {
    title: "Average Response Time",
    value: "1.2 sec",
    description: "Within target",
    icon: Clock3,
  },
  {
    title: "Token Usage",
    value: "2.4M",
    description: "68% monthly budget",
    icon: WalletCards,
  },
  {
    title: "Workflow Status",
    value: "96%",
    description: "Success rate",
    icon: GitBranch,
  },
]

export default function Dashboard() {
  const user = useAuthStore((state) => state.user)
  const logout = useAuthStore((state) => state.logout)

  return (
    <main className="min-h-screen bg-slate-950 p-6 text-white md:p-8">
      <div className="mx-auto max-w-7xl">
        <header className="mb-8 flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
          <div>
            <p className="text-sm text-slate-400">
              BlackRoth Enterprise AI Platform
            </p>

            <h1 className="mt-1 text-3xl font-bold">
              Enterprise Dashboard
            </h1>

            <p className="mt-2 text-slate-400">
              Monitor AI usage, agents, workflows, and platform performance.
            </p>
          </div>

          <div className="flex items-center gap-4">
            <div className="text-right">
              <p className="font-medium">
                {user?.email || "Administrator"}
              </p>
              <p className="text-sm text-slate-400">
                {user?.role || "Admin"}
              </p>
            </div>

            <button
              onClick={logout}
              className="rounded-lg bg-red-600 px-4 py-2 font-medium hover:bg-red-700"
            >
              Logout
            </button>
          </div>
        </header>

        <section className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {stats.map((stat) => {
            const Icon = stat.icon

            return (
              <Card
                key={stat.title}
                className="border-slate-800 bg-slate-900 text-white"
              >
                <CardContent className="p-6">
                  <div className="flex items-start justify-between">
                    <div>
                      <p className="text-sm text-slate-400">
                        {stat.title}
                      </p>

                      <p className="mt-2 text-3xl font-bold">
                        {stat.value}
                      </p>
                    </div>

                    <Icon className="h-6 w-6 text-slate-400" />
                  </div>

                  <p className="mt-4 text-sm text-slate-500">
                    {stat.description}
                  </p>
                </CardContent>
              </Card>
            )
          })}
        </section>

        <section className="mt-6 grid gap-6 lg:grid-cols-2">
          <Card className="border-slate-800 bg-slate-900 text-white">
            <CardHeader>
              <CardTitle>Daily Requests</CardTitle>
            </CardHeader>

            <CardContent>
              <div className="h-72">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={dailyRequests}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="day" />
                    <YAxis />
                    <Tooltip />
                    <Bar dataKey="requests" fill="currentColor" />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </CardContent>
          </Card>

          <Card className="border-slate-800 bg-slate-900 text-white">
            <CardHeader>
              <CardTitle>AI Usage Trends</CardTitle>
            </CardHeader>

            <CardContent>
              <div className="h-72">
                <ResponsiveContainer width="100%" height="100%">
                  <AreaChart data={aiUsage}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="time" />
                    <YAxis />
                    <Tooltip />
                    <Area
                      type="monotone"
                      dataKey="usage"
                      fill="currentColor"
                      stroke="currentColor"
                      fillOpacity={0.2}
                    />
                  </AreaChart>
                </ResponsiveContainer>
              </div>
            </CardContent>
          </Card>

          <Card className="border-slate-800 bg-slate-900 text-white">
            <CardHeader>
              <CardTitle>Cost Analytics</CardTitle>
            </CardHeader>

            <CardContent>
              <div className="h-72">
                <ResponsiveContainer width="100%" height="100%">
                  <LineChart data={costData}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="month" />
                    <YAxis />
                    <Tooltip />
                    <Line
                      type="monotone"
                      dataKey="cost"
                      stroke="currentColor"
                      strokeWidth={2}
                    />
                  </LineChart>
                </ResponsiveContainer>
              </div>
            </CardContent>
          </Card>

          <Card className="border-slate-800 bg-slate-900 text-white">
            <CardHeader>
              <CardTitle>Retrieval Performance</CardTitle>
            </CardHeader>

            <CardContent className="space-y-6">
              {retrievalData.map((item) => (
                <div key={item.metric}>
                  <div className="mb-2 flex justify-between">
                    <span className="text-sm text-slate-300">
                      {item.metric}
                    </span>
                    <span className="font-medium">
                      {item.score}%
                    </span>
                  </div>

                  <Progress value={item.score} />
                </div>
              ))}
            </CardContent>
          </Card>
        </section>
      </div>
    </main>
  )
}