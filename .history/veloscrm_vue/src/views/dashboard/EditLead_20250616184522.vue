<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Edit {{ lead.company }}</h1>
      </div>

      <div class="column is-12">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Company</label>
            <div class="control">
              <input type="text" class="input" v-model="lead.company" />
            </div>
          </div>

          <div class="field">
            <label>Contact person</label>
            <div class="control">
              <input type="text" class="input" v-model="lead.contact_person" />
            </div>
          </div>

          <div class="field">
            <label>Email</label>
            <div class="control">
              <input type="email" class="input" v-model="lead.email" />
            </div>
          </div>

          <div class="field">
            <label>Phone</label>
            <div class="control">
              <input type="text" class="input" v-model="lead.phone" />
            </div>
          </div>

          <div class="field">
            <label>Website</label>
            <div class="control">
              <input type="text" class="input" v-model="lead.website" />
            </div>
          </div>

          <div class="field">
            <label>Confidence</label>
            <div class="control">
              <input type="number" class="input" v-model="lead.confidence" />
            </div>
          </div>

          <div class="field">
            <label>Estimated value</label>
            <div class="control">
              <input type="number" class="input" v-model="lead.estimated_value" />
            </div>
          </div>

          <div class="field">
            <label>Status</label>
            <div class="control">
              <div class="select">
                <select v-model="lead.status">
                  <option value="new">New</option>
                  <option value="contacted">Contacted</option>
                  <option value="inprogress">In progress</option>
                  <option value="lost">Lost</option>
                  <option value="won">Won</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <label>Priority</label>
            <div class="control">
              <div class="select">
                <select v-model="lead.priority">
                  <option value="low">Low</option>
                  <option value="medium">Medium</option>
                  <option value="high">High</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <label>Assigned to</label>
            <div class="control">
              <div class="select">
                <select v-model="lead.assigned_to">
                  <option value="" selected>Select member</option>
                  <option
                    v-for="member in team.members"
                    :key="member.id"
                    :value="member.id"
                  >
                    {{ member.username }}
                  </option>
                </select>
              </div>
            </div>
          </div>

          <div class="field is-grouped is-grouped-right">
            <div class="control">
              <button class="button velos-button">Update</button>
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
  name: 'EditLead',
  data() {
    return {
      lead: {},
      team: {
        members: []
      }
    }
  },
  async mounted() {
    this.$store.commit('setIsLoading', true)
    await Promise.all([this.getLead(), this.getTeam()])
    this.$store.commit('setIsLoading', false)
  },
  methods: {
    async getLead() {
      try {
        const leadID = this.$route.params.id
        const { data } = await axios.get(`/leads/${leadID}/`)
        this.lead = data
      } catch (error) {
        console.error('Fout bij ophalen lead:', error.response?.data || error)
        toast({
          message: 'Kon lead niet laden',
          type: 'is-danger',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right',
        })
      }
    },
    async getTeam() {
      try {
        const { data } = await axios.get('/teams/get_my_team/')
        this.team = data
      } catch (error) {
        console.error('Fout bij ophalen team:', error.response?.data || error)
      }
    },
    async submitForm() {
      this.$store.commit('setIsLoading', true)
      try {
        const leadID = this.$route.params.id
        await axios.patch(`/leads/${leadID}/`, this.lead)
        toast({
          message: 'De lead is geüpdatet',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right',
        })
        this.$router.push({ name: 'Lead', params: { id: leadID } })
      } catch (error) {
        console.error('Update mislukt:', error.response?.data || error)
        toast({
          message: 'Update mislukt',
          type: 'is-danger',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
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
