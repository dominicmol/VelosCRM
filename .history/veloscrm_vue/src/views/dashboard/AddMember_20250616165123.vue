<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Add member</h1>
      </div>

      <div class="column is-12">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Email</label>
            <div class="control">
              <input
                type="email"
                class="input"
                v-model="username"
                placeholder="example@velos.nl"
                required
              />
            </div>
          </div>

          <div class="field">
            <label>Password</label>
            <div class="control">
              <input
                type="password"
                class="input"
                v-model="password1"
                placeholder="Enter password"
                required
              />
            </div>
          </div>

          <div class="field">
            <label>Repeat password</label>
            <div class="control">
              <input
                type="password"
                class="input"
                v-model="password2"
                placeholder="Repeat password"
                required
              />
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="(error, i) in errors" :key="i">{{ error }}</p>
          </div>

          <div class="field">
            <div class="control">
              <button type="submit" class="button velos-button">
                Submit
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
  name: 'AddMember',
  data() {
    return {
      username: '',
      password1: '',
      password2: '',
      errors: []
    }
  },
  methods: {
    async submitForm() {
      // reset
      this.errors = []

      // basic validation
      if (!this.username) this.errors.push('Email is required.')
      if (!this.password1) this.errors.push('Password is required.')
      if (this.password1 !== this.password2) this.errors.push('Passwords do not match.')

      if (this.errors.length) return

      this.$store.commit('setIsLoading', true)

      try {
        // 1) Maak eerst de user aan
        await axios.post('/auth/users/', {
          username: this.username,
          password: this.password1
        })

        toast({
          message: 'Member account created',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right'
        })

        // 2) Voeg gebruiker toe aan team
        await axios.post('/teams/add_member/', { email: this.username })

        toast({
          message: 'Member added to team',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right'
        })

        this.$router.push({ name: 'Team' })
      } catch (err) {
        // verzamel alle fouten
        if (err.response?.data) {
          for (const key in err.response.data) {
            const msg = err.response.data[key]
            this.errors.push(Array.isArray(msg) ? msg.join(' ') : msg)
          }
        } else {
          this.errors.push('Something went wrong. Please try again.')
        }
      } finally {
        this.$store.commit('setIsLoading', false)
      }
    }
  }
}
</script>

<style scoped>
.button.velos-button {
  background-color: #a41917;
  color: white;
  font-weight: bold;
  border-radius: 6px;
  border: none;
  transition: background-color 0.3s ease;
}
.button.velos-button:hover {
  background-color: #841614;
}
</style>
