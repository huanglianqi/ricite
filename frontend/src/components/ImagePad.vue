<template>
  <div
    id="imagePad">
    <b-card
      overlay
      border-variant="white"
      :img-src="url">
      <b-card-body>
        <b-button
          size="sm"
          pill
          variant="white"
          v-on:click="likeIt(pic)">
          <b-icon
            variant="danger"
            shift-v="1.75"
            font-scale="1.5"
            :icon="isLike(pic)"></b-icon></b-button></b-card-body></b-card>
  </div>
</template>

<script>
export default {
  name: 'imagePad',
  props: {
    url: {
      type: String,
      required: true
    }
  },
  methods: {
    likeIt (pic) {
      if (pic.like) {
        // modify data remotely
        this.updateLike(pic.id, false)
        // modify data locally
        pic.like = false
      } else {
        // modify data remotely
        this.updateLike(pic.id, true)
        // modify data locally
        pic.like = true
      }
    },
    updateLike (id, bool) {
      Axios
        .patch(
          `flourish/feedback_pic_like_update/${id}`,
          {
            like: bool
          }
        )
        .catch(
          err => {
            console.log(err)
          }
        )
    }
  }
}
</script>

<style>

</style>
