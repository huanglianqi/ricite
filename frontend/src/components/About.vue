<template>
  <div>
    <b-tabs
      pills
      card
      small
      fill
      align="center"
      active-nav-item-class="bg-success text-white font-weight-bold"
      nav-wrapper-class="bg-light">
      <b-tab
        title="关于我们"
        active>
        <AboutUs/>
      </b-tab>
      <b-tab
        title="关于网站">
      </b-tab>
      <b-tab
        title="关于作者">
      </b-tab>
    </b-tabs>
  </div>
</template>

<script>
// @ is an alias to /src
import AboutUs from '@/components/AboutUs.vue'

export default {
  name: 'about',
  components: {
    AboutUs
  }
}
</script>
