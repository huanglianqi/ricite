<template>
  <div
    id="numberBoard">
    <div
      v-b-hover="handleHover">
      <b-button
        @click="buttonClick(detail)"
        class="p-5 shadow-sm"
        block
        variant="light">
        <h1
          :class="numberFrontClass"
          v-show="!isHover">{{numberFront}}</h1>
        <h1
          :class="numberBackClass"
          v-show="isHover">{{numberBack}}</h1>
        <p
          class="font-weight-bold"
          v-show="!isHover">
          {{titleFront}}</p>
        <p
          class="font-weight-bold"
          v-show="isHover">
          {{titleBack}}</p>
        <small
          class="muted"
          v-show="!isHover">
          {{subTitleFront}}</small>
        <small
          class="muted"
          v-show="isHover">
          {{subTitleBack}}</small></b-button></div></div>
</template>

<script>
export default {
  name: 'numberBoard',
  props: {
    titleFront: {
      type: String,
      required: false
    },
    titleBack: {
      type: String,
      required: false
    },
    numberFront: {
      type: String,
      required: false
    },
    numberBack: {
      type: String,
      required: false
    },
    numberFrontClass: {
      type: String,
      required: false
    },
    numberBackClass: {
      type: String,
      required: false
    },
    subTitleFront: {
      type: String,
      required: false
    },
    subTitleBack: {
      type: String,
      required: false
    },
    detail: {
      type: Array,
      required: false
    },
    buttonClick: {
      type: Function,
      required: false
    }
  },
  data () {
    return {
      isHover: false
    }
  },
  methods: {
    handleHover (hovered) {
      this.isHover = hovered
    },
    click (detail) {
      this.buttonClick(detail)
    }
  }
}
</script>
