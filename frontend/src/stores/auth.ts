import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router'
import { jwtDecode } from 'jwt-decode'
import api from '@/utils/axios_config'


export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null as any,
    token: localStorage.getItem('token') || null,
    refresh: localStorage.getItem('refresh') || null,
  }),
  actions: {
    async register(email: string, password: string, name: string) {
      try {
        const response = await api.post('/register/',
          {
            email: email,
            password: password,
            name: name
          },
        )

        console.log('User registered properly!')

      } catch (error) {
        console.log('Registration failed: ', error)
      }
    },
    async login(email: string, password: string) {
      try {
        const response = await api.post('/token/',
        {
          email: email,
          password: password
        },
      )

        this.token = response.data.access
        this.refresh = response.data.refresh

        localStorage.setItem('token', this.token!)
        localStorage.setItem('refresh', this.refresh!)

        this.startRefreshToken()

        await this.fetchUser();

      } catch (error) {
        console.log('Login failed: ', error)
        this.user = null;
      }
    },
    async fetchUser() {
      if (!this.token) return;

      try {
        const response = await api.get('/users/')
        this.user = response.data
        console.log(this.user)
        router.push('/dashboard')
      } catch (error) {
        console.log('Failed to fetch user: ', error)
        this.user = null;
      }
    },
    async logout() {
      this.user = null
      this.token = null
      this.refresh = null

      localStorage.removeItem('refresh')
      localStorage.removeItem('token')

      console.log('User logged out')
      router.push('/logout')
    },
    async refreshToken() {
      if (!this.refresh) {
        // this.logout();
        throw new Error('There is no refresh token')
        return;
      }

      try {
        const response = await api.post('/token/refresh/', 
          { 
            refresh: this.refresh
          }
        );

        this.token = response.data.access;
        localStorage.setItem('token', this.token!);
      } catch (error) {
        console.error('Token refresh failed:', error);
        this.logout();
      }
    },
    startRefreshToken() {
      if (!this.token) return

      const tokenExp = jwtDecode<{ exp: number }>(this.token).exp
      const refreshTime = (tokenExp - 60) * 1000 - Date.now()

      if (refreshTime > 0) {
        setTimeout(async () => {
          await this.refreshToken()
          this.startRefreshToken()
        }, refreshTime)
      }
    }
    
  },
  getters: {
    isAuthenticated: (state) => !!state.token
  }
})
