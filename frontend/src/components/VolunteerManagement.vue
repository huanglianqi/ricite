<template>
  <div
    id="volunteerManagement">
    <t-menu
      :tag-name-dropdown-title="tag_name_title"
      :tag-name-dropdown-value="tag_name_value"
      :tag-name-select-item="tagNameFunc"
      :term-num-dropdown-title="term_num_title"
      :term-num-dropdown-value="term_num_value"
      :term-num-select-item="termNumFunc"
      :search-keyword="search_keyword">
    </t-menu>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import _ from 'lodash'
import ToolMenuVue from './ToolMenu.vue'

export default {
  name: 'volunteerManagement',
  components: {
    't-menu': ToolMenuVue
  },
  data () {
    return {
      tag_name_title: '--请选择课程--',
      tag_name_value: null,
      term_num_title: '--请选择学期--',
      term_num_value: null,
      search_keyword: '',
      list: [],
      fields: [
        {
          key: 'real_name',
          label: '姓名'
        },
        {
          key: 'phone',
          label: '手机号'
        },
        {
          key: 'gender',
          label: '性别',
          sortable: true
        }
      ],
      searchKeyword: ''
    }
  },
  computed: {
    isSearch () {
      if (this.searchKeyword !== '') {
        return true
      } else {
        return false
      }
    }
  },
  watch: {
    searchKeyword (newKeyword, oldKeyword) {
      this.debouncedGetList()
    }
  },
  created () {
    this.debouncedGetList = _.debounce(
      this.getList,
      500
    )
  },
  methods: {
    tagNameFunc (title, value) {
      this.tag_name_title = title
      this.tag_name_value = value
    },
    termNumFunc (title, value) {
      this.term_num_title = title
      this.term_num_value = value
    },
    getList () {
      if (this.searchKeyword === '') {
        this.getFullList()
      } else {
        this.getSearchList()
      }
    },
    getFullList () {
      axios
        .get('api/teacher/')
        .then(
          res => {
            this.list = res.data
          }
        )
        .catch(
          err => {
            console.log(err)
          }
        )
    },
    getSearchList () {
      axios
        .get(
          'api/teacher/?search^',
          {
            params: {
              name: this.searchKeyword
            }
          }
        )
        .then(
          res => {
            this.list = res.data
          }
        )
        .catch(
          err => {
            console.log(err)
          }
        )
    },
    renew () {
      console.log('Im renew function!')
    },
    searchReset () {
      this.searchKeyword = ''
    }
  }
}
</script>
