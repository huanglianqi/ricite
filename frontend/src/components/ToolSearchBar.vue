<template>
  <div
    id="toolSearchBar">
    <b-input-group>
      <b-input-group-prepend>
        <b-button
          variant="light">
          <b-icon
            icon="search">
          </b-icon>
        </b-button>
      </b-input-group-prepend>
      <b-form-input
        class="bg-light border-0"
        :id="searchId"
        :v-model="searchKeyword">
      </b-form-input>
      <b-input-group-append>
        <b-button
          variant="light">
          <b-icon
            icon="X">
          </b-icon>
        </b-button>
      </b-input-group-append>
    </b-input-group>
  </div>
</template>

<script>
export default {
  name: 'toolSearchBar',
  props: {
    searchKeyword: {
      type: String,
      required: false
    },
    searchId: {
      type: String,
      required: false
    },
    inputKeyword: {
      type: Function,
      required: true
    }
  },
  watch: {
    searchKeyword (keyword) {
      this.inputKeyword(keyword)
    }
  }
}
</script>
