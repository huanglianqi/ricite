<template>
  <div id="threeColumns">
    <b-container
      fluid="sm"
      class="bv-example-row">
      <div
        id="mobile">
        <b-row
          class="text-left font-weight-bolder my-2">
          {{firstColumnTitle}}
        </b-row>
        <b-row>
          <slot
            name="firstColumn"></slot>
        </b-row>
        <b-row
          class="text-left font-weight-bolder my-2">
          {{secondColumnTitle}}
        </b-row>
        <b-row>
          <slot name="secondColumn"></slot>
        </b-row>
        <b-row
          class="text-left font-weight-bolder my-2">
          {{thirdColumnTitle}}
        </b-row>
        <b-row>
          <slot name="thirdColumn"></slot>
        </b-row>
      </div>
      <div
        id="desktop">
        <b-row
          class="text-left font-weight-bolder my-2">
          <b-col>
            {{firstColumnTitle}}
          </b-col>
          <b-col>
            {{secondColumnTitle}}
          </b-col>
          <b-col>
            {{thirdColumnTitle}}
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <slot name="firstColumn"></slot>
          </b-col>
          <b-col>
            <slot name="secondColumn"></slot>
          </b-col>
          <b-col>
            <slot name="thirdColumn"></slot>
          </b-col>
        </b-row>
      </div>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'threeColumns',
  props: {
    firstColumnTitle: {
      type: String,
      required: true
    },
    secondColumnTitle: {
      type: String,
      required: true
    },
    thirdColumnTitle: {
      type: String,
      required: true
    }
  }
}
</script>

<style>
#mobile {
  display: none;
}

@media screen and (max-width: 850px) {
  #desktop {
    display: none;
  }
  #mobile {
    display: block;
    padding: 0 10px 0 10px;
  }
  #mobile > * {
    display: block;
  }
}
</style>
