<template>
  <div class="container">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <!-- koptekst voor registratiepagina -->
        <h1 class="title velos-title">Create account</h1>

        <!-- registratieformulier -->
        <form @submit.prevent="submitForm">
          <!-- e-mailveld -->
          <div class="field">
            <label>Email</label>
            <div class="control">
              <input type="email" class="input velos-input" v-model="email" />
            </div>
          </div>

          <!-- wachtwoordveld -->
          <div class="field">
            <label>Password</label>
            <div class="control">
              <input type="password" class="input velos-input" v-model="password" />
            </div>
          </div>

          <!-- herhaal-wachtwoordveld -->
          <div class="field">
            <label>Repeat password</label>
            <div class="control">
              <input type="password" class="input velos-input" v-model="confirmPassword" />
            </div>
          </div>

          <!-- foutmeldingen tonen -->
          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" :key="error">{{ error }}</p>
          </div>

          <!-- verzendknop -->
          <div class="field">
            <div class="control">
              <button class="button velos-button">Sign up</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'                 // voor API-aanroepen
import { toast } from 'bulma-toast'       // meldingen onderaan scherm

export default {
  name: 'SignUp',                         // component-naam
  data() {
    return {
      email: '',                          // e-mail van nieuwe gebruiker
      password: '',                       // gekozen wachtwoord
      confirmPassword: '',                // herhaling van wachtwoord
      errors: []                          // lijst met validatie- of serverfouten
    }
  },
  methods: {
    // functie bij formulierverzending
    async submitForm() {
      this.errors = []

      // basisvalidatie van invoer
      if (!this.email) this.errors.push('Email is required.')
      if (!this.password || this.password.length < 6)
        this.errors.push('Password must be at least 6 characters.')
      if (this.password !== this.confirmPassword)
        this.errors.push('Passwords do not match.')

      if (this.errors.length) return     // stop bij validatiefouten

      this.$store.commit('setIsLoading', true)  // toon loading

      try {
        // maak account via API
        await axios.post('/teams/signup/', {
          username: this.email,
          email: this.email,
          password: this.password
        })

        // succesvolle melding
        toast({
          message: 'Account created. You can now log in.',
          type: 'is-success',
          duration: 2000,
          dismissible: true,
          pauseOnHover: true,
          position: 'bottom-right'
        })

        // navigeer naar inlogpagina
        this.$router.push('/log-in')
      } catch (error) {
        // verwerk serverfouten
        if (error.response?.data) {
          for (const field in error.response.data) {
            const msgs = error.response.data[field]
            if (Array.isArray(msgs)) {
              msgs.forEach(msg => this.errors.push(`${field}: ${msg}`))
            } else {
              this.errors.push(`${field}: ${msgs}`)
            }
          }
        } else {
          this.errors.push('Something went wrong. Please try again.')
        }
      }

      this.$store.commit('setIsLoading', false) // verberg loading
    }
  }
}
</script>

<style scoped>
/* kleur van de titel */
.velos-title {
  color: #a41917;
}

/* randkleur voor inputvelden */
.velos-input {
  border-color: #a41917;
}

/* focus-effect voor inputvelden */
.velos-input:focus {
  box-shadow: 0 0 0 0.125em rgba(164, 25, 23, 0.3);
  border-color: #a41917;
}

/* stijl voor de sign-up knop */
.velos-button {
  background-color: #a41917;
  border-color: transparent;
  color: white;
  font-weight: 600;
  transition: background-color 0.3s ease;
}

/* hover-effect voor de knop */
.velos-button:hover {
  background-color: #821414;
}
</style>
