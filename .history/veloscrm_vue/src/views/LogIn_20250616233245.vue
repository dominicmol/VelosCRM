<template>
  <div class="container">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <!-- paginatitel -->
        <h1 class="title velos-title">Log in</h1>

        <!-- inlogformulier -->
        <form @submit.prevent="submitForm">
          <!-- gebruikersnaamveld -->
          <div class="field">
            <label>Username</label>
            <div class="control">
              <input
                type="text"
                class="input velos-input"
                v-model="username"
                required
              />
            </div>
          </div>

          <!-- wachtwoordveld -->
          <div class="field">
            <label>Password</label>
            <div class="control">
              <input
                type="password"
                class="input velos-input"
                v-model="password"
                required
              />
            </div>
          </div>

          <!-- foutmeldingen tonen als er errors zijn -->
          <div class="notification is-danger" v-if="errors.length">
            <p v-for="(error, index) in errors" :key="index">{{ error }}</p>
          </div>

          <!-- verzendknop -->
          <div class="field">
            <div class="control">
              <button class="button velos-button" type="submit">
                Log in
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'  // HTTP-client voor API-aanroepen

export default {
  name: 'LogIn',            // component-naam
  data() {
    return {
      username: '',         // gebruikersnaam invoer
      password: '',         // wachtwoord invoer
      errors: []            // array voor eventuele foutmeldingen
    }
  },
  methods: {
    // wordt aangeroepen bij formulierverzending
    async submitForm() {
      this.$store.commit('setIsLoading', true)  // toon loading-indicator
      this.errors = []
      localStorage.clear()                       // oude data verwijderen
      axios.defaults.headers.common['Authorization'] = ''

      const formData = {                         // credentials-payload
        username: this.username,
        password: this.password
      }

      try {
        // stap 1: vraag token op
        const loginRes = await axios.post('/auth/token/login/', formData)
        const token = loginRes.data.auth_token

        // stap 2: sla token op in store en localStorage
        this.$store.commit('setToken', token)
        axios.defaults.headers.common['Authorization'] = `Token ${token}`
        localStorage.setItem('token', token)

        // stap 3: haal gebruikersinfo op
        const userRes = await axios.get('/auth/users/me/')
        const user = {
          id: userRes.data.id,
          username: userRes.data.username
        }
        this.$store.commit('setUser', user)

        // stap 4: haal team-gegevens op
        const teamRes = await axios.get('/teams/get_my_team/')
        this.$store.commit('setTeam', {
          id: teamRes.data.id,
          name: teamRes.data.name
        })

        // navigeer naar accountpagina
        this.$router.push('/dashboard/my-account')
      } catch (error) {
        // verwerk en verzamel foutmeldingen
        if (error.response?.data) {
          for (const key in error.response.data) {
            this.errors.push(`${key}: ${error.response.data[key]}`)
          }
        } else {
          this.errors.push('Login failed. Please try again.')
        }
      }

      this.$store.commit('setIsLoading', false)  // verberg loading-indicator
    }
  }
}
</script>

<style scoped>
/* rode titelstijl */
.velos-title {
  color: #a41917;
}

/* input met custom randkleur */
.velos-input {
  border-color: #a41917;
}

/* focus-effect voor input */
.velos-input:focus {
  box-shadow: 0 0 0 0.125em rgba(164, 25, 23, 0.3);
  border-color: #a41917;
}

/* login-button stijl en hover-effect */
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
