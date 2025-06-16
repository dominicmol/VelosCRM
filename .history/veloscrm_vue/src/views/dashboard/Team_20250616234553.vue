<template>
  <div class="container">
    <div class="columns is-multiline">
      <!-- header met teamnaam en optionele “Add member” knop -->
      <div class="column is-12">
        <h1 class="title">{{ team.name }}</h1>
        <hr />
        <!-- alleen tonen als ingelogde gebruiker de maker van het team is -->
        <template v-if="isCreator">
          <router-link :to="{ name: 'AddMember' }" class="button velos-button">
            Add member
          </router-link>
        </template>
      </div>

      <!-- sectie met lijst van teamleden of melding als er geen zijn -->
      <div class="column is-12">
        <h2 class="subtitle">Members</h2>
        <table class="table is-fullwidth" v-if="team.members && team.members.length">
          <thead>
            <tr>
              <th>Username</th>
              <th>Full name</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="member in team.members" :key="member.id">
              <td>{{ member.username }}</td>
              <td>{{ member.first_name }} {{ member.last_name }}</td>
            </tr>
          </tbody>
        </table>
        <p v-else>No members in this team yet.</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'  // HTTP-client om API-aanroepen te doen

export default {
  name: 'Team',            // component-naam voor registratie en debuggen
  data() {
    return {
      // houdt teamgegevens, inclusief naam, leden en maker
      team: {
        name: '',
        members: [],
        created_by: {}
      },
      isCreator: false      // bepaalt of de ingelogde gebruiker de maker is
    }
  },
  mounted() {
    this.getTeam()         // haal teamgegevens op bij mount
  },
  methods: {
    // haalt je eigen team op via de API en checkt of je de maker bent
    async getTeam() {
      this.$store.commit('setIsLoading', true)  // toon globale loader

      try {
        const response = await axios.get('/teams/get_my_team/')
        this.team = response.data

        // vergelijk ingelogde user-id met de creator-id om isCreator in te stellen
        const userId = parseInt(this.$store.state.user.id)
        this.isCreator =
          response.data.created_by &&
          parseInt(response.data.created_by.id) === userId
      } catch (error) {
        console.error('Error loading team:', error)
      } finally {
        this.$store.commit('setIsLoading', false) // verberg loader
      }
    }
  }
}
</script>

<style scoped>
/* stijl voor primary actieknop */
.button.velos-button {
  background-color: #a41917;
  color: white;
  font-weight: bold;
  border-radius: 6px;
  border: none;
  transition: background-color 0.3s ease;
}
/* hover-effect voor knop */
.button.velos-button:hover {
  background-color: #841614;
}
</style>
