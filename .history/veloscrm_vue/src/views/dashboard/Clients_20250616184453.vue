<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Clients</h1>

        <router-link to="/dashboard/clients/add" class="button velos-red">Add client</router-link>

        <hr />

        <form @submit.prevent="getClients">
          <div class="field has-addons">
            <div class="control">
              <input
                type="text"
                class="input"
                v-model="query"
                placeholder="Search clients..."
              />
            </div>
            <div class="control">
              <button class="button velos-red">Search</button>
            </div>
          </div>
        </form>
      </div>

      <div class="column is-12">
        <template v-if="clients.length">
          <table class="table is-fullwidth">
            <thead>
              <tr>
                <th>Name</th>
                <th>Contact person</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="client in clients" :key="client.id">
                <td>{{ client.name }}</td>
                <td>{{ client.contact_person }}</td>
                <td>
                  <router-link :to="{ name: 'Client', params: { id: client.id } }">
                    Details
                  </router-link>
                </td>
              </tr>
            </tbody>
          </table>

          <div class="buttons">
            <button
              class="button is-light"
              @click="goToPreviousPage"
              v-if="showPreviousButton"
            >
              Previous
            </button>
            <button
              class="button is-light"
              @click="goToNextPage"
              v-if="showNextButton"
            >
              Next
            </button>
          </div>
        </template>

        <template v-else>
          <p>You don't have any clients yet...</p>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Clients',
  data() {
    return {
      clients: [],            
      showNextButton: false,
      showPreviousButton: false,
      currentPage: 1,
      query: ''
    }
  },
  mounted() {
    this.getClients()
  },
  methods: {
    goToNextPage() {
      this.currentPage++
      this.getClients()
    },
    goToPreviousPage() {
      this.currentPage--
      this.getClients()
    },
    async getClients() {
      this.$store.commit('setIsLoading', true)
      this.showNextButton = false
      this.showPreviousButton = false

      try {
        const response = await axios.get(
          `/clients/?page=${this.currentPage}&search=${this.query}`
        )
        const { results, next, previous } = response.data
        this.clients = Array.isArray(results) ? results : []
        this.showNextButton = !!next
        this.showPreviousButton = !!previous
      } catch (error) {
        console.error('Fout bij ophalen clients:', error.response?.data || error)
        this.clients = []
      } finally {
        this.$store.commit('setIsLoading', false)
      }
    }
  }
}
</script>

<style scoped>
.button.velos-red {
  background-color: #a41917;
  border-color: #a41917;
  color: #fff;
  font-weight: 600;
  transition: background-color 0.3s ease, border-color 0.3s ease;
}
.button.velos-red:hover {
  background-color: #821414;
  border-color: #821414;
}
</style>
