// importeren van Vue Router en je centrale store voor auth-checks
import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

// componenten voor de verschillende pagina’s
import Home from '../views/Home.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import Dashboard from '../views/dashboard/Dashboard.vue'
import MyAccount from '../views/dashboard/MyAccount.vue'
import Leads from '../views/dashboard/Leads.vue'
import Lead from '../views/dashboard/Lead.vue'
import AddLead from '../views/dashboard/AddLead.vue'
import EditLead from '../views/dashboard/EditLead.vue'
import AddTeam from '../views/dashboard/AddTeam.vue'
import Team from '../views/dashboard/Team.vue'
import AddMember from '../views/dashboard/AddMember.vue'
import Clients from '../views/dashboard/Clients.vue'
import AddClient from '../views/dashboard/AddClient.vue'
import Client from '../views/dashboard/Client.vue'
import EditClient from '../views/dashboard/EditClient.vue'
import AddNote from '../views/dashboard/AddNote.vue'
import EditNote from '../views/dashboard/EditNote.vue'
import EditMember from '../views/dashboard/EditMember.vue'

// definieer alle routes van de applicatie
const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/sign-up', name: 'SignUp', component: SignUp },
  { path: '/log-in', name: 'LogIn', component: LogIn },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue') // lazy-loaded
  },
  // dashboard en alle subpagina’s vereisen inloggen
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: { requireLogin: true }
  },
  {
    path: '/dashboard/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: { requireLogin: true }
  },
  {
    path: '/dashboard/team',
    name: 'Team',
    component: Team,
    meta: { requireLogin: true }
  },
  {
    path: '/dashboard/edit-member/:id',
    name: 'EditMember',
    component: EditMember,
    meta: { requireLogin: true }
  },
  {
    path: '/dashboard/team/add-member',
    name: 'AddMember',
    component: AddMember,
    meta: { requireLogin: true }
  },
  {
    path: '/dashboard/add-team',
    name: 'AddTeam',
    component: AddTeam,
    meta: { requireLogin: true }
  },
  {
    path: '/dashboard/leads',
    name: 'Leads',
    component: Leads,
    meta: { requireLogin: true }
  },
  {
    path: '/dashboard/leads/add',
    name: 'AddLead',
    component: AddLead,
    meta: { requireLogin: true }
  },
  {
    path: '/dashboard/leads/:id',
    name: 'Lead',
    component: Lead,
    meta: { requireLogin: true }
  },
  {
    path: '/dashboard/leads/:id/edit',
    name: 'EditLead',
    component: EditLead,
    meta: { requireLogin: true }
  },
  {
    path: '/dashboard/clients',
    name: 'Clients',
    component: Clients,
    meta: { requireLogin: true }
  },
  {
    path: '/dashboard/clients/add',
    name: 'AddClient',
    component: AddClient,
    meta: { requireLogin: true }
  },
  {
    path: '/dashboard/clients/:id',
    name: 'Client',
    component: Client,
    meta: { requireLogin: true }
  },
  {
    path: '/dashboard/clients/:id/edit',
    name: 'EditClient',
    component: EditClient,
    meta: { requireLogin: true }
  },
  {
    path: '/dashboard/clients/:id/add-note',
    name: 'AddNote',
    component: AddNote,
    meta: { requireLogin: true }
  },
  {
    path: '/dashboard/clients/:id/edit-note/:note_id',
    name: 'EditNote',
    component: EditNote,
    meta: { requireLogin: true }
  }
]

// maak de router met HTML5-historymodus
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// navigatie-guard: controleer bij elke route of inloggen vereist is
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/log-in')   // stuur ongeauthenticeerde gebruikers naar inlogpagina
  } else {
    next()            // anders gewoon doorlaten
  }
})

export default router
