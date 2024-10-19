import { createRouter, createWebHistory } from 'vue-router'

import UserDashView from '../views/userDashView.vue'
import landingView from '../views/landingView.vue'
import genreView from '../views/genreView.vue'
import gameView from '../views/gameView.vue'
import adminDash from '../views/adminDash.vue'
import pageNotFound from '../views/pageNotFound.vue'

const routes = [
  { path: '/', component: landingView }, // working
  { path: '/user/dashboard', component: UserDashView },
  { path: '/genre', component: genreView },
  { path: '/games', component: gameView },
  { path: '/admin/dashboard', component: adminDash }, // working
  { path: '/page-not-found', component: pageNotFound },
  { path: '/:pathMatch(.*)*', component: pageNotFound },
]

const router = createRouter({
  history: createWebHistory(), // Use createWebHistory
  routes,
})

export default router
