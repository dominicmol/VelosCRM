<template>
  <div class="container">
    <div class="columns is-multiline">
      <!-- paginatitel -->
      <div class="column is-12">
        <h1 class="title">Add lead</h1>
      </div>

      <!-- formulier om een nieuwe lead toe te voegen -->
      <div class="column is-12">
        <form @submit.prevent="submitForm">
          <!-- bedrijfsnaamveld -->
          <div class="field">
            <label>Company</label>
            <div class="control">
              <input
                type="text"
                class="input"
                v-model="company"
                placeholder="Enter company name"
                required
              />
            </div>
          </div>

          <!-- contactpersoonveld -->
          <div class="field">
            <label>Contact person</label>
            <div class="control">
              <input
                type="text"
                class="input"
                v-model="contact_person"
                placeholder="Enter contact person"
                required
              />
            </div>
          </div>

          <!-- e-mailveld -->
          <div class="field">
            <label>Email</label>
            <div class="control">
              <input
                type="email"
                class="input"
                v-model="email"
                placeholder="example@company.com"
              />
            </div>
          </div>

          <!-- telefoonveld -->
          <div class="field">
            <label>Phone</label>
            <div class="control">
              <input
                type="text"
                class="input"
                v-model="phone"
                placeholder="Enter phone number"
              />
            </div>
          </div>

          <!-- websiteveld -->
          <div class="field">
            <label>Website</label>
            <div class="control">
              <input
                type="text"
                class="input"
                v-model="website"
                placeholder="https://"
              />
            </div>
          </div>

          <!-- confidence-waarde (0–100) -->
          <div class="field">
            <label>Confidence</label>
            <div class="control">
              <input
                type="number"
                class="input"
                v-model="confidence"
                placeholder="Enter confidence"
                min="0"
                max="100"
              />
            </div>
          </div>

          <!-- geschatte waardeveld -->
          <div class="field">
            <label>Estimated value</label>
            <div class="control">
              <input
                type="number"
                class="input"
                v-model="estimated_value"
                placeholder="Enter estimated value"
                min="0"
              />
            </div>
          </div>

          <!-- status-select -->
          <div class="field">
            <label>Status</label>
            <div class="control">
              <div class="select">
                <select v-model="status">
                  <option value="new">New</option>
                  <option value="contacted">Contacted</option>
                  <option value="inprogress">In progress</option>
                  <option value="lost">Lost</option>
                  <option value="won">Won</option>
                </select>
              </div>
            </div>
          </div>

          <!-- prioriteits-select -->
          <div class="field">
            <label>Priority</label>
            <div class="control">
              <div class="select">
                <select v-model="priority">
                  <option value="low">Low</option>
                  <option value="medium">Medium</option>
                  <option value="high">High</option>
                </select>
              </div>
            </div>
          </div>

          <!-- verzendknop -->
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
import axios from 'axios'             // HTTP-client om API-aanroepen te doen
import { toast } from 'bulma-toast'   // visuele meldingen onderaan scherm

export default {
  name: 'AddLead',                    // component-naam
  data() {
    return {
      // formuliergegevens
      company: '',
      contact_person: '',
      email: '',
      phone: '',
      website: '',
      confidence: 0,
      estimated_value: 0,
      status: 'new',    // standaardstatus voor nieuwe leads
      priority: 'medium' // standaard prioriteit
    }
  },
  methods: {
    // functie bij formulierverzending
    async submitForm() {
      this.$store.commit('setIsLoading', true) // toon loading-indicator

      // bouw payload voor de API
      const payload = {
        company: this.company,
        contact_person: this.contact_person,
        email: this.email,
        phone: this.phone,
        website: this.website,
        confidence: this.confidence,
        estimated_value: this.estimated_value,
        status: this.status,
        priority: this.priority
      }

      try {
        // verzend de POST-aanvraag naar de /leads/ endpoint
        await axios.post('/leads/', payload)

        // succesmelding tonen
        toast({
          message: 'The lead was added',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right'
        })

        // navigeer naar de leads-lijst
        this.$router.push('/dashboard/leads')
      } catch (error) {
        console.error('Error adding lead:', error)
        // foutmelding tonen
        toast({
          message: 'Failed to add lead',
          type: 'is-danger',
          dismissible: true,
          pauseOnHover: true,
          duration: 3000,
          position: 'bottom-right'
        })
      } finally {
        // verberg loading-indicator
        this.$store.commit('setIsLoading', false)
      }
    }
  }
}
</script>

<style scoped>
/* stijl voor de Submit-knop */
.button.velos-button {
  background-color: #a41917;
  color: #fff;
  font-weight: bold;
  border-radius: 6px;
  border: none;
  transition: background-color 0.3s ease;
}

/* hover-effect voor de knop */
.button.velos-button:hover {
  background-color: #841614;
}
</style>
