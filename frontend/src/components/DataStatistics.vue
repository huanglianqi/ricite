<template>
  <div
    id="dataStatistics">
    {{applyNum.teacher}}
    {{applyNum.student}}
  </div>
</template>

<script>

export default {
  name: 'dataStatistics',
  data () {
    return {
      applyNum: {
        teacher: 0,
        student: 0
      }
    }
  }
}
</script>

<style>
</style>
