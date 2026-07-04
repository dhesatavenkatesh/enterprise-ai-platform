import {
  Area,
  AreaChart,
  Bar,
  BarChart,
  CartesianGrid,
  Line,
  LineChart,
  Pie,
  PieChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
  Cell,
} from "recharts"

import {
  Brain,
  Clock,
  Download,
  DollarSign,
  FileText,
  ShieldAlert,
  Star,
  TrendingUp,
} from "lucide-react"

const requestData = [
  { day: "Mon", requests: 1200 },
  { day: "Tue", requests: 1600 },
  { day: "Wed", requests: 1400 },
  { day: "Thu", requests: 2100 },
  { day: "Fri", requests: 2400 },
]

const costData = [
  { month: "Jan", cost: 120 },
  { month: "Feb", cost: 210 },
  { month: "Mar", cost: 180 },
  { month: "Apr", cost: 260 },
  { month: "May", cost: 310 },
]

const agentData = [
  { agent: "HR", score: 96 },
  { agent: "Payroll", score: 91 },
  { agent: "Knowledge", score: 98 },
  { agent: "Project", score: 88 },
]

const ragData = [
  { metric: "Recall@5", value: 94 },
  { metric: "Precision@5", value: 91 },
  { metric: "MRR", value: 93 },
  { metric: "Citation", value: 97 },
]

const sourceData = [
  { name: "HR Policy", value: 35 },
  { name: "Payroll Guide", value: 25 },
  { name: "Project Docs", value: 20 },
  { name: "Support KB", value: 20 },
]

const stats = [
  { title: "AI Requests", value: "8,742", icon: TrendingUp },
  { title: "Total Cost", value: "$310", icon: DollarSign },
  { title: "RAG Accuracy", value: "94%", icon: Brain },
  { title: "Hallucination Rate", value: "2.1%", icon: ShieldAlert },
  { title: "API Response Time", value: "1.1 sec", icon: Clock },
  { title: "Top Sources", value: "248", icon: FileText },
  { title: "User Satisfaction", value: "4.8/5", icon: Star },
]

export default function Analytics() {
  const exportCSV = () => {
    const csv = "Metric,Value\nAI Requests,8742\nCost,310\nRAG Accuracy,94%"
    const blob = new Blob([csv], { type: "text/csv" })
    const url = URL.createObjectURL(blob)

    const link = document.createElement("a")
    link.href = url
    link.download = "analytics_report.csv"
    link.click()
  }

  const exportPDF = () => {
    alert("PDF export placeholder. Connect jsPDF later.")
  }

  return (
    <main className="min-h-screen bg-slate-950 p-6 text-white">
      <div className="mx-auto max-w-7xl">
        <header className="mb-8 flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
          <div>
            <p className="text-sm text-slate-400">
              BlackRoth Enterprise AI
            </p>
            <h1 className="text-3xl font-bold">
              Analytics Dashboard
            </h1>
            <p className="mt-2 text-slate-400">
              Monitor AI usage, cost, RAG quality, latency, and user feedback.
            </p>
          </div>

          <div className="flex gap-3">
            <button
              onClick={exportCSV}
              className="flex items-center gap-2 rounded-lg bg-blue-600 px-4 py-2 hover:bg-blue-700"
            >
              <Download className="h-4 w-4" />
              Export CSV
            </button>

            <button
              onClick={exportPDF}
              className="flex items-center gap-2 rounded-lg bg-slate-800 px-4 py-2 hover:bg-slate-700"
            >
              <Download className="h-4 w-4" />
              Export PDF
            </button>
          </div>
        </header>

        <section className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {stats.map((stat) => {
            const Icon = stat.icon

            return (
              <div
                key={stat.title}
                className="rounded-xl border border-slate-800 bg-slate-900 p-5"
              >
                <div className="flex justify-between">
                  <p className="text-sm text-slate-400">{stat.title}</p>
                  <Icon className="h-5 w-5 text-slate-400" />
                </div>

                <p className="mt-3 text-3xl font-bold">{stat.value}</p>
              </div>
            )
          })}
        </section>

        <section className="mt-6 grid gap-6 lg:grid-cols-2">
          <ChartCard title="AI Requests">
            <BarChart data={requestData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="day" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="requests" fill="currentColor" />
            </BarChart>
          </ChartCard>

          <ChartCard title="Cost Dashboard">
            <LineChart data={costData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="month" />
              <YAxis />
              <Tooltip />
              <Line dataKey="cost" stroke="currentColor" strokeWidth={2} />
            </LineChart>
          </ChartCard>

          <ChartCard title="Agent Performance">
            <BarChart data={agentData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="agent" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="score" fill="currentColor" />
            </BarChart>
          </ChartCard>

          <ChartCard title="Top Knowledge Sources">
            <PieChart>
              <Pie
                data={sourceData}
                dataKey="value"
                nameKey="name"
                outerRadius={100}
                label
              >
                {sourceData.map((_, index) => (
                  <Cell key={index} fill="currentColor" />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ChartCard>

          <ChartCard title="API Response Time">
            <AreaChart data={requestData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="day" />
              <YAxis />
              <Tooltip />
              <Area
                dataKey="requests"
                fill="currentColor"
                stroke="currentColor"
                fillOpacity={0.2}
              />
            </AreaChart>
          </ChartCard>

          <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">RAG Accuracy</h2>

            <div className="mt-5 space-y-5">
              {ragData.map((item) => (
                <div key={item.metric}>
                  <div className="mb-2 flex justify-between text-sm">
                    <span className="text-slate-400">{item.metric}</span>
                    <span>{item.value}%</span>
                  </div>

                  <div className="h-2 rounded-full bg-slate-800">
                    <div
                      className="h-2 rounded-full bg-blue-500"
                      style={{ width: `${item.value}%` }}
                    />
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>
      </div>
    </main>
  )
}

function ChartCard({
  title,
  children,
}: {
  title: string
  children: React.ReactElement
}) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="mb-5 text-xl font-semibold">{title}</h2>

      <div className="h-72">
        <ResponsiveContainer width="100%" height="100%">
          {children}
        </ResponsiveContainer>
      </div>
    </div>
  )
}