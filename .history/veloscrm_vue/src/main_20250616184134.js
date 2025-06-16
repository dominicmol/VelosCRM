import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

// hostname uit de browser
const host = window.location.hostname

const isLocal = host === 'localhost' || host === '127.0.0.1'

// baseURL instellen
axios.defaults.baseURL = isLocal
  ? 'http://127.0.0.1:8000/api/v1'                                // lokaal
  : 'https://dominicmol.pythonanywhere.com/api/v1'                // productie

const app = createApp(App)
app.use(store)
app.use(router)
app.mount('#app')