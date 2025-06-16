<template>
  <div class="container">
    <div class="columns is-multiline">
      <!-- koptekst van de pagina -->
      <div class="column is-12">
        <h1 class="title">Add client</h1>
      </div>

      <!-- formulier voor het toevoegen van een nieuwe client -->
      <div class="column is-12">
        <form @submit.prevent="submitForm">
          <!-- veld voor bedrijfsnaam -->
          <div class="field">
            <label>Name</label>
            <div class="control">
              <input
                type="text"
                class="input"
                v-model="name"
                placeholder="Enter client name"
                required
              />
            </div>
          </div>

          <!-- veld voor contactpersoon -->
          <div class="field">
            <label>Contact person</label>
            <div class="control">
              <input
                type="text"
                class="input"
                v-model="contact_person"
                placeholder="Enter contact person"
              />
            </div>
          </div>

          <!-- veld voor e-mailadres -->
          <div class="field">
            <label>Email</label>
            <div class="control">
              <input
                type="email"
                class="input"
                v-model="email"
                placeholder="example@client.com"
              />
            </div>
          </div>

          <!-- veld voor telefoonnummer -->
          <div class="field">
            <label>Phone</label>
            <div class="control">
              <input
                type="text"
                class="input"
                v-model="phone"
                placeholder="Enter phone number"
              />
            </div>
          </div>

          <!-- optioneel veld voor website-URL -->
          <div class="field">
            <label>Website</label>
            <div class="control">
              <input
                type="text"
                class="input"
                v-model="website"
                placeholder="https://"
              />
            </div>
          </div>

          <!-- submit-knop -->
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
import axios from 'axios'             // HTTP-client om API-aanvragen te doen
import { toast } from 'bulma-toast'   // visuele meldingen onderaan scherm

export default {
  name: 'AddClient',                  // naam van deze component
  data() {
    return {
      name: '',                       // clientnaam
      contact_person: '',             // contactpersoon
      email: '',                      // e-mailadres
      phone: '',                      // telefoonnummer
      website: ''                     // website-URL
    }
  },
  methods: {
    // wordt uitgevoerd als het formulier wordt verzonden
    async submitForm() {
      this.$store.commit('setIsLoading', true)  // toon globale loader

      // bouw payload voor API-call
      const payload = {
        name: this.name,
        contact_person: this.contact_person,
        email: this.email,
        phone: this.phone,
        website: this.website
      }

      try {
        // stuur POST naar /clients/ om nieuwe client aan te maken
        await axios.post('/clients/', payload)

        // succesmelding tonen
        toast({
          message: 'The client was added',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right'
        })

        // ga terug naar lijst met clients
        this.$router.push('/dashboard/clients')
      } catch (err) {
        // foutmelding uit response of error.message
        const msg = err.response?.data
          ? JSON.stringify(err.response.data)
          : err.message

        // toon foutmelding
        toast({
          message: `Error adding client: ${msg}`,
          type: 'is-danger',
          dismissible: true,
          pauseOnHover: true,
          duration: 4000,
          position: 'bottom-right'
        })

        console.error('Add client failed:', err)
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
  color: #fff;
  font-weight: bold;
  border-radius: 6px;
  border: none;
  transition: background-color 0.3s ease;
}

/* hover-effect voor Submit-knop */
.button.velos-button:hover {
  background-color: #841614;
}
</style>
