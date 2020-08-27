<template>
  <div
    id="modalModel">
    <b-modal
      :id="id"
      :size="size"
      :centered="true"
      :hide-header="true"
      :hide-header-close="true"
      :hide-footer="hideFooter">
      <slot></slot></b-modal></div>
</template>

<script>
export default {
  name: 'modalModel',
  props: {
    id: {
      type: String,
      required: false
    },
    size: {
      type: String,
      required: false,
      default: 'xl'
    },
    hideFooter: {
      type: Boolean,
      required: false,
      defalut: true
    }
  }
}
</script>
