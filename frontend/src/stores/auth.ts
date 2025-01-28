import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
})

export const useAuthStore = defineStore('auth',{
  state: () => ({
    user: null,
  }),
  actions: {
    async login(email: string, password: string) {
      try {
        const response = await axios.post('http://localhost:8000/api/token/', { email, password });
        if (response.status === 200) {
          const token = response.data.token;
          localStorage.setItem('token', token);
          return token;
        }
      } catch (error) {
        console.log(error);
      }
    },
    async register(email: string, password: string) {
      console.log('register', email, password);
    },
    async logout() {
      try {
       const response = await axios.post('api/token/logout', {})
        if (response.status === 200) {
          localStorage.removeItem('token');
          console.log('logged out');
        }
      } catch (error) {
        console.log(error);
      }
    }
  },
  getters: {
    auth(state) {
      return state.user
    }
  }
})
