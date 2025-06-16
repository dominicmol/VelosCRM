<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">{{ lead.company }}</h1>

        <div class="buttons">
          <router-link
            :to="{ name: 'EditLead', params: { id: lead.id } }"
            class="button velos-button"
          >
            Edit
          </router-link>

          <button @click="convertToClient" class="button velos-button-convert">
            Convert to client
          </button>

          <button @click="deleteLead" class="button velos-button-delete is-outlined">
            Delete
          </button>
        </div>
      </div>

      <div class="column is-6">
        <div class="box">
          <h2 class="subtitle">Details</h2>

          <template v-if="lead.assigned_to">
            <p>
              <strong>Assigned to: </strong>
              {{ lead.assigned_to.first_name }} {{ lead.assigned_to.last_name }}
            </p>
          </template>
          <p><strong>Status: </strong>{{ lead.status }}</p>
          <p><strong>Priority: </strong>{{ lead.priority }}</p>
          <p><strong>Confidence: </strong>{{ lead.confidence }}</p>
          <p><strong>Estimated value: </strong>{{ lead.estimated_value }}</p>
          <p><strong>Created at: </strong>{{ lead.created_at }}</p>
          <p><strong>Modified at: </strong>{{ lead.modified_at }}</p>
        </div>
      </div>

      <div class="column is-6">
        <div class="box">
          <h2 class="subtitle">Contact information</h2>

          <p><strong>Contact person: </strong>{{ lead.contact_person }}</p>
          <p><strong>Email: </strong>{{ lead.email }}</p>
          <p><strong>Phone: </strong>{{ lead.phone }}</p>
          <p><strong>Website: </strong>{{ lead.website }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Lead',
  data() {
    return {
      lead: {}
    }
  },
  async mounted() {
    this.$store.commit('setIsLoading', true)
    await this.getLead()
    this.$store.commit('setIsLoading', false)
  },
  methods: {
    async getLead() {
      const leadID = this.$route.params.id
      try {
        const { data } = await axios.get(`/leads/${leadID}/`)
        this.lead = data
      } catch (error) {
        console.error('Error fetching lead:', error.response?.data || error)
      }
    },
    async deleteLead() {
      this.$store.commit('setIsLoading', true)
      const leadID = this.$route.params.id
      try {
        await axios.post(`/leads/delete_lead/${leadID}/`)
        this.$router.push('/dashboard/leads')
      } catch (error) {
        console.error('Error deleting lead:', error.response?.data || error)
      } finally {
        this.$store.commit('setIsLoading', false)
      }
    },
    async convertToClient() {
      this.$store.commit('setIsLoading', true)
      const leadID = this.$route.params.id
      try {
        await axios.post(`/clients/convert_lead_to_client/`, { lead_id: leadID })
        this.$router.push('/dashboard/clients')
      } catch (error) {
        console.error('Error converting lead:', error.response?.data || error)
      } finally {
        this.$store.commit('setIsLoading', false)
      }
    }
  }
}
</script>

<style scoped>
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

.velos-button-convert {
  background-color: #ee8b1a;
  border-color: transparent;
  color: white;
  font-weight: 600;
  transition: background-color 0.3s ease;
}
.velos-button-convert:hover {
  background-color: #d17a15;
  color: white;
}

.button.velos-button-delete.is-outlined {
  background-color: white;
  color: #a41917;
  border-color: #a41917;
  font-weight: 600;
  transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
}
.button.velos-button-delete.is-outlined:hover {
  background-color: #fcebeb;
  color: #821414;
  border-color: #821414;
}
</style>
