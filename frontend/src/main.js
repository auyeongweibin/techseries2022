import { createApp } from 'vue'
import App from './App.vue'
import { plugin, defaultConfig } from '@formkit/vue'
import '@formkit/themes/genesis'
import FirstPage from './views/FirstPage.vue'

const app = createApp(App).use(plugin, defaultConfig);

app.component('first-page', FirstPage);

app.mount("#app");
