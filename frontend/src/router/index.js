import { createRouter, createWebHistory } from 'vue-router'
import FirstPage from '../views/FirstPage.vue'

const routes = [
  {
    path: '/',
    name: 'firstpage',
    component: FirstPage
  },
  {
    path: '/secondpage',
    name: 'secondpage',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '@/views/SecondPage.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
