import { createApp } from 'vue'
import App from './App.vue'
import { plugin, defaultConfig } from '@formkit/vue'
import '@formkit/themes/genesis'
import FirstPage from './views/FirstPage.vue'
import ChronicDisease from './components/ChronicDisease.vue'

const app = createApp(App).use(plugin, defaultConfig);
app.component('first-page', FirstPage);
app.component('chronic-disease', ChronicDisease);

app.mount("#app");
