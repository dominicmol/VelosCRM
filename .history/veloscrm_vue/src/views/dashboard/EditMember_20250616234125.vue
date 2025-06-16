<template>
  <div class="container">
    <div class="columns is-multiline">
      <!-- paginatitel voor bewerken van teamlid -->
      <div class="column is-12">
        <h1 class="title">Edit member</h1>
      </div>

      <!-- formulier om voornaam en achternaam bij te werken -->
      <div class="column is-12">
        <form @submit.prevent="submitForm">
          <!-- veld voor voornaam -->
          <div class="field">
            <label>First name</label>
            <div class="control">
              <input type="text" class="input" v-model="user.first_name" />
            </div>
          </div>

          <!-- veld voor achternaam -->
          <div class="field">
            <label>Last name</label>
            <div class="control">
              <input type="text" class="input" v-model="user.last_name" />
            </div>
          </div>

          <!-- knop om wijzigingen op te slaan, rechts uitgelijnd -->
          <div class="field is-grouped is-grouped-right">
            <div class="control">
              <button type="submit" class="button velos-button">
                Update
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'           // HTTP-client voor API-aanroepen
import { toast } from 'bulma-toast' // korte pop-upmeldingen

export default {
  name: 'EditMember',               // component-naam
  data() {
    return {
      user: {}                      // sla gebruikersgegevens op
    }
  },
  async mounted() {
    // laad ledeninformatie zodra component is geladen
    this.$store.commit('setIsLoading', true)
    await this.getUser()
    this.$store.commit('setIsLoading', false)
  },
  methods: {
    // haalt de gegevens van het teamlid op
    async getUser() {
      try {
        const userID = this.$route.params.id
        const { data } = await axios.get(`/teams/member/${userID}/`)
        this.user = data
      } catch (error) {
        console.error('Fout bij ophalen member:', error.response?.data || error)
        toast({
          message: 'Kon member niet laden',
          type: 'is-danger',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right',
        })
      }
    },
    // verstuurt bijgewerkte naamgegevens naar de server
    async submitForm() {
      this.$store.commit('setIsLoading', true)
      try {
        const userID = this.$route.params.id
        await axios.put(`/teams/member/${userID}/`, {
          first_name: this.user.first_name,
          last_name: this.user.last_name
        })
        toast({
          message: 'De member is geüpdatet',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right',
        })
        // terug naar eigen accountpagina na update
        this.$router.push({ name: 'MyAccount' })
      } catch (error) {
        console.error('Update mislukt:', error.response?.data || error)
        toast({
          message: 'Update mislukt',
          type: 'is-danger',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right',
        })
      } finally {
        this.$store.commit('setIsLoading', false)
      }
    }
  }
}
</script>

<style scoped>
/* ruimte tussen velden */
.field {
  margin-bottom: 1.25rem;
}

/* stijl voor de Update-knop */
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
