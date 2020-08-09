<template>
  <div
    id="personInfo">
    <modal-model
      :id="id"
      :size="'lg'">
      <b-card
        border-variant="white">
        <b-list-group
          class="p-2"
          flush>
          <b-list-group-item
            class="font-weight-bold p-3 shadow-lg mb-2 bg-success text-light text-center rounded w-100 align-self-center">
            教师基础信息表</b-list-group-item>
          <b-list-group-item
            class="shadow-lg mb-2 rounded"
            v-for="i in info.infoForms"
            :key="i.field_id">
            <b-row>
              <small
                class="text-muted pl-1">{{i.field_name}}</small></b-row>
            <b-row
              class="font-weight-bold pl-2">{{i.field_value}}</b-row></b-list-group-item></b-list-group></b-card></modal-model></div>
</template>

<script>
import ModalModelVue from './ModalModel.vue'

export default {
  name: 'personInfo',
  components: {
    'modal-model': ModalModelVue
  },
  props: {
    id: {
      type: String,
      required: true
    },
    info: {
      type: Object,
      required: false
    }
  }
}
</script>
