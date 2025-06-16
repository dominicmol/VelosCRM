import { createApp } from 'vue'      // core-functie om een Vue-app te maken
import App from './App.vue'          // root-component van je applicatie
import router from './router'        // router-configuratie voor pagina-navigatie
import store from './store'          // Vuex-store voor globale state
import axios from 'axios'            // HTTP-client voor API-aanroepen

// bepaal of we lokaal draaien aan de hand van hostname
const host = window.location.hostname
const isLocal = host === 'localhost' || host === '127.0.0.1'

// stel de basis-URL voor axios in: lokaal of productie
axios.defaults.baseURL = isLocal
  ? 'http://127.0.0.1:8000/api/v1'              // lokale API-endpoint tijdens ontwikkeling
  : 'https://dominicmol.pythonanywhere.com/api/v1' // productie-API-endpoint

// maak en configureer de Vue-applicatie
const app = createApp(App)
app.use(store)    // registreer Vuex-store
app.use(router)   // registreer Vue Router
app.mount('#app') // mount de app op het DOM-element met id "app"
