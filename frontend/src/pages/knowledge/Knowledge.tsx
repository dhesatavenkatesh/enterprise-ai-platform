import { useState } from "react"
import {
  Download,
  Eye,
  FileText,
  Search,
  Trash2,
  Upload,
} from "lucide-react"

type DocumentItem = {
  id: number
  name: string
  type: string
  department: string
  status: string
  version: string
  tags: string[]
  uploadedBy: string
}

const initialDocuments: DocumentItem[] = [
  {
    id: 1,
    name: "HR Policy.pdf",
    type: "PDF",
    department: "HR",
    status: "Approved",
    version: "v2",
    tags: ["leave", "policy"],
    uploadedBy: "Admin",
  },
  {
    id: 2,
    name: "Payroll Guide.docx",
    type: "DOCX",
    department: "Payroll",
    status: "Pending",
    version: "v1",
    tags: ["salary", "payroll"],
    uploadedBy: "Finance",
  },
]

export default function Knowledge() {
  const [documents, setDocuments] = useState(initialDocuments)
  const [search, setSearch] = useState("")
  const [department, setDepartment] = useState("All")

  const filteredDocuments = documents.filter((doc) => {
    const matchesSearch = doc.name.toLowerCase().includes(search.toLowerCase())
    const matchesDepartment =
      department === "All" || doc.department === department

    return matchesSearch && matchesDepartment
  })

  const deleteDocument = (id: number) => {
    setDocuments((prev) => prev.filter((doc) => doc.id !== id))
  }

  const approveDocument = (id: number) => {
    setDocuments((prev) =>
      prev.map((doc) =>
        doc.id === id ? { ...doc, status: "Approved" } : doc
      )
    )
  }

  return (
    <main className="min-h-screen bg-slate-950 p-6 text-white">
      <div className="mx-auto max-w-7xl">
        <header className="mb-8">
          <p className="text-sm text-slate-400">Knowledge Base</p>
          <h1 className="text-3xl font-bold">Document Management</h1>
          <p className="mt-2 text-slate-400">
            Upload, manage, search, approve, and monitor enterprise documents.
          </p>
        </header>

        <section className="mb-6 grid gap-4 md:grid-cols-4">
          <div className="rounded-xl border border-slate-800 bg-slate-900 p-5">
            <p className="text-sm text-slate-400">Total Documents</p>
            <p className="mt-2 text-3xl font-bold">{documents.length}</p>
          </div>

          <div className="rounded-xl border border-slate-800 bg-slate-900 p-5">
            <p className="text-sm text-slate-400">Approved</p>
            <p className="mt-2 text-3xl font-bold">
              {documents.filter((d) => d.status === "Approved").length}
            </p>
          </div>

          <div className="rounded-xl border border-slate-800 bg-slate-900 p-5">
            <p className="text-sm text-slate-400">Pending</p>
            <p className="mt-2 text-3xl font-bold">
              {documents.filter((d) => d.status === "Pending").length}
            </p>
          </div>

          <div className="rounded-xl border border-slate-800 bg-slate-900 p-5">
            <p className="text-sm text-slate-400">Departments</p>
            <p className="mt-2 text-3xl font-bold">4</p>
          </div>
        </section>

        <section className="mb-6 rounded-xl border border-slate-800 bg-slate-900 p-5">
          <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
            <label className="flex cursor-pointer items-center gap-2 rounded-lg bg-blue-600 px-4 py-3 font-medium hover:bg-blue-700">
              <Upload className="h-4 w-4" />
              Upload Document
              <input type="file" className="hidden" />
            </label>

            <div className="flex flex-1 gap-3 md:max-w-xl">
              <div className="relative flex-1">
                <Search className="absolute left-3 top-3.5 h-4 w-4 text-slate-400" />
                <input
                  value={search}
                  onChange={(e) => setSearch(e.target.value)}
                  placeholder="Search documents..."
                  className="w-full rounded-lg bg-slate-800 py-3 pl-10 pr-4 outline-none"
                />
              </div>

              <select
                value={department}
                onChange={(e) => setDepartment(e.target.value)}
                className="rounded-lg bg-slate-800 px-4 py-3 outline-none"
              >
                <option>All</option>
                <option>HR</option>
                <option>Payroll</option>
                <option>Engineering</option>
                <option>Support</option>
              </select>
            </div>
          </div>
        </section>

        <section className="rounded-xl border border-slate-800 bg-slate-900">
          <div className="border-b border-slate-800 p-5">
            <h2 className="text-xl font-semibold">Documents</h2>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-left text-sm">
              <thead className="bg-slate-800 text-slate-300">
                <tr>
                  <th className="p-4">Document</th>
                  <th className="p-4">Department</th>
                  <th className="p-4">Status</th>
                  <th className="p-4">Version</th>
                  <th className="p-4">Tags</th>
                  <th className="p-4">Uploaded By</th>
                  <th className="p-4">Actions</th>
                </tr>
              </thead>

              <tbody>
                {filteredDocuments.map((doc) => (
                  <tr key={doc.id} className="border-t border-slate-800">
                    <td className="p-4">
                      <div className="flex items-center gap-3">
                        <FileText className="h-5 w-5 text-blue-400" />
                        <div>
                          <p className="font-medium">{doc.name}</p>
                          <p className="text-xs text-slate-500">{doc.type}</p>
                        </div>
                      </div>
                    </td>

                    <td className="p-4">{doc.department}</td>

                    <td className="p-4">
                      <span
                        className={
                          doc.status === "Approved"
                            ? "rounded-full bg-green-500/20 px-3 py-1 text-xs text-green-300"
                            : "rounded-full bg-yellow-500/20 px-3 py-1 text-xs text-yellow-300"
                        }
                      >
                        {doc.status}
                      </span>
                    </td>

                    <td className="p-4">{doc.version}</td>

                    <td className="p-4">
                      <div className="flex gap-2">
                        {doc.tags.map((tag) => (
                          <span
                            key={tag}
                            className="rounded bg-slate-800 px-2 py-1 text-xs text-slate-300"
                          >
                            {tag}
                          </span>
                        ))}
                      </div>
                    </td>

                    <td className="p-4">{doc.uploadedBy}</td>

                    <td className="p-4">
                      <div className="flex gap-2">
                        {doc.status === "Pending" && (
                          <button
                            onClick={() => approveDocument(doc.id)}
                            className="rounded bg-green-600 px-3 py-1 text-xs"
                          >
                            Approve
                          </button>
                        )}

                        <button className="rounded bg-slate-800 p-2">
                          <Eye className="h-4 w-4" />
                        </button>

                        <button className="rounded bg-slate-800 p-2">
                          <Download className="h-4 w-4" />
                        </button>

                        <button
                          onClick={() => deleteDocument(doc.id)}
                          className="rounded bg-red-600 p-2"
                        >
                          <Trash2 className="h-4 w-4" />
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>

        <section className="mt-6 grid gap-6 lg:grid-cols-2">
          <div className="rounded-xl border border-slate-800 bg-slate-900 p-5">
            <h2 className="text-xl font-semibold">Approval Queue</h2>
            <p className="mt-2 text-slate-400">
              Pending documents waiting for admin review.
            </p>

            <div className="mt-4 space-y-3">
              {documents
                .filter((doc) => doc.status === "Pending")
                .map((doc) => (
                  <div
                    key={doc.id}
                    className="flex items-center justify-between rounded-lg bg-slate-800 p-4"
                  >
                    <div>
                      <p className="font-medium">{doc.name}</p>
                      <p className="text-sm text-slate-400">
                        Uploaded by {doc.uploadedBy}
                      </p>
                    </div>

                    <button
                      onClick={() => approveDocument(doc.id)}
                      className="rounded bg-green-600 px-3 py-2 text-sm"
                    >
                      Approve
                    </button>
                  </div>
                ))}
            </div>
          </div>

          <div className="rounded-xl border border-slate-800 bg-slate-900 p-5">
            <h2 className="text-xl font-semibold">Version History</h2>
            <p className="mt-2 text-slate-400">
              Track document versions and restore previous versions.
            </p>

            <div className="mt-4 space-y-3 text-sm text-slate-300">
              <p>HR Policy.pdf — v1 → v2</p>
              <p>Payroll Guide.docx — v1</p>
              <p>Security Handbook.md — v3</p>
            </div>
          </div>
        </section>
      </div>
    </main>
  )
}