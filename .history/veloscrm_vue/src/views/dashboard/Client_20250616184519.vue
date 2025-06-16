<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">{{ client.name }}</h1>
        <div class="buttons">
          <router-link
            :to="{ name: 'EditClient', params: { id: client.id } }"
            class="button is-light"
          >
            Edit
          </router-link>
          <button class="button velos-danger" @click="deleteClient">
            Delete
          </button>
        </div>
      </div>

      <div class="column is-6">
        <div class="box">
          <h2 class="subtitle">Details</h2>
          <p><strong>Created at: </strong>{{ client.created_at }}</p>
          <p><strong>Modified at: </strong>{{ client.modified_at }}</p>
        </div>
      </div>

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

      <div class="column is-12">
        <h2 class="subtitle">Notes</h2>
        <router-link
          :to="{ name: 'AddNote', params: { id: client.id } }"
          class="button velos-red mb-6"
        >
          Add note
        </router-link>

        <div
          v-for="note in notes"
          :key="note.id"
          class="box"
        >
          <h3 class="is-size-4">{{ note.name }}</h3>
          <p>{{ note.body }}</p>
          <router-link
            :to="{ name: 'EditNote', params: { id: client.id, note_id: note.id } }"
            class="button velos-red mt-6"
          >
            Edit note
          </router-link>
        </div>

        <p v-if="!notes.length">No notes yet for this client.</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Client',
  data() {
    return {
      client: {},
      notes: []
    }
  },
  async mounted() {
    this.$store.commit('setIsLoading', true)
    const clientID = this.$route.params.id

    try {
      const { data: clientData } = await axios.get(
        `/clients/${clientID}/`
      )
      this.client = clientData

      const { data: notesData } = await axios.get(
        `/notes/?client_id=${clientID}`
      )

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
      this.$store.commit('setIsLoading', false)
    }
  },
  methods: {
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

.mb-6 {
  margin-bottom: 1.5rem;
}
.mt-6 {
  margin-top: 1.5rem;
}
</style>
