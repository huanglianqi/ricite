<template>
  <div
    id="headImg">
    <b-avatar
      v-b-modal.personInfo
      class="mr-2"
      icon="person-fill"
      variant="white"
      size="2em"
      :button="true"
      rounded
      :src="src"></b-avatar>
    <span
      class="align-bottom">{{name}}</span>
    <modal-model
      :hide-footer="true"
      id="personInfo"
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
            v-for="i in info"
            :key="i.field_id">
            <b-row>
              <small
                class="text-muted pl-1">{{i.field_name}}</small></b-row>
            <b-row
              class="font-weight-bold pl-2">{{i.field_value}}</b-row></b-list-group-item>
          <b-button
            @click="$bvModal.hide('personInfo')"
            class="shadow border-0"
            variant="outline-info">
            <b-icon
              icon="arrows-angle-contract"></b-icon></b-button></b-list-group></b-card></modal-model></div>
</template>

<script>
import ModalModelVue from '../parts/ModalModel.vue'

export default {
  name: 'headImg',
  components: {
    'modal-model': ModalModelVue
  },
  props: {
    name: {
      type: String,
      required: false
    },
    src: {
      type: String,
      required: false
    },
    info: {
      type: Array,
      required: false
    }
  }
}
</script>

<style>
  #headImg:focus {
    outline: none;
  }
</style>
