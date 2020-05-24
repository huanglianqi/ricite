<template>
  <div class="course">
    <h1>{{msg}}</h1>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'course',
  props: {
    msg: String
  }
}
</script>
