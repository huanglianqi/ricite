<template>
  <div id="community">
    <b-button-group
      class="d-flex justify-content-center">
      <b-button
          variant="outline-success"
          v-on:click="renew">
          <b-icon
            icon="arrow-clockwise"
            scale="1.25"
            shift-v="1.25"
            aria-hidden="true">
          </b-icon>
          刷新
        </b-button>
        <b-button
          variant="outline-info"
          v-b-toggle.filterMenu>
          <b-icon
            icon="funnel"
            scale="1.25"
            shift-v="1.25"
            aria-hidden="true">
          </b-icon>
          筛选
        </b-button>
        <b-button
          variant="outline-dark"
          v-b-toggle.searchMenu>
          <b-icon
            icon="search"
            scale="1.25"
            shift-v="1.25"
            aria-hidden="true">
          </b-icon>
          搜索
        </b-button>
    </b-button-group>
    <b-collapse
      id="filterMenu">
      filterMenu
    </b-collapse>
    <b-collapse
      id="searchMenu"
      class="mt-10">
      <b-form
        class="mt-2"
        @reset="searchReset">
        <b-input-group>
          <b-form-input
            id="search"
            v-model="searchKeyword"
            required
            trim
            placeholder="输入姓名、手机号或其他信息，进行搜索">
          </b-form-input>
          <b-button
            type="reset"
            variant="outline-danger">
            <b-icon
              icon="arrow-clockwise"
              class="mr-2">
            </b-icon>
            重置
          </b-button>
        </b-input-group>
      </b-form>
    </b-collapse>
    <b-table
      striped
      hover
      small
      :items="list"
      :fields="fields">
    </b-table>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import _ from 'lodash'

export default {
  name: 'community',
  data () {
    return {
      list: [],
      fields: [
        {
          key: 'name',
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
      this.getList, 500
    )
  },
  methods: {
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
