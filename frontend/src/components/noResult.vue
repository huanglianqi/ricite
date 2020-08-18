<template>
  <div
    id="noResult">
    <div
      v-show="show"
      class="mt-5">
      <b-icon
        :icon="icon"
        :font-scale="size"></b-icon>
        <p
          class="font-weight-bold">
          {{content}}</p></div></div>
</template>

<script>
export default {
  name: 'noResult',
  props: {
    show: {
      type: Boolean,
      required: true
    },
    icon: {
      type: String,
      required: true
    },
    size: {
      type: String,
      required: false,
      default: '5'
    },
    content: {
      type: String,
      required: false,
      default: 'No Result'
    }
  }
}
</script>
