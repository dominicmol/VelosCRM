<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">{{ team.name }}</h1>

        <hr />

        <template v-if="isCreator">
          <router-link :to="{ name: 'AddMember' }" class="button velos-button">
            Add member
          </router-link>
        </template>
      </div>

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
import axios from 'axios'

export default {
  name: 'Team',
  data() {
    return {
      team: {
        name: '',
        members: [],
        created_by: {}
      },
      isCreator: false
    }
  },
  mounted() {
    this.getTeam()
  },
  methods: {
    async getTeam() {
      this.$store.commit('setIsLoading', true)

      try {
        const response = await axios.get('/teams/get_my_team/')
        this.team = response.data

        const userId = parseInt(this.$store.state.user.id)
        this.isCreator =
          response.data.created_by &&
          parseInt(response.data.created_by.id) === userId

      } catch (error) {
        console.error('Error loading team:', error)
      }

      this.$store.commit('setIsLoading', false)
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