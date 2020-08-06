<template>
  <div
    id="personDetailModal">
    <modal-model
      :id="id">{{detail}}</modal-model></div>
</template>

<script>
import ModalModelVue from './ModalModel.vue'

export default {
  name: 'personDetailModal',
  components: {
    'modal-model': ModalModelVue
  },
  props: {
    id: {
      type: String,
      required: true
    },
    detail: {
      type: Object,
      required: true
    }
  }
}
</script>
