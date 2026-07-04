import axios from "axios"

export const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  timeout: 15000,
  headers: {
    "Content-Type": "application/json",
  },
})

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("access_token")

    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }

    return config
  },
  (error) => Promise.reject(error)
)

api.interceptors.response.use(
  (response) => response,

  async (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem("access_token")

      if (window.location.pathname !== "/login") {
        window.location.href = "/login"
      }
    }

    return Promise.reject(error)
  }
)