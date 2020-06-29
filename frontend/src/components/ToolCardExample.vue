<template>
  <div
    id="toolCardExample">
    <b-card
      :border-variant="borderCrl">
      <b-card-header
        v-show="showHeader"
        header-bg-variant="success"
        header-text-variant="light"
        class="mb-4 font-weight-bolder border-0">
        <slot name="header"></slot>
      </b-card-header>
      <b-card-text
        class="text-left font-weight-bolder">
        <slot name="body"></slot>
        <t-progress
          v-show="showProgress"
          :progressMax="progressMax"
          :progressValue="progressValue">
        </t-progress>
        <b-button
          v-show="showBtn"
          block
          variant="outline-success"
          v-b-modal.card-modal
          v-on:click="getData"
          :disabled="noData">
          <b-icon
            :icon="card-checklist"
            class="float-left">
          </b-icon>
          <b-icon
            icon="box-arrow-up-right"
            class="float-right"
            shift-v="-0.5">
          </b-icon>
          {{btnName}}
        </b-button>
      </b-card-text>
    </b-card>
    <t-modal
      id="card-modal">
      <slot name="modal"></slot>
    </t-modal>
  </div>
</template>

<script>
import ToolProgressVue from './ToolProgress.vue'
import ToolModalVue from './ToolModal.vue'

export default {
  name: 'toolCardExample',
  components: {
    't-progress': ToolProgressVue,
    't-modal': ToolModalVue
  },
  props: {
    progressMax: {
      type: Number,
      required: true
    },
    progressValue: {
      type: Number,
      required: true
    },
    getDataFunc: {
      type: Function,
      required: true
    },
    noData: {
      type: Boolean,
      required: true
    },
    btnName: {
      type: String,
      required: true
    },
    borderClr: {
      type: String,
      required: false
    },
    showHeader: {
      type: Boolean,
      required: false,
      default: () => {
        return false
      }
    },
    showBtn: {
      type: Boolean,
      required: false,
      default: () => {
        return false
      }
    },
    showProgress: {
      type: Boolean,
      required: false,
      default: () => {
        return false
      }
    }
  },
  methods: {
    getDate () {
      this.getDateFunc()
    }
  }
}
</script>
