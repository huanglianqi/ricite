<template>
  <div
    id="headImg">
    <b-avatar
      icon="person-fill"
      variant="white"
      size="2em"
      :button="button"
      rounded
      :src="src"></b-avatar></div>
</template>

<script>
export default {
  name: 'headImg',
  props: {
    src: {
      type: String,
      required: false
    },
    button: {
      type: Boolean,
      required: false,
      default: true
    }
  }
}
</script>

<style>
  #headImg:focus {
    outline: none;
  }
</style>
