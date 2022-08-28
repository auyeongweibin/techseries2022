import { createApp } from 'vue'
import App from './App.vue'
import { plugin, defaultConfig } from '@formkit/vue'
import '@formkit/themes/genesis'
import FirstPage from './views/FirstPage.vue'
import SecondPage from './views/SecondPage.vue'
// import ChronicDisease from './components/ChronicDisease.vue'
import router from './router/index.js'

const app = createApp(App).use(router).use(plugin, defaultConfig);
app.component('first-page', FirstPage);
// app.component('chronic-disease', ChronicDisease);
app.component('second-page', SecondPage);
app.mount("#app");
