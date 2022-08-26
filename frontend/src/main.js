import { createApp } from 'vue'
import App from './App.vue'
import { plugin, defaultConfig } from '@formkit/vue'
import '@formkit/themes/genesis'
import FirstPage from './components/FirstPage.vue'

const app = createApp(App).use(plugin, defaultConfig);

app.component('first-page', FirstPage);

app.mount("#app");
