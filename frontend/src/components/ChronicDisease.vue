<template>
    <div>
        <FormKit
          type="checkbox"
          label="Any Chronic Disease(s)?"
          v-model="chronicDiseases"
          :options="[
            'Hypertension',
            'Diabetes',
            'Dementia',
            'Others',
          ]"
          help="Please check where applicable."
        />

        <FormKit
          type="text"
          label="Any drug prescription?"
          help="Please type in the medication that was prescribed."
          validation="required"
          validation-label="Field"
          validation-visibility="live"
        />
    </div>
</template>

