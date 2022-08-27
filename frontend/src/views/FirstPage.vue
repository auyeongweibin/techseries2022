<template>
  <div class="firstPage">
    <h1><i>Anna's Steam Fresh Meat's Insurance Page</i></h1>

    <FormKit type="form" v-model="formData">
      <div class="form-body">
        <h3>Search Insurance</h3>

        <FormKit
          type="date"
          value="1969-11-11"
          label="Date of Birth"
          validation="required|date_before: 2001-01-01|date_after: 1910-01-01"
          validation-visibility="live"
          name="birthday"
        />

        <FormKit
          type="select"
          label="Gender"
          name="gender"
          value="Male"
          placeholder="Choose a gender"
          validation="required"
          validation-visibility="live"
          :options="['Male', 'Female', 'Non-binary']"
        />

        <FormKit
          type="select"
          label="Are you a smoker?"
          name="smoker"
          value="No"
          placeholder="Choose an option"
          validation="required"
          validation-label="Field"
          validation-visibility="live"
          :options="['Yes', 'No']"
        />

        <FormKit
          type="select"
          label="Any intake of nicotine within the last 12 months?"
          name="nicotine"
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
          name="insuranceType"
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
          name="premiumType"
          type="select"
          label="Premium Type"
          placeholder="Choose an option"
          validation="required"
          validation-label="Field"
          validation-visibility="live"
          :options="['Annual', 'Premium']"
        />

        <FormKit
          name="sumAssured"
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
          name="coverageTerm"
          :options="[
            '0 to 5 Years',
            '6 to 10 Years',
            '11 to 15 Years',
            '16 to 20 Years',
          ]"
          help="Select the number of years you would like to spread the payment of premiums over."
          validation="required|min:1"
        />

        <FormKit
          type="select"
          label="Do you have any chronic disease?"
          placeholder="Choose an option"
          validation="required"
          validation-label="Field"
          validation-visibility="live"
          :options="['Yes', 'No']"
          name="chronicDisease"
        />

        <!-- <p>Do you have any chronic diseases?</p>
        <select v-model="chronicDisease">
          <option value="Yes">Yes</option>
          <option value="No">No</option>
        </select>
        <br /><br /> -->

        <chronic-disease v-if="chronicDisease === 'Yes'" />
        <br />
        <FormKit
          type="checkbox"
          label="Terms of service"
          validation="accepted"
        />
      </div>
    </FormKit>
  </div>
</template>

<script>
import axios from "axios";
// import { useRouter } from 'vue-router'

// const route = useRoute()
// const router = useRouter()

export default {
  data() {
    return {
      formData: {
        birthday: "1969-11-11",
        gender: "Male",
        smoker: "No",
        nicotine: "No",
        insuranceType: "",
        premiumType: "",
        sumAssured: "",
        coverageTerm: [],
        chronicDisease: "",
      },
    };
  },
  // methods: {
  //   secondPage() {
  //     router.push('/secondpage')
  //   }
  // },
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
