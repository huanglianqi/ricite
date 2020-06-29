<template>
  <div
    id="toolCardItem">
    <b-card>
      <b-card-text
        class="text-left font-weight-bolder mt-4">
        <b-icon
          icon="person-fill"
          variant="success"
          class="mr-3">
        </b-icon>
        {{personName}}
      </b-card-text>
      <b-card-text
        class="text-left font-weight-bolder">
        <b-icon
          icon="calendar-check-fill"
          varaint="success"
          class="mr-3">
        </b-icon>
        {{termNumTitle}}
      </b-card-text>
      <b-card-text
        class="text-left font-weight-bolder mb-3">
        <b-icon
          icon="book"
          variant="success"
          class="mr-3">
        </b-icon>
        {{tagNameTitle}}
      </b-card-text>
      <b-card-text
        class="text-left font-weight-bolder mt-3">
        <t-progress
          :progressMax="progressMax"
          :progressValue="progressValue">
        </t-progress>
      </b-card-text>
      <b-card-text
        class="mt-4 mb-2">
        <b-button
          block
          variant="outline-success"
          v-b-modal.cardItem
          v-on:click="getDate">
          <b-icon
            icon="card-checklist"
            class="float-left">
          </b-icon>
          {{btnName}}
          <b-icon
            icon="box-arrow-up-right"
            class="float-right"
            shift-v="-0.9">
          </b-icon>
        </b-button>
      </b-card-text>
    </b-card>
  </div>
</template>

<script>
import ToolProgressVue from './ToolProgress.vue'

export default {
  name: 'toolCardItem',
  props: {
    personName: {
      type: String,
      required: false
    },
    termNumTitle: {
      type: String,
      required: true
    },
    tagNameTitle: {
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
    btnName: {
      type: String,
      required: true
    }
  },
  components: {
    't-progress': ToolProgressVue
  }
}
</script>
