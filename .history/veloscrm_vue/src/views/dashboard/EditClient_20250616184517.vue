<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Edit {{ client.name }}</h1>
      </div>

      <div class="column is-12">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Name</label>
            <div class="control">
              <input type="text" class="input" v-model="client.name" />
            </div>
          </div>

          <div class="field">
            <label>Contact person</label>
            <div class="control">
              <input type="text" class="input" v-model="client.contact_person" />
            </div>
          </div>

          <div class="field">
            <label>Email</label>
            <div class="control">
              <input type="email" class="input" v-model="client.email" />
            </div>
          </div>

          <div class="field">
            <label>Phone</label>
            <div class="control">
              <input type="text" class="input" v-model="client.phone" />
            </div>
          </div>

          <div class="field">
            <label>Website</label>
            <div class="control">
              <input type="text" class="input" v-model="client.website" />
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
  name: 'EditClient',
  data() {
    return {
      client: {}
    }
  },
  async mounted() {
    this.$store.commit('setIsLoading', true)
    try {
      const clientID = this.$route.params.id
      const { data } = await axios.get(`/api/v1/clients/${clientID}/`)
      this.client = data
    } catch (error) {
      console.error('Kon client niet ophalen:', error.response?.data || error)
      toast({
        message: 'Kon client niet laden',
        type: 'is-danger',
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: 'bottom-right',
      })
    } finally {
      this.$store.commit('setIsLoading', false)
    }
  },
  methods: {
    async submitForm() {
      this.$store.commit('setIsLoading', true)
      const clientID = this.$route.params.id

      const payload = {
        name:           this.client.name,
        contact_person: this.client.contact_person,
        email:          this.client.email,
        phone:          this.client.phone,
        website:        this.client.website,
      }

      try {
        await axios.patch(`/api/v1/clients/${clientID}/`, payload)

        toast({
          message: 'De client is geüpdatet',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right',
        })

        this.$router.push({ name: 'Client', params: { id: clientID } })
      } catch (error) {
        console.error('Update failed:', error.response?.data || error)
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
