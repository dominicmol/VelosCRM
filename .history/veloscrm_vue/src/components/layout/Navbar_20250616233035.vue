<template>
  <!-- hoofd navigatiebalk voor Velos CRM -->
  <nav class="navbar velos-navbar">
    <!-- merklogo en link naar home -->
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item brand-link">
        <img src="@/assets/logo.png" alt="Velos logo" class="navbar-logo" />
        <span class="navbar-title">Velos CRM</span>
      </router-link>
    </div>

    <!-- navigatie-items aan de rechterkant -->
    <div class="navbar-menu">
      <div class="navbar-end">
        <!-- links voor ingelogde gebruikers -->
        <template v-if="$store.state.isAuthenticated">
          <router-link to="/dashboard/leads" class="navbar-item nav-link">Leads</router-link>
          <router-link to="/dashboard/clients" class="navbar-item nav-link">Clients</router-link>
          <router-link to="/dashboard/team" class="navbar-item nav-link">Team</router-link>
        </template>

        <!-- knoppen voor in- en uitloggen of account -->
        <div class="navbar-item">
          <div class="buttons">
            <!-- als niet ingelogd: toon signup en login -->
            <template v-if="!$store.state.isAuthenticated">
              <router-link to="/sign-up" class="button velos-button"><strong>Sign up</strong></router-link>
              <router-link to="/log-in" class="button velos-button-outlined">Log in</router-link>
            </template>
            <!-- als ingelogd: link naar accountpagina -->
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
  name: 'Navbar'  // componentnaam voor debugging en registratie
}
</script>

<style scoped>
/* logo-afmetingen en ruimte ernaast */
.navbar-logo {
  height: 40px;
  width: auto;
  margin-right: 10px;
}

/* titelstijl naast logo */
.navbar-title {
  color: #222222;
  font-weight: bold;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
}

/* achtergrond en onderrand van navigatiebalk */
.velos-navbar {
  background-color: #ffffff !important;
  border-bottom: 1px solid #d9bf9c;
}

/* kleur merknaam-link */
.brand-link {
  color: #a41917 !important;
}

/* standaard kleur navigatielinks */
.nav-link {
  color: #a41917 !important;
}

/* hover-effect voor navigatielinks */
.nav-link:hover {
  background-color: transparent;
  color: #821414 !important;
}

/* primaire button-stijl */
.velos-button {
  background-color: #ee8b1a !important;
  border-color: transparent;
  color: white !important;
}

/* hover-stijl voor primaire button */
.velos-button:hover {
  background-color: #d97706 !important;
  color: white !important;
}

/* stijl voor outlined secondary button */
.button.velos-button-outlined {
  background-color: #ffffff !important;
  color: #a41917 !important;
  border-color: #a41917 !important;
  font-weight: 600;
  transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
}

/* hover-effect voor outlined button */
.button.velos-button-outlined:hover {
  background-color: #ffffff !important;
  color: #821414 !important;
  border-color: #821414 !important;
}
</style>
