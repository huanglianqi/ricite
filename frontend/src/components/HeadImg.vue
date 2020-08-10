<template>
  <div
    id="headImg">
    <b-avatar
      class="mr-2"
      icon="person-fill"
      variant="white"
      size="2em"
      :button="button"
      rounded
      v-b-modal.personInfo
      :src="src"></b-avatar>
    <span
      class="align-bottom"
      v-show="showName">{{info.name}}</span>
    <person-info
      :info="info"></person-info></div>
</template>

<script>
import ModalModelVue from './ModalModel.vue'
import PersonInfoVue from './PersonInfo.vue'

export default {
  name: 'headImg',
  components: {
    'modal-model': ModalModelVue,
    'person-info': PersonInfoVue
  },
  props: {
    src: {
      type: String,
      required: false
    },
    button: {
      type: Boolean,
      required: false,
      default: true
    },
    info: {
      type: Object,
      required: false
    },
    showName: {
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
