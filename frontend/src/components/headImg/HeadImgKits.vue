<template>
  <div
    id="headImgKits">
    <b-row
      class="m-1">
      <slot
        name="button"></slot>
      <b-col
        v-if="twoLine">
        <b-row>
          <span
            class="font-weight-bold">
            <slot
              name="topText"></slot></span></b-row>
        <b-row>
          <small
            class="text-truncate">
            <slot
              name="bottomText"></slot></small></b-row></b-col>
      <b-col
        v-else
        class="font-weight-bold pl-1">
        <slot
          name="centerText"></slot></b-col></b-row></div>
</template>

<script>
export default {
  name: 'headImgKits',
  props: {
    twoLine: {
      type: Boolean,
      required: false
    }
  }
}
</script>

<style>

</style>
