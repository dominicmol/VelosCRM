<template>
  <div class="container">
    <div class="columns is-multiline">
      <!-- paginatitel -->
      <div class="column is-12">
        <h1 class="title">Add note</h1>
      </div>

      <!-- formulier voor het toevoegen van een nieuwe notitie -->
      <div class="column is-12">
        <form @submit.prevent="submitForm">
          <!-- titelveld van de notitie -->
          <div class="field">
            <label>Title</label>
            <div class="control">
              <input
                type="text"
                class="input"
                v-model="name"
                placeholder="Note title"
                required
              />
            </div>
          </div>

          <!-- tekstveld voor de inhoud van de notitie -->
          <div class="field">
            <label>Body</label>
            <div class="control">
              <textarea
                class="textarea"
                v-model="body"
                placeholder="Write your note here..."
                required
              ></textarea>
            </div>
          </div>

          <!-- verzendknop voor het formulier -->
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
import axios from 'axios'             // HTTP-client voor API-aanvragen
import { toast } from 'bulma-toast'   // voor visuele meldingen (toasts)

export default {
  name: 'AddNote',                    // component-naam
  data() {
    return {
      name: '',                       // titel van de nieuwe notitie
      body: ''                        // inhoud van de nieuwe notitie
    }
  },
  methods: {
    // wordt aangeroepen bij formulierverzending
    async submitForm() {
      this.$store.commit('setIsLoading', true)  // toon globale loader

      // bouw note-object, inclusief client-ID uit de route-parameters
      const note = {
        name: this.name,
        body: this.body,
        client_id: this.$route.params.id
      }

      try {
        // verstuur POST-verzoek naar /notes/ endpoint
        await axios.post('/notes/', note)

        // succesmelding tonen
        toast({
          message: 'The note was added',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right'
        })

        // navigeer terug naar de client-detailpagina
        this.$router.push({
          name: 'Client',
          params: { id: this.$route.params.id }
        })
      } catch (error) {
        console.error('Error adding note:', error.response?.data || error)
        // zet foutmelding samen, inclusief veld-specifieke messages
        let errorMessage = 'Error adding note.'
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
  background-color: #a41917; /* Velos-rood */
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
