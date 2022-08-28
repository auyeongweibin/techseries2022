<template>
  <div class="secondPage"><h1>Recommended For You</h1></div>

  <button @click="() => TogglePopup('buttonTrigger')">open policy</button>
  
  <Popup v-if="popupTriggers.buttonTrigger" :TogglePopup="() => TogglePopup('buttonTrigger')">
    <h2>Insurance Policy</h2>
    <p>
      Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rerum officia debitis, minus illo quod ad voluptate illum dolorum mollitia quidem praesentium, distinctio, ducimus vel eaque. Repellendus vitae necessitatibus iusto architecto?
    </p>
  </Popup>
</template>

<script>
import {ref} from 'vue';
import Popup from './component/Popup'

export default {
  data() {
    return {
      company: [],
      policyName: [],
      premiumType: [],
      productSummary: [],
      features: [],
    };
  },
  setup(){
    const popupTriggers = ref({
      buttonTrigger: false,
    });

    const TogglePopup = (trigger) => {
      popupTriggers.value[trigger] = !popupTriggers.value[trigger]
    }

    return{
      Popup,
      popupTriggers, 
      TogglePopup
    }
    }
  };
</script>

<style lang="scss">
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
  </style>