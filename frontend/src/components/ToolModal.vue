<template>
  <div
    id="toolModal">
    <b-modal
      :id="id"
      centered
      size='xl'
      ok-only
      ok-variant="outline-success"
      body-bg-variant="light"
      :title="title">
      <slot></slot>
      <template
        v-slot:modal-ok>
        关闭
      </template>
    </b-modal>
  </div>
</template>

<script>
export default {
  name: 'toolModal',
  props: {
    id: {
      type: String,
      required: false
    },
    title: {
      type: String,
      required: false
    }
  }
}
</script>
