import { createRouter, createWebHistory } from 'vue-router';
import FirstPage from '../views/FirstPage.vue';
import NotFound from '../views/NotFound.vue';

const routes = [
  {
    path: '/',
    name: 'firstPage',
    component: FirstPage,
  },
  {
    path: '/secondpage',
    name: 'secondPage',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '@/views/SecondPage.vue'),
  },
  { //404 error - invalid sites
    path: '/:catchAll(.*)',
    component: NotFound,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
