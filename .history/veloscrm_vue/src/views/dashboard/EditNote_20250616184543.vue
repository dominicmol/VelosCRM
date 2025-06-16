<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Edit note</h1>
      </div>

      <div class="column is-12">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Name</label>
            <div class="control">
              <input type="text" class="input" v-model="note.name" />
            </div>
          </div>

          <div class="field">
            <label>Body</label>
            <div class="control">
              <textarea class="textarea" v-model="note.body"></textarea>
            </div>
          </div>

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
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
  name: 'EditNote',
  data() {
    return {
      note: {}
    }
  },
  async mounted() {
    this.$store.commit('setIsLoading', true)
    await this.getNote()
    this.$store.commit('setIsLoading', false)
  },
  methods: {
    async getNote() {
      const noteID = this.$route.params.note_id
      const clientID = this.$route.params.id

      try {
        const { data } = await axios.get(
          `/notes/${noteID}/?client_id=${clientID}`
        )
        this.note = data
      } catch (error) {
        console.error('Error fetching note:', error.response?.data || error)
        toast({
          message: 'Fout bij het ophalen van de notitie.',
          type: 'is-danger',
          dismissible: true,
          pauseOnHover: true,
          duration: 3000,
          position: 'bottom-right',
        })
        this.$router.push({ name: 'Client', params: { id: clientID } })
      }
    },
    async submitForm() {
      this.$store.commit('setIsLoading', true)
      const clientID = this.$route.params.id

      try {
        // update note
        await axios.patch(`/notes/${this.note.id}/`, this.note)

        toast({
          message: 'De notitie is bijgewerkt.',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right',
        })
        this.$router.push({ name: 'Client', params: { id: clientID } })
      } catch (error) {
        console.error('Error updating note:', error.response?.data || error)
        let errorMessage = 'Fout bij bijwerken notitie.'
        if (error.response?.data) {
          for (const field in error.response.data) {
            errorMessage += ` ${field}: ${error.response.data[field]}`
          }
        }
        toast({
          message: errorMessage,
          type: 'is-danger',
          dismissible: true,
          pauseOnHover: true,
          duration: 3000,
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
  margin-bottom: 1.25rem;
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
  color: white;
}
</style>
