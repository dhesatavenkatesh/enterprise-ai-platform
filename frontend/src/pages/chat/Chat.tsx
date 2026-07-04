import { useState } from "react"
import { Copy, ThumbsDown, ThumbsUp } from "lucide-react"
import { api } from "@/api/axios"

type Source = {
  file_name?: string
  department?: string
  chunk_id?: string
}

type Message = {
  role: "user" | "assistant"
  content: string
  sources?: Source[]
}

const suggestions = [
  "What is the leave policy?",
  "Show HR policies",
  "How many annual leave days are allowed?",
  "What is the work from home policy?",
]

export default function Chat() {
  const [sessionId, setSessionId] = useState("")
  const [messages, setMessages] = useState<Message[]>([])
  const [question, setQuestion] = useState("")
  const [loading, setLoading] = useState(false)

  const createSession = async () => {
    try {
      const response = await api.post("/chat/session")
      setSessionId(response.data.session_id)
    } catch {
      setSessionId("demo-session")
    }
  }

  const sendMessage = async (text?: string) => {
    const finalQuestion = text || question

    if (!finalQuestion.trim()) return

    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: finalQuestion,
      },
    ])

    setQuestion("")
    setLoading(true)

    try {
      const response = await api.post("/chat/", {
        session_id: sessionId || "demo-session",
        question: finalQuestion,
        department: "hr_docs",
      })

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            response.data.answer ||
            "This is a simulated AI response from the Enterprise RAG engine.",
          sources: response.data.sources || [],
        },
      ])
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            "This is a demo response. Backend connection is not available right now.",
          sources: [
            {
              file_name: "company_handbook.txt",
              department: "HR",
              chunk_id: "chunk_1",
            },
          ],
        },
      ])
    } finally {
      setLoading(false)
    }
  }

  const copyText = (text: string) => {
    navigator.clipboard.writeText(text)
  }

  return (
    <main className="min-h-screen bg-slate-950 p-6 text-white">
      <div className="mx-auto max-w-6xl">
        <header className="mb-6 flex items-center justify-between">
          <div>
            <p className="text-sm text-slate-400">
              BlackRoth Enterprise AI
            </p>
            <h1 className="text-3xl font-bold">
              AI Chat Interface
            </h1>
            <p className="mt-2 text-slate-400">
              Ask questions from enterprise knowledge with source citations.
            </p>
          </div>

          <button
            onClick={createSession}
            className="rounded-lg bg-blue-600 px-4 py-2 font-medium hover:bg-blue-700"
          >
            New Session
          </button>
        </header>

        <section className="mb-4 rounded-xl border border-slate-800 bg-slate-900 p-4">
          <p className="text-sm text-slate-400">
            Session ID:
          </p>
          <p className="mt-1 break-all font-mono text-sm">
            {sessionId || "No session created yet"}
          </p>
        </section>

        <section className="grid gap-6 lg:grid-cols-[1fr_300px]">
          <div className="rounded-xl border border-slate-800 bg-slate-900">
            <div className="h-[560px] space-y-4 overflow-y-auto p-5">
              {messages.length === 0 && (
                <div className="flex h-full items-center justify-center text-center text-slate-400">
                  <div>
                    <h2 className="text-xl font-semibold text-white">
                      Start a conversation
                    </h2>
                    <p className="mt-2">
                      Ask about HR policies, workflows, agents, or documents.
                    </p>
                  </div>
                </div>
              )}

              {messages.map((message, index) => (
                <div
                  key={index}
                  className={
                    message.role === "user"
                      ? "flex justify-end"
                      : "flex justify-start"
                  }
                >
                  <div
                    className={
                      message.role === "user"
                        ? "max-w-[80%] rounded-xl bg-blue-600 p-4"
                        : "max-w-[80%] rounded-xl bg-slate-800 p-4"
                    }
                  >
                    <p className="whitespace-pre-wrap">
                      {message.content}
                    </p>

                    {message.role === "assistant" && (
                      <div className="mt-4 flex gap-2">
                        <button
                          onClick={() => copyText(message.content)}
                          className="rounded bg-slate-700 px-3 py-1 text-sm hover:bg-slate-600"
                        >
                          <Copy className="mr-1 inline h-4 w-4" />
                          Copy
                        </button>

                        <button className="rounded bg-slate-700 px-3 py-1 text-sm hover:bg-slate-600">
                          <ThumbsUp className="mr-1 inline h-4 w-4" />
                          Helpful
                        </button>

                        <button className="rounded bg-slate-700 px-3 py-1 text-sm hover:bg-slate-600">
                          <ThumbsDown className="mr-1 inline h-4 w-4" />
                          Not Helpful
                        </button>
                      </div>
                    )}

                    {message.sources && message.sources.length > 0 && (
                      <div className="mt-4 rounded-lg bg-slate-950 p-3">
                        <p className="mb-2 text-sm font-semibold text-slate-300">
                          Sources
                        </p>

                        {message.sources.map((source, sourceIndex) => (
                          <div
                            key={sourceIndex}
                            className="mb-2 text-sm text-slate-400"
                          >
                            <p>File: {source.file_name || "Unknown"}</p>
                            <p>Department: {source.department || "Unknown"}</p>
                            <p>Chunk: {source.chunk_id || "N/A"}</p>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                </div>
              ))}

              {loading && (
                <div className="flex justify-start">
                  <div className="rounded-xl bg-slate-800 p-4 text-slate-400">
                    AI is typing...
                  </div>
                </div>
              )}
            </div>

            <div className="border-t border-slate-800 p-4">
              <div className="flex gap-3">
                <input
                  value={question}
                  onChange={(e) => setQuestion(e.target.value)}
                  onKeyDown={(e) => {
                    if (e.key === "Enter") sendMessage()
                  }}
                  placeholder="Ask anything about enterprise knowledge..."
                  className="flex-1 rounded-lg bg-slate-800 px-4 py-3 text-white outline-none"
                />

                <button
                  onClick={() => sendMessage()}
                  className="rounded-lg bg-blue-600 px-6 py-3 font-medium hover:bg-blue-700"
                >
                  Send
                </button>
              </div>
            </div>
          </div>

          <aside className="rounded-xl border border-slate-800 bg-slate-900 p-5">
            <h2 className="text-lg font-semibold">
              Suggested Questions
            </h2>

            <div className="mt-4 space-y-3">
              {suggestions.map((item) => (
                <button
                  key={item}
                  onClick={() => sendMessage(item)}
                  className="w-full rounded-lg bg-slate-800 p-3 text-left text-sm text-slate-300 hover:bg-slate-700"
                >
                  {item}
                </button>
              ))}
            </div>

            <div className="mt-8">
              <h2 className="text-lg font-semibold">
                Features
              </h2>

              <ul className="mt-4 space-y-2 text-sm text-slate-400">
                <li>• Chat history</li>
                <li>• Typing indicator</li>
                <li>• Source citations</li>
                <li>• Feedback buttons</li>
                <li>• Copy response</li>
              </ul>
            </div>
          </aside>
        </section>
      </div>
    </main>
  )
}