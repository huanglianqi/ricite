<template>
  <div
    id="tianZiGe">
    <div
      class="m-2">
      <slot
        name="leftTop"></slot></div>
    <div
      class="m-2">
      <slot
        name="rightTop"></slot></div>
    <div
      class="m-2">
      <slot
        name="leftBottom"></slot></div>
    <div
      class="m-2">
      <slot
        name="rightBottom"></slot></div></div>
</template>

<style>
#tianZiGe {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

@media screen and (max-width: 850px) {
  #tianZiGe {
    display: block;
  }
}
</style>
