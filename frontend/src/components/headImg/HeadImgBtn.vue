<template>
  <div
    id="headImgBtn">
    <b-avatar
      class="mr-2"
      icon="person-fill"
      variant="white"
      :size="size"
      :button="true"
      :rounded="rounded"
      :src="src"></b-avatar></div>
</template>

<script>
export default {
  name: 'headImgBtn',
  props: {
    src: {
      type: String,
      required: false
    },
    size: {
      type: String,
      required: false
    },
    rounded: {
      type: Boolean,
      required: false,
      default: true
    }
  }
}
</script>

<style>
  #headImgBtn:focus {
    outline: none;
  }
</style>
