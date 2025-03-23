import { createRouter, createWebHistory } from 'vue-router'
import userDash from '../views/userDash.vue'
import landingView from '../views/landingView.vue'
import genreView from '../views/genreView.vue'
import gameView from '../views/gameView.vue'
import adminDash from '../views/adminDash.vue'
import pageNotFound from '../views/pageNotFound.vue'
import gamePageView from '../views/gamePageView.vue'
import allGamesView from '../views/allGamesView.vue'
import adminAllGamesView from '../views/adminAllGamesView.vue'
import adminManageUsers from '../views/adminManageUsers.vue'

const routes = [
  { path: '/', name: 'landingView', component: landingView }, // working
  { path: '/user-dashboard', name: 'userDash', component: userDash },
  { path: '/games', name: 'allGamesView', component: allGamesView },
  { path: '/admin/genre', name: 'genreView', component: genreView },
  { path: '/admin/games', name: 'gameView', component: gameView },
  { path: '/admin-dashboard', name: 'adminDash', component: adminDash },
  { path:'/admin/users', name:'adminManageUsers', component: adminManageUsers},
  {
    path: '/admin/allgames',
    name: 'adminAllGamesView',
    component: adminAllGamesView,
  },
  { path: '/game/:gameid', name: 'gamePageView', component: gamePageView },
  {
    path: '/admin/allgames',
    name: 'adminAllGamesView',
    component: adminAllGamesView,
  },
  { path: '/page-not-found', name: 'pageNotFound', component: pageNotFound },
  { path: '/:pathMatch(.*)*', component: pageNotFound },
]

const router = createRouter({
  history: createWebHistory(), // Use createWebHistory
  routes,
})

export default router
