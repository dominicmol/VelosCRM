<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Add note</h1>
      </div>

      <div class="column is-12">
        <form @submit.prevent="submitForm">
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
  name: 'AddNote',
  data() {
    return {
      name: '',
      body: ''
    }
  },
  methods: {
    async submitForm() {
      this.$store.commit('setIsLoading', true)

      // payload met client_id zoals je backend verwacht
      const note = {
        name: this.name,
        body: this.body,
        client_id: this.$route.params.id
      }

      try {
        // baseURL is al '/api/v1', dus hier volstaat alleen '/notes/'
        await axios.post('/notes/', note)

        toast({
          message: 'The note was added',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right'
        })

        // terug naar de client-detailpagina
        this.$router.push({
          name: 'Client',
          params: { id: this.$route.params.id }
        })
      } catch (error) {
        console.error('Error adding note:', error.response?.data || error)
        let errorMessage = 'Error adding note.'
        if (error.response?.data) {
          // verzamelt veldfouten
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
