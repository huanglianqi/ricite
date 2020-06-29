<template>
  <div
    id="toolDropdown">
    <b-dropdown
      block
      no-caret
      :variant="dropdownVariant">
      <template
        v-slot:button-content>
        <div
          v-on:click="toolDropdown_down=true">
          <b-icon
            :icon="iconUp"
            class="float-left"
            v-show="!toolDropdown_down">
          </b-icon>
          <b-icon
            :icon="iconDown"
            class="float-left"
            v-show="toolDropdown_down">
          </b-icon>
          {{title}}
          <b-icon
            class="float-right"
            icon="caret-left-fill"
            v-show="!toolDropdown_down">
          </b-icon>
          <b-icon
            class="float-right"
            icon="caret-down-fill"
            v-show="toolDropdown_down">
          </b-icon>
        </div>
      </template>
      <b-dropdown-item
        v-on:click="selectItem(firstItemTitle, firstItemValue)">
        {{firstItemTitle}}
      </b-dropdown-item>
      <b-dropdown-divider></b-dropdown-divider>
      <b-dropdown-item
        v-for="item in itemList"
        v-bind:key="item.title"
        v-on:click="selectItem(item.title, item.value)">
        {{item.title}}
      </b-dropdown-item>
    </b-dropdown>
  </div>
</template>

<script>
export default {
  name: 'toolDropdown',
  props: {
    dropdownVariant: {
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
      required: true
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
      toolDropdown_down: false
    }
  },
  mounted () {
    this.$root.$on(
      'bv::dropdown::hide',
      () => {
        this.toolDropdown_down = false
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
