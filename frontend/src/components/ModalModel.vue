<template>
  <div
    id="modalModel">
    <b-modal
      :id="id"
      :size="size"
      hide-header
      centered
      ok-variant="outline-success"
      ok-only
      ok-title="关闭"
      :hide-footer="hideFooter"
      :body-bg-variant="bodyBgVariant">
      <slot></slot></b-modal></div>
</template>

<script>
export default {
  name: 'modalModel',
  props: {
    id: {
      type: String,
      required: true
    },
    size: {
      type: String,
      required: false,
      default: 'xl'
    },
    bodyBgVariant: {
      type: String,
      required: false,
      default: 'white'
    },
    hideFooter: {
      type: Boolean,
      required: false,
      default: false
    }
  }
}
</script>

<style>
#modalModel {
  z-index: inherit;
}
</style>
