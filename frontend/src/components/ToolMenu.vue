<template>
  <div
    id="toolMenu">
    <b-container
      fluid="sm"
      class="bv-example-row">
      <div
        id="toolMenuMobile">
        <b-row
          class="text-left font-weight-bolder my-2">
          {{searchBtnName}}
        </b-row>
        <b-row>
          <slot></slot>
        </b-row>
        <b-row
          class="text-left font-weight-bolder my-2">
          {{typeName}}
        </b-row>
        <b-row>
          <t-dropdown
            variant="outline-success"
            icon-up="folder-check"
            icon-down="folder-plus"
            :title="typeDropdownTitle"
            :value="typeDropdownValue"
            :first-item-title="firstTypeTitle"
            :first-item-value="firstTypeValue"
            :item-list="typeList"
            :select-item-func="typeSelectItemFunc">
          </t-dropdown>
        </b-row>
        <b-row
          class="text-left font-weight-bolder my-2">
          {{timeName}}
        </b-row>
        <b-row>
          <t-dropdown
            variant="outline-info"
            icon-up="calendar-check-fill"
            icon-down="calendar-plus-fill"
            :title="timeDropdownTitle"
            :value="timeDropdownValue"
            :first-item-title="firstTimeTitle"
            :first-item-value="firstTimeValue"
            :item-list="termList"
            :select-item-func="timeSelectItemFunc">
          </t-dropdown>
        </b-row>
      </div>
      <div
        id="toolMenuDesktop">
        <b-row
          class="text-left font-weight-bolder my-2">
          <b-col>
            {{searchBtnName}}
          </b-col>
          <b-col>
            {{typeName}}
          </b-col>
          <b-col>
            {{timeName}}
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <slot></slot>
          </b-col>
          <b-col>
            <t-dropdown
              variant="outline-success"
              icon-up="folder-check"
              icon-down="folder-plus"
              :title="typeDropdownTitle"
              :value="typeDropdownValue"
              :first-item-title="firstTypeTitle"
              :first-item-value="firstTypeValue"
              :item-list="typeList"
              :select-item-func="typeSelectItemFunc">
            </t-dropdown>
          </b-col>
          <b-col>
            <t-dropdown
              variant="outline-info"
              icon-up="calendar-check-fill"
              icon-down="calendar-plus-fill"
              :title="timeDropdownTitle"
              :value="timeDropdownValue"
              :first-item-title="firstTimeTitle"
              :first-item-value="firstTimeValue"
              :item-list="termList"
              :select-item-func="timeSelectItemFunc">
            </t-dropdown>
          </b-col>
        </b-row>
      </div>
    </b-container>
  </div>
</template>

<script>
import ToolDropdownVue from './parts/ToolDropdown.vue'

export default {
  name: 'toolMenu',
  components: {
    't-dropdown': ToolDropdownVue
  },
  props: {
    typeName: {
      type: String,
      required: false,
      default: () => {
        return '课程'
      }
    },
    typeDropdownTitle: {
      type: String,
      required: true
    },
    typeDropdownValue: {
      type: String,
      required: false
    },
    typeSelect: {
      type: Function,
      required: true
    },
    firstTypeTitle: {
      type: String,
      required: false,
      default: () => {
        return '全部课程'
      }
    },
    firstTypeValue: {
      type: String,
      required: false,
      default: () => {
        return ''
      }
    },
    timeName: {
      type: String,
      required: false,
      default: () => {
        return '学期'
      }
    },
    timeDropdownTitle: {
      type: String,
      required: true
    },
    timeDropdownValue: {
      type: String,
      required: false
    },
    timeSelect: {
      type: Function,
      required: true
    },
    firstTimeTitle: {
      type: String,
      required: false,
      default: () => {
        return '全部学期'
      }
    },
    firstTimeValue: {
      type: String,
      required: false,
      default: () => {
        return ''
      }
    },
    searchBtnName: {
      type: String,
      required: false,
      default: () => {
        return '教师'
      }
    },
    typeList: {
      type: Array,
      required: false,
      default: () => {
        return [
          {title: '乐群包', value: '乐群包【1-3年级】'},
          {title: '乐学包', value: '乐学包【1-3年级】'},
          {title: '初中生心智素养课程', value: '初中生心智素养课程【7-9年级】'},
          {title: '积极关系（上册）', value: '积极关系（上册）【4-6年级】'},
          {title: '情绪管理', value: '情绪管理【4-6年级】'}
        ]
      }
    },
    termList: {
      type: Array,
      required: false,
      default: () => {
        let ls = []
        let yearDelta = new Date().getFullYear() - 2019
        for (let i = 0; i <= yearDelta; i++) {
          ls.push(
            {
              title: `${2019 + i}年春季学期`,
              value: `${i * 2}`
            },
            {
              title: `${2019 + i}年秋季学期`,
              value: `${i * 2 + 1}`
            }
          )
        }
        return ls
      }
    }
  },
  computed: {
    term_num_list () {
      let ls = []
      let yearDelta = new Date().getFullYear() - 2019
      for (let i = 0; i <= yearDelta; i++) {
        ls.push(
          {
            title: `${2019 + i}年春季学期`,
            value: `${i * 2}`
          },
          {
            title: `${2019 + i}年秋季学期`,
            value: `${i * 2 + 1}`
          }
        )
      }
      return ls
    }
  },
  methods: {
    typeSelectItemFunc (title, value) {
      this.typeSelect(title, value)
    },
    timeSelectItemFunc (title, value) {
      this.timeSelect(title, value)
    }
  }
}
</script>

<style>
#toolMenuMobile {
  display: none;
}

@media screen and (max-width: 850px) {
  #toolMenuDesktop {
    display: none;
  }
  #toolMenuMobile {
    display: block;
    padding: 0 10px 0 10px;
  }
  #toolMenuMobile > * {
    display: block;
  }
}
</style>
