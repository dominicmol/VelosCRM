<template>
  <div class="container">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title velos-title">Log in</h1>

        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Username</label>
            <div class="control">
              <input type="text" class="input velos-input" v-model="username" required />
            </div>
          </div>

          <div class="field">
            <label>Password</label>
            <div class="control">
              <input type="password" class="input velos-input" v-model="password" required />
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="(error, index) in errors" :key="index">{{ error }}</p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button velos-button" type="submit">Log in</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LogIn',
  data() {
    return {
      username: '',
      password: '',
      errors: []
    }
  },
  methods: {
    async submitForm() {
      this.$store.commit('setIsLoading', true)
      this.errors = []
      localStorage.clear()
      axios.defaults.headers.common['Authorization'] = ''

      const formData = {
        username: this.username,
        password: this.password
      }

      try {
        // let op: hier enkel /auth/... because baseURL al /api/v1 bevat
        const loginRes = await axios.post('/auth/token/login/', formData)
        const token    = loginRes.data.auth_token

        this.$store.commit('setToken', token)
        axios.defaults.headers.common['Authorization'] = `Token ${token}`
        localStorage.setItem('token', token)

        const userRes = await axios.get('/auth/users/me/')
        const user    = {
          id:       userRes.data.id,
          username: userRes.data.username
        }
        this.$store.commit('setUser', user)
        localStorage.setItem('username', user.username)
        localStorage.setItem('userid',   user.id)

        // teams endpoint ook zonder prefix
        const teamRes = await axios.get('/teams/get_my_team/')
        this.$store.commit('setTeam', {
          id:   teamRes.data.id,
          name: teamRes.data.name
        })
        localStorage.setItem('team_id',   teamRes.data.id)
        localStorage.setItem('team_name', teamRes.data.name)

        this.$router.push('/dashboard/my-account')
      } catch (error) {
        if (error.response?.data) {
          for (const key in error.response.data) {
            this.errors.push(`${key}: ${error.response.data[key]}`)
          }
        } else {
          this.errors.push('Login failed. Please try again.')
        }
      }

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

<style scoped>
.velos-title {
  color: #a41917;
}

.velos-input {
  border-color: #a41917;
}

.velos-input:focus {
  box-shadow: 0 0 0 0.125em rgba(164, 25, 23, 0.3);
  border-color: #a41917;
}

.velos-button {
  background-color: #a41917;
  border-color: transparent;
  color: white;
  font-weight: 600;
  transition: background-color 0.3s ease;
}

.velos-button:hover {
  background-color: #821414;
  color: white;
}
</style>