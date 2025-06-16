<template>
  <nav class="navbar velos-navbar">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item brand-link">
        <img src="@/assets/logo.png" alt="Velos logo" class="navbar-logo" />
        <span class="navbar-title">Velos CRM</span>
      </router-link>
    </div>

    <div class="navbar-menu">
      <div class="navbar-end">
        <template v-if="$store.state.isAuthenticated">
          <router-link to="/dashboard/leads" class="navbar-item nav-link">Leads</router-link>
          <router-link to="/dashboard/clients" class="navbar-item nav-link">Clients</router-link>
          <router-link to="/dashboard/team" class="navbar-item nav-link">Team</router-link>
        </template>

        <div class="navbar-item">
          <div class="buttons">
            <template v-if="!$store.state.isAuthenticated">
              <router-link to="/sign-up" class="button velos-button"><strong>Sign up</strong></router-link>
              <router-link to="/log-in" class="button is-light">Log in</router-link>
            </template>

            <template v-else>
              <router-link to="/dashboard/my-account" class="button velos-button">My account</router-link>
            </template>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style scoped>
.navbar-logo {
  height: 40px;
  width: auto;
  margin-right: 10px;
}

.navbar-title {
  color: white;
  font-weight: bold;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
}

/* 🌑 Velos kleuren */
.velos-navbar {
  background-color: #a41917 !important;
}

/* Nav links wit maken */
.nav-link {
  color: white !important;
}

.nav-link:hover {
  background-color: transparent;
  color: #e8ceb0 !important; /* optioneel: zachte hoverkleur */
}

/* Zorg ook dat de merk-link wit is */
.brand-link {
  color: white !important;
}

.velos-button {
  background-color: #ee8b1a !important;
  border-color: transparent;
  color: white !important;
}

.velos-button:hover {
  background-color: #d97706 !important;
  color: white !important;
}
</style>
