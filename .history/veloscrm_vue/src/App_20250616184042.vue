<template>
  <div>
    <Navbar />

    <div class="is-loading-bar has-text-centered" :class="{ 'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>

    <section class="section">
      <router-view />
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import Navbar from '@/components/layout/Navbar'

export default {
  name: 'App',
  components: {
    Navbar
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    if (this.$store.state.token) {
      axios.defaults.headers.common['Authorization'] = 'Token ' + this.$store.state.token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

.button.velos-red {
  background-color: #a41917;
  color: #fff;
  border: none;

  &:hover {
    background-color: #8c1412;
  }

  &:focus {
    box-shadow: 0 0 0 0.125em rgba(164, 25, 23, 0.25);
  }

  &:active {
    background-color: #76110f;
  }

  &.is-loading::after {
    border-color: transparent transparent #fff #fff !important;
  }
}

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}

.lds-dual-ring:after {
  content: ' ';
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #a41917;
  border-color: #a41917 transparent #a41917 transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
</style>