<template>
  <div
    id="toolCardHead">
    <b-card
      v-show="show"
      border-variant="success">
      <b-card-header
        header-bg-variant="success"
        header-text-variant="light"
        class="mb-4 font-weight-bolder border-0">
        <b-icon
          icon="star-fill"
          class="float-left"
          shift-v="-3">
        </b-icon>
        {{cardName}}
        <b-icon
          icon="star-fill"
          class="float-right"
          shift-v="-3">
        </b-icon>
      </b-card-header>
      <b-card-text
        class="text-left font-weight-bolder">
        <b-icon
          icon="calendar-check-fill"
          variant="success"
          class="mr-3">
        </b-icon>
        {{termTitle}}
      </b-card-text>
      <b-card-text
        class="text-left font-weight-bolder">
        <b-icon
          icon="book"
          variant="success"
          class="mr-3">
        </b-icon>
        {{tagTitle}}
      </b-card-text>
      <t-progress
        :progressMax="progressMax"
        :progressValue="progressValue">
      </t-progress>
      <b-card-text
        class="text-left font-weight-bolder mt-4">
        <b-button
          block
          variant="outline-success"
          v-b-modal.cardHead
          v-on:click="getData"
          :disabled="noData">
          <div
            v-show="!noData">
            <b-icon
              icon="card-checklist"
              class="float-left">
            </b-icon>
            查看{{cardName}}
            <b-icon
              icon="box-arrow-up-right"
              class="float-right"
              shift-v="-0.5">
            </b-icon>
          </div>
          <div
            v-show="noData">
            <b-icon
              icon="card-checklist"
              class="float-left"
              shift-v="-0.5">
            </b-icon>
            暂无{{cardName}}
            <b-icon
              icon="cone-striped"
              class="float-right">
            </b-icon>
          </div>
        </b-button>
      </b-card-text>
    </b-card>
  </div>
</template>

<script>
import ToolProgressVue from './ToolProgress.vue'

export default {
  name: 'toolCardHead',
  components: {
    't-progress': ToolProgressVue
  },
  props: {
    show: {
      type: Boolean,
      required: false
    },
    cardName: {
      type: String,
      required: true
    },
    termTitle: {
      type: String,
      required: true
    },
    tagTitle: {
      type: String,
      required: true
    },
    progressMax: {
      type: Number,
      required: true
    },
    progressValue: {
      type: Number,
      required: true
    },
    noData: {
      type: Boolean,
      required: true
    },
    getDataFunc: {
      type: Function,
      required: true
    }
  },
  methods: {
    getData () {
      this.getDataFunc()
    }
  }
}
</script>
