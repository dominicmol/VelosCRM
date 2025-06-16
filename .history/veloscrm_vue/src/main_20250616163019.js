// src/main.js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

// hostname uit de browser
const host = window.location.hostname

// localhost of 127.0.0.1 beschouwen we als "dev", alle andere hosts als productie
const isLocal = host === 'localhost' || host === '127.0.0.1'

// baseURL instellen
axios.defaults.baseURL = isLocal
  ? 'http://127.0.0.1:8000/api/v1'                                // lokaal
  : 'https://dominicmol.pythonanywhere.com'                // productie

const app = createApp(App)
app.use(store)
app.use(router)
app.mount('#app')