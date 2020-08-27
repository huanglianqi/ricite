<template>
  <div
    id="twoColumns">
    <div
      class="m-1">
      <slot
        name="left"></slot></div>
    <div
      class="m-1">
      <slot
        name="right"></slot></div></div>
</template>

<style>
#twoColumns {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

@media screen and (max-width: 850px){
  #twoColumns {
    display: block;
  }
}
</style>
