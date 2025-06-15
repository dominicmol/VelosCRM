<template>
  <div class="home velos-home">
    <img alt="Velos logo" src="../assets/logo.png" />
    <HelloWorld />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script>

<style scoped>
.velos-home {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
}

.velos-home img {
  max-width: 200px;
  margin-bottom: 1.5rem;
}
</style>
