<template>
  <div class="inventory">
    <h1>{{msg}}</h1>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'inventory',
  props: {
    msg: String
  }
}
</script>
