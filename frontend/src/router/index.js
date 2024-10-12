import { createRouter, createWebHistory } from 'vue-router' // Ensure both are imported

import UserDashView from '../views/userDashView.vue'
import landingView from '../views/landingView.vue'
import genreView from '../views/genreView.vue'
import gameView from '../views/gameView.vue'
import adminPage from '../views/adminPage.vue'
import notFoundPage from '../views/notFoundPage.vue'

const routes = [
  { path: '/', component: landingView },
  { path: '/user/dashboard', component: UserDashView },
  { path: '/genre', component: genreView },
  { path: '/games', component: gameView },
  { path: '/admin', component: adminPage },
  { path: '/*', component: notFoundPage }
  //  path at last
]

const router = createRouter({
  history: createWebHistory(), // Use createWebHistory here
  routes,
})

export default router
