import { createStore } from 'vuex'

export default createStore({
  state: {
    isLoading: false,
    isAuthenticated: false,
    token: '',
    user: {
      id: 0,
      username: ''
    },
    team: {
      id: 0,
      name: ''
    }
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.user.username = localStorage.getItem('username') || ''
        state.user.id = parseInt(localStorage.getItem('userid')) || 0
        state.team.name = localStorage.getItem('team_name') || ''
        state.team.id = parseInt(localStorage.getItem('team_id')) || 0
      } else {
        state.token = ''
        state.isAuthenticated = false
        state.user = { id: 0, username: '' }
        state.team = { id: 0, name: '' }
      }
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    },
    setUser(state, user) {
      state.user = user
      localStorage.setItem('username', user.username)
      localStorage.setItem('userid', user.id)
    },
    setTeam(state, team) {
      state.team = {
        id: team.id,
        name: team.name
      }
      localStorage.setItem('team_id', team.id)
      localStorage.setItem('team_name', team.name)
    }
  },
  actions: {},
  modules: {}
})