import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

import DashboardView from '@/views/Dashboard/DashboardView.vue'
import LoginView from '@/views/LoginView.vue'
import LandingPageView from '@/views/LandingPageView.vue'
import FeaturesView from '@/views/FeaturesView.vue'
import TeamView from '@/views/TeamView.vue'
import ContactView from '@/views/ContactView.vue'
import LogoutView from '@/views/LogoutView.vue'
import RegisterView from '@/views/RegisterView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'LandingPage',
      component: LandingPageView,
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: DashboardView,
    },
    {
      path: '/features',
      name: 'FeaturesPage',
      component: FeaturesView,
    },
    {
      path: '/team',
      name: 'TeamPage',
      component: TeamView
    },
    {
      path: '/contact',
      name: 'ContactPage',
      component: ContactView
    },
    {
      path: '/login',
      name: 'LoginPage',
      component: LoginView
    },
    {
      path: '/register',
      name: 'RegisterPage',
      component: RegisterView
    },
    {
      path: '/logout',
      name: 'Logout',
      component: LogoutView
    }
  ],
})

router.beforeEach(async (to) => {
  const publicPages = ['/', '/login', '/register', '/features', '/team', '/logout', '/register']
  const authRequired = !publicPages.includes(to.path)
  const auth = useAuthStore()

  if (authRequired && !auth.isAuthenticated) {
    return '/login'
  }
})

export default router
