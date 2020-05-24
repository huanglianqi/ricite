<template>
  <div>
    <b-tabs
      pills
      card
      small
      fill
      align="center"
      active-nav-item-class="bg-success text-white font-weight-bold"
      nav-wrapper-class="bg-white">
      <b-tab
        title="社群管理"
        active>
        <Community msg="Community Management"/>
      </b-tab>
      <b-tab
        title="课程申请">
        <Course msg="Course Apply Management"/>
      </b-tab>
      <b-tab
        title="库存管理">
        <Inventory msg="Inventory Control"/>
      </b-tab>
      <b-tab
        title="数据图表">
        <Chart msg="Chart Presentation"/>
      </b-tab>
    </b-tabs>
    <Nav msg="Navigration"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Community from '@/components/Community.vue'
import Course from '@/components/Course.vue'
import Inventory from '@/components/Inventory.vue'
import Chart from '@/components/Chart.vue'

export default {
  name: 'home',
  components: {
    Community,
    Course,
    Inventory,
    Chart
  }
}
</script>
