<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Add team</h1>
      </div>

      <div class="column is-12">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Team name</label>
            <div class="control">
              <input
                type="text"
                class="input"
                v-model="name"
                placeholder="Enter team name"
                required
              />
            </div>
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
  name: 'AddTeam',
  data() {
    return {
      name: ''
    }
  },
  methods: {
    async submitForm() {
      this.$store.commit('setIsLoading', true)

      const payload = { name: this.name }

      try {
        const response = await axios.post('/teams/', payload)

        toast({
          message: 'The team was added',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right'
        })

        this.$store.commit('setTeam', {
          id: response.data.id,
          name: response.data.name
        })

        this.$router.push('/dashboard')
      } catch (error) {
        console.error('Error adding team:', error.response?.data || error)
        let errorMessage = 'Error adding team.'
        if (error.response?.data) {
          for (const field in error.response.data) {
            const msg = error.response.data[field]
            errorMessage += ` ${field}: ${Array.isArray(msg) ? msg.join(' ') : msg}`
          }
        }
        toast({
          message: errorMessage,
          type: 'is-danger',
          dismissible: true,
          pauseOnHover: true,
          duration: 3000,
          position: 'bottom-right'
        })
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
