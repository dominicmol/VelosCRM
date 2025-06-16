<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Leads</h1>

        <router-link to="/dashboard/leads/add" class="button velos-red mb-4">
          Add lead
        </router-link>

        <hr>

        <form @submit.prevent="getLeads">
          <div class="field has-addons">
            <div class="control">
              <input type="text" class="input" v-model="query" placeholder="Search leads...">
            </div>
            <div class="control">
              <button class="button velos-red">Search</button>
            </div>
          </div>
        </form>
      </div>

      <div class="column is-12">
        <table class="table is-fullwidth">
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
                <template v-if="lead.assigned_to">
                  {{ lead.assigned_to.first_name }} {{ lead.assigned_to.last_name }}
                </template>
              </td>
              <td>{{ lead.status }}</td>
              <td>
                <router-link :to="{ name: 'Lead', params: { id: lead.id } }">Details</router-link>
              </td>
            </tr>
          </tbody>
        </table>

        <div class="buttons">
          <button class="button is-light" @click="goToPreviousPage" v-if="showPreviousButton">Previous</button>
          <button class="button is-light" @click="goToNextPage" v-if="showNextButton">Next</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Leads',
  data() {
    return {
      leads: [],
      showNextButton: false,
      showPreviousButton: false,
      currentPage: 1,
      query: ''
    }
  },
  mounted() {
    this.getLeads()
  },
  methods: {
    goToNextPage() {
      this.currentPage += 1
      this.getLeads()
    },
    goToPreviousPage() {
      this.currentPage -= 1
      this.getLeads()
    },
    async getLeads() {
      this.$store.commit('setIsLoading', true)

      this.showNextButton = false
      this.showPreviousButton = false

      try {
        const response = await axios.get(`/api/v1/leads/?page=${this.currentPage}&search=${this.query}`)
        this.leads = response.data.results

        this.showNextButton = !!response.data.next
        this.showPreviousButton = !!response.data.previous
      } catch (error) {
        console.error(error)
      }

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

<style scoped>
.button.velos-red {
  background-color: #a41917;
  border-color: #a41917;
  color: #fff;
}

.button.velos-red:hover {
  background-color: #821414;
  border-color: #821414;
}
</style>