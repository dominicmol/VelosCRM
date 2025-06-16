<template>
  <div class="container">
    <div class="columns is-multiline">
      <!-- koptekst met clientnaam en bewerk-/verwijderknoppen -->
      <div class="column is-12">
        <h1 class="title">{{ client.name }}</h1>
        <div class="buttons">
          <!-- link naar bewerkformulier -->
          <router-link
            :to="{ name: 'EditClient', params: { id: client.id } }"
            class="button is-light"
          >
            Edit
          </router-link>
          <!-- knop om client te verwijderen -->
          <button class="button velos-danger" @click="deleteClient">
            Delete
          </button>
        </div>
      </div>

      <!-- sectie met datumgegevens -->
      <div class="column is-6">
        <div class="box">
          <h2 class="subtitle">Details</h2>
          <p><strong>Created at: </strong>{{ client.created_at }}</p>
          <p><strong>Modified at: </strong>{{ client.modified_at }}</p>
        </div>
      </div>

      <!-- sectie met contactinformatie -->
      <div class="column is-6">
        <div class="box">
          <h2 class="subtitle">Contact information</h2>
          <p><strong>Contact person: </strong>{{ client.contact_person }}</p>
          <p><strong>Email: </strong>{{ client.email }}</p>
          <p><strong>Phone: </strong>{{ client.phone }}</p>
          <p><strong>Website: </strong>{{ client.website }}</p>
        </div>
      </div>

      <hr />

      <!-- notities-lijst en knop om nieuwe notitie toe te voegen -->
      <div class="column is-12">
        <h2 class="subtitle">Notes</h2>
        <router-link
          :to="{ name: 'AddNote', params: { id: client.id } }"
          class="button velos-red mb-6"
        >
          Add note
        </router-link>

        <!-- toon elke notitie in een box -->
        <div
          v-for="note in notes"
          :key="note.id"
          class="box"
        >
          <h3 class="is-size-4">{{ note.name }}</h3>
          <p>{{ note.body }}</p>
          <!-- link om notitie te bewerken -->
          <router-link
            :to="{ name: 'EditNote', params: { id: client.id, note_id: note.id } }"
            class="button velos-red mt-6"
          >
            Edit note
          </router-link>
        </div>

        <!-- boodschap als er nog geen notities zijn -->
        <p v-if="!notes.length">No notes yet for this client.</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'  // HTTP-client voor API-aanroepen

export default {
  name: 'Client',
  data() {
    return {
      client: {},  // data voor de huidige client
      notes: []    // array met notities voor deze client
    }
  },
  async mounted() {
    this.$store.commit('setIsLoading', true)  // toon loader tijdens data-ophalen
    const clientID = this.$route.params.id

    try {
      // haal clientgegevens op
      const { data: clientData } = await axios.get(
        `/clients/${clientID}/`
      )
      this.client = clientData

      // haal notities op voor deze client
      const { data: notesData } = await axios.get(
        `/notes/?client_id=${clientID}`
      )
      // note: paginatie kan in notesData.results zitten
      this.notes = Array.isArray(notesData)
        ? notesData
        : Array.isArray(notesData.results)
          ? notesData.results
          : []
    } catch (error) {
      console.error(
        'Error fetching client or notes:',
        error.response?.data || error
      )
      this.notes = []
    } finally {
      this.$store.commit('setIsLoading', false)  // verberg loader
    }
  },
  methods: {
    // verwijdert de huidige client en gaat terug naar de lijst
    async deleteClient() {
      this.$store.commit('setIsLoading', true)
      const clientID = this.$route.params.id

      try {
        await axios.post(`/clients/delete_client/${clientID}/`)
        this.$router.push('/dashboard/clients')
      } catch (error) {
        console.error(
          'Error deleting client:',
          error.response?.data || error
        )
      } finally {
        this.$store.commit('setIsLoading', false)
      }
    }
  }
}
</script>

<style scoped>
/* rode delete-knop */
.button.velos-danger {
  background-color: #a41917;
  color: white;
  border: none;
  font-weight: bold;
  border-radius: 6px;
  transition: background-color 0.3s ease;
}
.button.velos-danger:hover {
  background-color: #841614;
}

/* rode actieknoppen voor notities */
.button.velos-red {
  background-color: #a41917;
  border-color: #a41917;
  color: #fff;
  font-weight: bold;
  border-radius: 6px;
  transition: background-color 0.3s ease;
}
.button.velos-red:hover {
  background-color: #821414;
}

/* marges voor knoppen */
.mb-6 {
  margin-bottom: 1.5rem;
}
.mt-6 {
  margin-top: 1.5rem;
}
</style>
