<template>
  <div
    id="toolCardGroup">
    <b-card-group
      id="three-cards"
      columns
      class="m-4">
      <slot></slot>
    </b-card-group>
  </div>
</template>

<script>

export default {
  name: 'toolCardGroup'
}
</script>

<style>
#three-cards {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}

@media screen and (max-width: 850px) {
  #three-cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
}

@media screen and (max-width: 500px) {
  #three-cards {
    display: block;
  }
}
</style>
