<script setup lang="ts">

import InvestmentWidgetElement from '@/components/InvestmentWidgetElement.vue'
</script>

<template>
  <div
    class="p-3 border rounded-lg border-gray-300 dark:border-gray-600 h-96 mb-4">
    <p class="text-base font-medium mb-3">Investments</p>
    <div v-for="i in 3" :key="i">
      <InvestmentWidgetElement class="mb-2"/>
    </div>
  </div>
</template>

<style scoped>

</style>
