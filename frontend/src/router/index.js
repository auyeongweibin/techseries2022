import { createRouter, createWebHistory } from 'vue-router'
import FirstPage from '../views/FirstPage.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'firstpage',
            component: FirstPage
        },
        {
            path: '/secondpage',
            name: 'secondpage',
            component: () => import('../views/SecondPage.vue')
        }
    ]
})

export default router