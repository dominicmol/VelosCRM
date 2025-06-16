<template>
  <section class="section has-text-centered velos-home">
    <div class="container">
      <img alt="Velos logo" src="@/assets/logo.png" />
      <h1 class="title is-3">Welkom bij Velos CRM</h1>
      <p class="subtitle is-5">
        Velos CRM is jouw centrale plek voor leadbeheer, klantcontacten en teamoverzicht — gebouwd door en voor marketeers.
      </p>

      <div class="content mt-5">
        <p>
          Gebruik het menu bovenaan om te navigeren naar je leads, klanten of teamleden. 
          Dit dashboard is ontworpen voor snelheid, overzicht en eenvoud.
        </p>
        <p>
           Functionaliteiten: voeg notities toe aan klanten, volg leads op per status, en houd je teamleden altijd up-to-date.
        </p>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Home'
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
  max-width: 150px;
  margin-bottom: 1.5rem;
}
</style>