<template>
  <div class="container">
    <div class="columns is-multiline">
      <!-- koptekst en zoekformulier bovenaan -->
      <div class="column is-12">
        <h1 class="title">Clients</h1>
        <!-- knop om nieuwe client toe te voegen -->
        <router-link to="/dashboard/clients/add" class="button velos-red">
          Add client
        </router-link>
        <hr />

        <!-- zoekbalk voor clients -->
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

      <!-- tabel met clients en paginatieknoppen -->
      <div class="column is-12">
        <template v-if="clients.length">
          <!-- lijst van clients -->
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
                  <!-- link naar detailpagina van een client -->
                  <router-link
                    :to="{ name: 'Client', params: { id: client.id } }"
                  >
                    Details
                  </router-link>
                </td>
              </tr>
            </tbody>
          </table>

          <!-- knoppen om door pagina’s te navigeren -->
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

        <!-- boodschap als er geen clients zijn -->
        <template v-else>
          <p>You don't have any clients yet...</p>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'  // HTTP-client voor API-aanroepen

export default {
  name: 'Clients',         // component-naam
  data() {
    return {
      clients: [],              // array voor opgehaalde clients
      showNextButton: false,    // toon “Next” als er meer pagina’s zijn
      showPreviousButton: false,// toon “Previous” als je niet op pagina 1 bent
      currentPage: 1,           // huidige paginanummer
      query: ''                 // zoekterm voor filteren
    }
  },
  mounted() {
    this.getClients()         // haal clients op bij laden van component
  },
  methods: {
    // ga naar de volgende paginapagina
    goToNextPage() {
      this.currentPage++
      this.getClients()
    },
    // ga naar de vorige paginapagina
    goToPreviousPage() {
      this.currentPage--
      this.getClients()
    },
    // haalt de lijst van clients op van de API
    async getClients() {
      this.$store.commit('setIsLoading', true)  // toon loader tijdens ophalen
      this.showNextButton = false
      this.showPreviousButton = false

      try {
        // GET met search- en page-parameters
        const response = await axios.get(
          `/clients/?page=${this.currentPage}&search=${this.query}`
        )
        const { results, next, previous } = response.data
        this.clients = Array.isArray(results) ? results : []
        // bepaal of paginaknoppen zichtbaar moeten zijn
        this.showNextButton = !!next
        this.showPreviousButton = !!previous
      } catch (error) {
        console.error('Fout bij ophalen clients:', error.response?.data || error)
        this.clients = []  // reset bij fout
      } finally {
        this.$store.commit('setIsLoading', false) // verberg loader
      }
    }
  }
}
</script>

<style scoped>
/* stijl voor de rode actieknop */
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
