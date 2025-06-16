<template>
  <div class="container">
    <div class="columns is-multiline">
      <!-- pagina-header -->
      <div class="column is-12">
        <h1 class="title">My account</h1>
      </div>

      <!-- knoppen om profiel te bewerken of uit te loggen -->
      <div class="column is-12">
        <div class="buttons">
          <!-- link naar bewerk-scherm voor de huidige gebruiker -->
          <router-link 
            :to="{ name: 'EditMember', params: { id: $store.state.user.id } }" 
            class="button velos-button is-light"
          >
            Edit
          </router-link>

          <!-- knop om uit te loggen -->
          <button @click="logout" class="button velos-button is-outlined">
            Log out
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'  // HTTP-client voor eventuele API-aanroepen

export default {
  name: 'MyAccount',
  methods: {
    // verwijdert token en gebruikersgegevens, navigeert terug naar home
    async logout() {
      // haal Authorization-header weg
      axios.defaults.headers.common['Authorization'] = ''
      // wis opgeslagen credentials en teamgegevens
      localStorage.removeItem('token')
      localStorage.removeItem('username')
      localStorage.removeItem('userid')
      localStorage.removeItem('team_name')
      localStorage.removeItem('team_id')

      // update store zodat gebruiker als uitgelogd wordt gemarkeerd
      this.$store.commit('removeToken')
      // stuur terug naar startpagina
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>
/* basisstijl voor actieknoppen */
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

/* style voor outlined knop (logout) */
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
