<template>
  <div class="container">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title velos-title">Create account</h1>

        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Email</label>
            <div class="control">
              <input type="email" class="input velos-input" v-model="email" />
            </div>
          </div>

          <div class="field">
            <label>Password</label>
            <div class="control">
              <input type="password" class="input velos-input" v-model="password" />
            </div>
          </div>

          <div class="field">
            <label>Repeat password</label>
            <div class="control">
              <input type="password" class="input velos-input" v-model="confirmPassword" />
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" :key="error">{{ error }}</p>
          </div>

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
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
  name: 'SignUp',
  data() {
    return {
      email: '',
      password: '',
      confirmPassword: '',
      errors: []
    }
  },
  methods: {
    async submitForm() {
      this.errors = []

      if (!this.email) this.errors.push('Email is required.')
      if (!this.password || this.password.length < 6) this.errors.push('Password must be at least 6 characters.')
      if (this.password !== this.confirmPassword) this.errors.push('Passwords do not match.')

      if (this.errors.length) return

      this.$store.commit('setIsLoading', true)

      try {
        // Let op: hier enkel '/users/' omdat baseURL al '/api/v1' is
        await axios.post('/users/', {
          username: this.email,
          password: this.password
        })

        toast({
          message: 'Account created. You can now log in.',
          type: 'is-success',
          duration: 2000,
          dismissible: true,
          pauseOnHover: true,
          position: 'bottom-right'
        })

        this.$router.push('/log-in')
      } catch (error) {
        if (error.response?.data) {
          for (const field in error.response.data) {
            this.errors.push(`${field}: ${error.response.data[field]}`)
          }
        } else {
          this.errors.push('Something went wrong. Please try again.')
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
}
</style>