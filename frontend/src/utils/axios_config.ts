import axios from 'axios'
import { useAuthStore } from '@/stores/auth'

const api = axios.create({
    baseURL: 'http://localhost:8000/api/',
    headers: {
        'Accept': 'application/json;version=1.0'
    }
})

api.interceptors.request.use(async (config) => {
    const authStore = useAuthStore()

    if (authStore.token) {
        config.headers.Authorization = `Bearer ${authStore.token}`
    }

    return config
})

api.interceptors.response.use(
    (response) => response,
    async (error) => {
        const authStore = useAuthStore()

        if (error.response && error.response.status === 401) {
            try {
                await authStore.refreshToken()
                error.config.headers["Authorization"] = `Bearer ${authStore.token}`
                return api.request(error.config)
            } catch (refreshError) {
                authStore.logout()
                return Promise.reject(refreshError)
            }
        }

        return Promise.reject(error)
    }
)

export default api;