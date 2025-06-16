<template>
  <div class="container">
    <div class="columns is-multiline">
      <!-- paginatitel -->
      <div class="column is-12">
        <h1 class="title">Add team</h1>
      </div>

      <!-- formulier om een nieuw team aan te maken -->
      <div class="column is-12">
        <form @submit.prevent="submitForm">
          <!-- veld voor teamnaam -->
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

          <!-- verzendknop -->
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
import axios from 'axios'           // HTTP-client om API-aanroepen te doen
import { toast } from 'bulma-toast' // voor visuele meldingen

export default {
  name: 'AddTeam',                  // component-naam
  data() {
    return {
      name: ''                      // invoer voor de nieuwe teamnaam
    }
  },
  methods: {
    // wordt aangeroepen bij verzenden van het formulier
    async submitForm() {
      this.$store.commit('setIsLoading', true)  // toon globale loader

      const payload = { name: this.name }       // bouw payload voor de API

      try {
        // verstuur POST-verzoek om nieuw team te maken
        const response = await axios.post('/teams/', payload)

        // toon succesmelding
        toast({
          message: 'The team was added',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right'
        })

        // sla nieuw team op in Vuex-store
        this.$store.commit('setTeam', {
          id: response.data.id,
          name: response.data.name
        })

        // navigeer naar dashboard
        this.$router.push('/dashboard')
      } catch (error) {
        console.error('Error adding team:', error.response?.data || error)
        // bouw foutmelding
        let errorMessage = 'Error adding team.'
        if (error.response?.data) {
          for (const field in error.response.data) {
            const msg = error.response.data[field]
            errorMessage += ` ${field}: ${Array.isArray(msg) ? msg.join(' ') : msg}`
          }
        }
        // toon foutmelding
        toast({
          message: errorMessage,
          type: 'is-danger',
          dismissible: true,
          pauseOnHover: true,
          duration: 3000,
          position: 'bottom-right'
        })
      } finally {
        // verberg globale loader
        this.$store.commit('setIsLoading', false)
      }
    }
  }
}
</script>

<style scoped>
/* stijl voor de Submit-knop */
.button.velos-button {
  background-color: #a41917;
  color: white;
  font-weight: bold;
  border-radius: 6px;
  border: none;
  transition: background-color 0.3s ease;
}
/* hover-effect voor knop */
.button.velos-button:hover {
  background-color: #841614;
}
</style>
