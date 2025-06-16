<template>
  <div class="container">
    <div class="columns is-multiline">
      <!-- titel met naam van de te bewerken client -->
      <div class="column is-12">
        <h1 class="title">Edit {{ client.name }}</h1>
      </div>

      <!-- formulier om clientgegevens te bewerken -->
      <div class="column is-12">
        <form @submit.prevent="submitForm">
          <!-- veld voor naam -->
          <div class="field">
            <label>Name</label>
            <div class="control">
              <input type="text" class="input" v-model="client.name" />
            </div>
          </div>

          <!-- veld voor contactpersoon -->
          <div class="field">
            <label>Contact person</label>
            <div class="control">
              <input type="text" class="input" v-model="client.contact_person" />
            </div>
          </div>

          <!-- veld voor e-mailadres -->
          <div class="field">
            <label>Email</label>
            <div class="control">
              <input type="email" class="input" v-model="client.email" />
            </div>
          </div>

          <!-- veld voor telefoonnummer -->
          <div class="field">
            <label>Phone</label>
            <div class="control">
              <input type="text" class="input" v-model="client.phone" />
            </div>
          </div>

          <!-- veld voor website-URL -->
          <div class="field">
            <label>Website</label>
            <div class="control">
              <input type="text" class="input" v-model="client.website" />
            </div>
          </div>

          <!-- knop om wijzigingen op te slaan -->
          <div class="field is-grouped is-grouped-right">
            <div class="control">
              <button type="submit" class="button velos-button">Update</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'           // HTTP-client voor API-aanroepen
import { toast } from 'bulma-toast' // korte meldingen onderin scherm

export default {
  name: 'EditClient',               // component-naam
  data() {
    return {
      client: {}                    // houdt clientgegevens vast
    }
  },
  async mounted() {
    // laad clientgegevens bij het inladen van de pagina
    this.$store.commit('setIsLoading', true)
    try {
      const clientID = this.$route.params.id
      const { data } = await axios.get(`/api/v1/clients/${clientID}/`)
      this.client = data
    } catch (error) {
      console.error('Kon client niet ophalen:', error.response?.data || error)
      toast({
        message: 'Kon client niet laden',
        type: 'is-danger',
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: 'bottom-right',
      })
    } finally {
      this.$store.commit('setIsLoading', false)
    }
  },
  methods: {
    // sla wijzigingen op via PATCH en toon resultaatmelding
    async submitForm() {
      this.$store.commit('setIsLoading', true)
      const clientID = this.$route.params.id
      const payload = {
        name:           this.client.name,
        contact_person: this.client.contact_person,
        email:          this.client.email,
        phone:          this.client.phone,
        website:        this.client.website,
      }

      try {
        await axios.patch(`/api/v1/clients/${clientID}/`, payload)
        toast({
          message: 'De client is geüpdatet',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right',
        })
        this.$router.push({ name: 'Client', params: { id: clientID } })
      } catch (error) {
        console.error('Update failed:', error.response?.data || error)
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
.field {
  margin-bottom: 1.25rem; /* ruimte tussen formuliervelden */
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
