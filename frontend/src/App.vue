<template>
  <div id="app">
    <first-page />
    <router-link to="/secondpage"></router-link>
  </div>
</template>

<script>
import FirstPage from './views/FirstPage'
export default {
  components: {
    FirstPage
  }
};
</script>
