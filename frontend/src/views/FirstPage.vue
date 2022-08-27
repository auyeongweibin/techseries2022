<template>
  <div class="firstPage">
    <h1><i>Anna's Steam Fresh Meat's Insurance Page</i></h1>
    <!-- <FormKit type="form" #default="{ value }"> -->
    <FormKit type="form">
      <div class="form-body">
        <h3>Search Insurance</h3>

        <FormKit
          v-model="birthday"
          type="date"
          value="1969-11-11"
          label="Date of Birth"
          validation="required|date_before: 2001-01-01|date_after: 1910-01-01"
          validation-visibility="live"
        />

        <FormKit
          type="select"
          label="Gender"
          v-model="gender"
          value="Male"
          placeholder="Choose a gender"
          validation="required"
          validation-visibility="live"
          :options="['Male', 'Female', 'Non-binary']"
        />

        <FormKit
          type="select"
          label="Are you a smoker?"
          v-model="smoker"
          value="No"
          placeholder="Choose an option"
          validation="required"
          validation-label="Field"
          validation-visibility="live"
          :options="['Yes', 'No']"
        />

        <FormKit
          type="select"
          label="What type of insurance are you looking for?"
          v-model="insuranceType"
          placeholder="Choose an option"
          validation="required"
          validation-label="Field"
          validation-visibility="live"
          :options="[
            'Direct Purchase Insurance Products',
            'Term Life Products',
            'Whole Life Products',
            'Endowment Products',
          ]"
        />

        <FormKit
          v-model="premiumType"
          type="select"
          label="Premium Type"
          placeholder="Choose an option"
          validation="required"
          validation-label="Field"
          validation-visibility="live"
          :options="['Annual', 'Premium']"
        />

        <FormKit
          v-model="sumAssured"
          type="select"
          label="Sum Assured"
          placeholder="Choose an option"
          help="Select an amount of coverage that you would like"
          validation="required"
          validation-label="Field"
          validation-visibility="live"
          :options="['S$500', 'S$1,000', 'S$5,000', 'S$10,000']"
        />

        <FormKit
          type="checkbox"
          label="Coverage Term"
          :options="[
            '0 to 5 Years',
            '6 to 10 Years',
            '11 to 15 Years',
            '16 to 20 Years',
          ]"
          help="Select the number of years you would like to spread the payment of premiums over."
          validation="required|min:1"
        />
        <pre wrap>{{ value }}</pre>

        <br /><FormKit
          type="checkbox"
          label="Terms of service"
          validation="accepted"
        />
        <!-- <details>
          <summary>Form data</summary>
          <pre>{{ value }}</pre>
        </details> -->
      </div>
    </FormKit>
  </div>
</template>


<script>
import axios from "axios";

export default {
  data() {
    return {
      formData: {
        birthday: "",
        gender: "",
        smoker: "",
        insuranceType: "",
        premiumType: "",
        sumAssured: "",
      },
    };
  },
  mounted() {
    axios
      .post(
        "http://techseries2022backend-env.eba-waamuq9p.ap-southeast-1.elasticbeanstalk.com/dev/policies",
        this.formData
      )
      .then((response) => console.log(response))
      .catch((error) => {
        console.log(error);
        this.errored = true;
      })
      .finally(() => (this.loading = false));
  },
};
</script>