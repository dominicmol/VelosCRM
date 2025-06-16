<template>
  <div class="container">
    <div class="columns is-multiline">
      <!-- header met titel en “Add lead” knop -->
      <div class="column is-12">
        <h1 class="title">Leads</h1>
        <router-link to="/dashboard/leads/add" class="button velos-red mb-4">
          Add lead
        </router-link>
        <hr />
        <!-- zoekformulier om leads te filteren -->
        <form @submit.prevent="getLeads">
          <div class="field has-addons">
            <div class="control">
              <input
                type="text"
                class="input"
                v-model="query"
                placeholder="Search leads..."
              />
            </div>
            <div class="control">
              <button class="button velos-red">Search</button>
            </div>
          </div>
        </form>
      </div>

      <!-- tabel met leads of boodschap als er geen zijn -->
      <div class="column is-12">
        <table class="table is-fullwidth" v-if="leads.length">
          <thead>
            <tr>
              <th>Company</th>
              <th>Contact person</th>
              <th>Assigned to</th>
              <th>Status</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="lead in leads" :key="lead.id">
              <td>{{ lead.company }}</td>
              <td>{{ lead.contact_person }}</td>
              <td>
                <!-- toon toegewezen teamlid als aanwezig -->
                <template v-if="lead.assigned_to">
                  {{ lead.assigned_to.first_name }} {{ lead.assigned_to.last_name }}
                </template>
              </td>
              <td>{{ lead.status }}</td>
              <td>
                <router-link :to="{ name: 'Lead', params: { id: lead.id } }">
                  Details
                </router-link>
              </td>
            </tr>
          </tbody>
        </table>
        <p v-else>You don't have any leads yet...</p>

        <!-- paginatieknoppen -->
        <div class="buttons" v-if="showPreviousButton || showNextButton">
          <button class="button is-light" @click="goToPreviousPage" v-if="showPreviousButton">
            Previous
          </button>
          <button class="button is-light" @click="goToNextPage" v-if="showNextButton">
            Next
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'  // HTTP-client voor API-aanroepen

export default {
  name: 'Leads',           // component-naam
  data() {
    return {
      leads: [],               // array met opgehaalde leads
      showNextButton: false,   // toon “Next” knop als er meer pagina’s zijn
      showPreviousButton: false, // toon “Previous” als niet op eerste pagina
      currentPage: 1,          // huidig paginanummer
      query: ''                // zoekterm voor filteren
    }
  },
  mounted() {
    this.getLeads()          // haal leads op bij laden van component
  },
  methods: {
    // ga naar volgende pagina en haal opnieuw leads
    goToNextPage() {
      this.currentPage += 1
      this.getLeads()
    },
    // ga naar vorige pagina en haal opnieuw leads
    goToPreviousPage() {
      this.currentPage -= 1
      this.getLeads()
    },
    // haalt leads op van de API met zoek- en paginatieparameters
    async getLeads() {
      this.$store.commit('setIsLoading', true)  // toon globale loader
      this.showNextButton = false
      this.showPreviousButton = false

      try {
        const { data } = await axios.get(
          `/leads/?page=${this.currentPage}&search=${this.query}`
        )
        // sla resultaten op en bepaal of paginatie mogelijk is
        this.leads = Array.isArray(data.results) ? data.results : []
        this.showNextButton = !!data.next
        this.showPreviousButton = !!data.previous
      } catch (error) {
        console.error('Error fetching leads:', error.response?.data || error)
        this.leads = []  // reset bij fout
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
  transition: background-color 0.3s ease, border-color 0.3s ease;
}
.button.velos-red:hover {
  background-color: #821414;
  border-color: #821414;
}

/* marge onder de “Add lead” knop */
.mb-4 {
  margin-bottom: 1rem;
}
</style>
