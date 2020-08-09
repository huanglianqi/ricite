<template>
  <div
    id="toolDropdown">
    <b-dropdown
      toggle-class="shadow-sm border-white border-0 p-2"
      block
      no-caret
      menu-class="w-100"
      :variant="variant">
      <template
        v-slot:button-content>
        <div
          v-on:click="toolDropdownDown=true">
          <b-icon
            :icon="iconUp"
            shift-v="-1"
            class="float-left mr-2"
            v-show="!toolDropdownDown"></b-icon>
          <b-icon
            :icon="iconDown"
            shift-v="-1"
            class="float-left mr-2"
            v-show="toolDropdownDown"></b-icon>
          {{title}}
          <b-icon
            class="float-right ml-1"
            shift-v="-1"
            icon="three-dots"
            v-show="!toolDropdownDown"></b-icon>
          <b-icon
            class="float-right ml-1"
            icon="x"
            v-show="toolDropdownDown"></b-icon></div></template>
      <b-dropdown-item
        v-on:click="selectItem(firstItemTitle, firstItemValue)">
        {{firstItemTitle}}
      </b-dropdown-item>
      <b-dropdown-divider></b-dropdown-divider>
      <b-dropdown-item
        v-for="item in itemList"
        v-bind:key="item.title"
        v-on:click="selectItem(item.title, item.value)">
        {{item.title}}</b-dropdown-item></b-dropdown>
  </div>
</template>

<script>
export default {
  name: 'toolDropdown',
  props: {
    variant: {
      type: String,
      required: true
    },
    iconUp: {
      type: String,
      required: true
    },
    iconDown: {
      type: String,
      required: true
    },
    title: {
      type: String,
      required: true
    },
    value: {
      type: String,
      required: false
    },
    firstItemTitle: {
      type: String,
      required: false
    },
    firstItemValue: {
      type: String,
      required: false
    },
    itemList: {
      type: Array,
      required: false
    },
    selectItemFunc: {
      type: Function,
      required: true
    }
  },
  data () {
    return {
      toolDropdownDown: false
    }
  },
  mounted () {
    this.$root.$on(
      'bv::dropdown::hide',
      () => {
        this.toolDropdownDown = false
      }
    )
  },
  methods: {
    selectItem (title, value) {
      this.selectItemFunc(title, value)
    }
  }
}
</script>
