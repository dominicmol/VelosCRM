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
              <router-link to="/log-in" class="button velos-button-outlined">Log in</router-link>
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
  color: #222222;
  font-weight: bold;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
}

.velos-navbar {
  background-color: #ffffff !important; 
  border-bottom: 1px solid #d9bf9c; 
}

.brand-link {
  color: #a41917 !important;
}

.nav-link {
  color: #a41917 !important;
}

.nav-link:hover {
  background-color: transparent;
  color: #821414 !important; 
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

.button.velos-button-outlined {
    background-color: #ffffff !important;
    color: #a41917 !important; 
    border-color: #a41917 !important;
    font-weight: 600;
    transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
}

.button.velos-button-outlined:hover {
    background-color: #ffffff !important; 
    color: #821414 !important; 
    border-color: #821414 !important; 
}
</style>