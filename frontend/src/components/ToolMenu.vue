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
          教师
        </b-row>
        <b-row>
          <t-searchBar
            :search-keyword="searchKeyword"
            search-id="mobile-search"
            :input-keyword="inputKeywordFunc">
          </t-searchBar>
        </b-row>
        <b-row
          class="text-left font-weight-bolder my-2">
          课程
        </b-row>
        <b-row>
          <t-dropdown
            dropdown-variant="outline-success"
            icon-up="folder-check"
            icon-down="folder-plus"
            :title="tagNameDropdownTitle"
            :value="tagNameDropdownValue"
            first-item-title="全部课程"
            first-item-value=""
            :item-list="tagNameItemList"
            :select-item-func="tagNameSelectItemFunc">
          </t-dropdown>
        </b-row>
        <b-row
          class="text-left font-weight-bolder my-2">
          学期
        </b-row>
        <b-row>
          <t-dropdown
            dropdown-variant="outline-info"
            icon-up="calendar-check-fill"
            icon-down="calendar-plus-fill"
            :title="termNumDropdownTitle"
            :value="termNumDropdownValue"
            first-item-title="全部学期"
            first-item-value=""
            :item-list="termNumItemList"
            :select-item-func="termNumSelectItemFunc">
          </t-dropdown>
        </b-row>
      </div>
      <div
        id="toolMenuDesktop">
        <b-row
          class="text-left font-weight-bolder my-2">
          <b-col>
            教师
          </b-col>
          <b-col>
            课程
          </b-col>
          <b-col>
            学期
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <t-searchBar
              :search-keyword="searchKeyword"
              search-id="desktop-search"
              :input-keyword="inputKeywordFunc">
            </t-searchBar>
          </b-col>
          <b-col>
            <t-dropdown
              dropdown-variant="outline-success"
              icon-up="folder-check"
              icon-down="folder-plus"
              :title="tagNameDropdownTitle"
              :value="tagNameDropdownValue"
              first-item-title="全部课程"
              first-item-value=""
              :item-list="tagNameItemList"
              :select-item-func="tagNameSelectItemFunc">
            </t-dropdown>
          </b-col>
          <b-col>
            <t-dropdown
              dropdown-variant="outline-info"
              icon-up="calendar-check-fill"
              icon-down="calendar-plus-fill"
              :title="termNumDropdownTitle"
              :value="termNumDropdownValue"
              first-item-title="全部学期"
              first-item-value=""
              :item-list="termNumItemList"
              :select-item-func="termNumSelectItemFunc">
            </t-dropdown>
          </b-col>
        </b-row>
      </div>
    </b-container>
  </div>
</template>

<script>
import ToolDropdownVue from './ToolDropdown.vue'
import ToolSearchBarVue from './ToolSearchBar.vue'

export default {
  name: 'toolMenu',
  components: {
    't-dropdown': ToolDropdownVue,
    't-searchBar': ToolSearchBarVue
  },
  props: {
    tagNameDropdownTitle: {
      type: String,
      required: true
    },
    tagNameDropdownValue: {
      type: String,
      required: false
    },
    tagNameSelectItem: {
      type: Function,
      required: true
    },
    termNumDropdownTitle: {
      type: String,
      required: true
    },
    termNumDropdownValue: {
      type: String,
      required: false
    },
    termNumSelectItem: {
      type: Function,
      required: true
    },
    searchKeyword: {
      type: String,
      required: false
    },
    tagNameItemList: {
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
    termNumItemList: {
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
    },
    inputKeyword: {
      type: Function,
      required: true
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
    term_num_list_ () {
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
    },
    tagNameSelectItemFunc (title, value) {
      this.tagNameSelectItem(title, value)
    },
    termNumSelectItemFunc (title, value) {
      this.termNumSelectItem(title, value)
    },
    inputKeywordFunc (keyword) {
      this.inputKeyword(keyword)
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
