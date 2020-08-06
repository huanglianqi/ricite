<template>
  <div
    id="updateLikeButton">
    <b-button
      block
      variant="outline-danger"
      v-on:click="updateLike(api, id)">
      <b-icon
        :icon="icon"></b-icon></b-button></div>
</template>

<script>
import Axios from 'axios'
export default {
  name: 'updateLikeButton',
  props: {
    likeState: {
      type: Boolean,
      required: true
    },
    id: {
      type: Number,
      required: true
    },
    api: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      icon: '',
      state: null
    }
  },
  mounted () {
    if (this.likeState) {
      this.icon = 'heart-fill'
    } else {
      this.icon = 'heart'
    }
    this.state = this.likeState
  },
  methods: {
    updateLike (api, id) {
      Axios
        .patch(
          `${api}/${id}`,
          {
            like: !this.state
          }
        )
        .then(
          response => {
            this.state = response.data.like
            if (this.state) {
              this.icon = 'heart-fill'
            } else {
              this.icon = 'heart'
            }
          }
        )
        .catch(
          error => {
            console.log(error)
          }
        )
    }
  }
}
</script>
