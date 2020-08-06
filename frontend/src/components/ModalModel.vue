<template>
  <div
    id="modalModel">
    <b-modal
      :id="id"
      size="xl"
      hide-header
      centered
      ok-variant="outline-success"
      ok-only
      ok-title="关闭"
      body-bg-variant="light">
      <slot></slot></b-modal></div>
</template>

<script>
export default {
  name: 'modalModel',
  props: {
    id: {
      type: String,
      required: true
    }
  }
}
</script>
