<template>
  <div class="container">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title velos-title">Log in</h1>
    
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Email</label>
            <div class="control">
              <input type="email" name="email" class="input velos-input" v-model="username" />
            </div>
          </div>

          <div class="field">
            <label>Password</label>
            <div class="control">
              <input type="password" name="password" class="input velos-input" v-model="password" />
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" :key="error">{{ error }}</p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button velos-button">Submit</button>
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

      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem('token')

      const formData = {
        username: this.username,
        password: this.password
      }

      await axios
        .post('/api/v1/token/login/', formData)
        .then(response => {
          const token = response.data.auth_token

          this.$store.commit('setToken', token)

          axios.defaults.headers.common['Authorization'] = 'Token ' + token

          localStorage.setItem('token', token)
        })
        .catch(error => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`)
            }
          } else if (error.message) {
            this.errors.push('Something went wrong. Please try again!')
          }
        })

      await axios
        .get('/api/v1/users/me')
        .then(response => {
          this.$store.commit('setUser', { id: response.data.id, username: response.data.username })

          localStorage.setItem('username', response.data.username)
          localStorage.setItem('userid', response.data.id)
        })
        .catch(error => {
          console.log(error)
        })

      await axios
        .get('/api/v1/teams/get_my_team/')
        .then(response => {
          console.log(response.data)

          this.$store.commit('setTeam', {
            id: response.data.id,
            name: response.data.name,
            plan: response.data.plan.name,
            max_leads: response.data.plan.max_leads,
            max_clients: response.data.plan.max_clients
          })

          this.$router.push('/dashboard/my-account')
        })
        .catch(error => {
          console.log(error)
        })

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
