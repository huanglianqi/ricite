<template>
  <div
    id="toolProgress">
    <b-progress
      variant="success"
      :max="max">
      <b-progress-bar
        :value="value"
        :label="`${(value / max * 100).toFixed(2)}%`"
        :variant="variant">
      </b-progress-bar>
    </b-progress>
  </div>
</template>

<script>
export default {
  name: 'toolProgress',
  props: {
    max: {
      type: Number,
      required: true
    },
    value: {
      type: Number,
      required: true
    },
    variant: {
      type: String,
      required: false,
      default: () => {
        return 'success'
      }
    }
  }
}
</script>
