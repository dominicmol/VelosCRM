import { createStore } from 'vuex'

export default createStore({
  // centrale state van de applicatie
  state: {
    isLoading: false,          // geeft aan of er een API-call bezig is
    isAuthenticated: false,    // of de gebruiker is ingelogd
    token: '',                 // JWT-token voor verzoeken
    user: {                    // info over de ingelogde gebruiker
      id: 0,
      username: ''
    },
    team: {                    // info over het huidige team
      id: 0,
      name: ''
    }
  },

  // synchronistische mutaties om state te wijzigen
  mutations: {
    // bij het opstarten van de app: haal auth-data uit localStorage
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.user.username = localStorage.getItem('username') || ''
        state.user.id = parseInt(localStorage.getItem('userid')) || 0
        state.team.name = localStorage.getItem('team_name') || ''
        state.team.id = parseInt(localStorage.getItem('team_id')) || 0
      } else {
        // geen data → terug naar lege defaults
        state.token = ''
        state.isAuthenticated = false
        state.user = { id: 0, username: '' }
        state.team = { id: 0, name: '' }
      }
    },

    // togglet de globale loading-indicator
    setIsLoading(state, status) {
      state.isLoading = status
    },

    // slaat een nieuw token op en markeert als ingelogd
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },

    // verwijdert het token en zet auth-flag uit
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    },

    // zet gebruikersgegevens in de store en localStorage
    setUser(state, user) {
      state.user = user
      localStorage.setItem('username', user.username)
      localStorage.setItem('userid', user.id)
    },

    // slaat teamgegevens op en bewaard ze voor herlaad
    setTeam(state, team) {
      state.team = {
        id: team.id,
        name: team.name
      }
      localStorage.setItem('team_id', team.id)
      localStorage.setItem('team_name', team.name)
    }
  },

  // (nog lege) acties voor asynchrone logica
  actions: {},

  // (nog lege) modules voor opsplitsing van de store
  modules: {}
})
