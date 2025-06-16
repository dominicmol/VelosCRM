<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">My account</h1>
      </div>

      <div class="column is-12">
        <div class="buttons">
          <router-link 
            :to="{ name: 'EditMember', params: { id: $store.state.user.id } }" 
            class="button velos-button is-light"
          >
            Edit
          </router-link>

          <button @click="logout" class="button velos-button is-outlined">Log out</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MyAccount',
  methods: {
    async logout() {
      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem('token')
      localStorage.removeItem('username')
      localStorage.removeItem('userid')
      localStorage.removeItem('team_name')
      localStorage.removeItem('team_id')

      this.$store.commit('removeToken')
      this.$router.push('/')
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

.button.velos-button.is-outlined {
    background-color: white; 
    color: #a41917; 
    border-color: #a41917; 
}

.button.velos-button.is-outlined:hover {
    background-color: #fcebeb; 
    color: #821414; 
    border-color: #821414;
}

</style>