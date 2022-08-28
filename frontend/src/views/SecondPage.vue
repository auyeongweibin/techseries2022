<template>
  <div class="secondPage"><h1>Hello World!</h1></div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      company: [],
      policy: [],
    };
  },

  methods: {
    async getData() {
      try {
        const response = await axios.get(
        "http://techseries2022backend-env.eba-waamuq9p.ap-southeast-1.elasticbeanstalk.com/dev/policies"
        );
        this.company = response.data.company;
        this.policy = response.data.policy;
      } catch (error) {
        console.log(error);
      }
    },
  },
};
  </script>