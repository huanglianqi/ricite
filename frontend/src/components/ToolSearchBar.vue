<template>
  <div
    id="toolSearchBar">
    <b-form
      @submit="searchFunc(keyword)"
      @reset="reset(keyword)">
      <b-input-group>
        <b-input-group-prepend>
          <b-button
            variant="light"
            type="submit">
            <b-icon
              icon="search">
            </b-icon>
          </b-button>
        </b-input-group-prepend>
        <b-form-input
          class="bg-light border-0"
          :id="id"
          v-model="keyword">
        </b-form-input>
        <b-input-group-append>
          <b-button
            variant="light"
            type="reset">
            <b-icon
              icon="X">
            </b-icon>
          </b-button>
        </b-input-group-append>
      </b-input-group>
    </b-form>
  </div>
</template>

<script>
export default {
  name: 'toolSearchBar',
  props: {
    id: {
      type: String,
      required: true
    },
    keyword: {
      type: String,
      required: true
    },
    search: {
      type: Function,
      required: true
    }
  },
  methods: {
    searchFunc (keyword) {
      this.search(keyword)
    },
    reset () {
      this.keyword = ''
    }
  }
}
</script>
