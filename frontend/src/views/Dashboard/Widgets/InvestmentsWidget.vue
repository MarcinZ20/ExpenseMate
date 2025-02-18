<script setup lang="ts">

import InvestmentWidgetElement from '@/views/Dashboard/Elements/InvestmentWidgetElement.vue'
</script>

<template>
  <div
    class="p-3 border rounded-lg border-gray-300 dark:border-gray-600 h-72 lg:h-96 mb-4 col-span-3 lg:col-span-1 overflow-auto">
    <p class="text-base font-medium mb-3">Investments</p>
    <div v-for="i in 3" :key="i">
      <InvestmentWidgetElement class="mb-2"/>
    </div>
    <button class="flex w-72 gap-2 justify-center items-center rounded-lg border border-gray-200 p-3 shadow-sm dark:border-gray-700 dark:bg-gray-800 md:p-3">
      <div class="text-white flex justify-center rounded-full bg-green-400 w-5 h-5 items-center">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
          <path fill="currentColor" d="M12.75 7a.75.75 0 0 0-1.5 0v4.25H7a.75.75 0 0 0 0 1.5h4.25V17a.75.75 0 0 0 1.5 0v-4.25H17a.75.75 0 0 0 0-1.5h-4.25z" />
        </svg>
      </div>
      New Investment
    </button>
  </div>
</template>

<style scoped>

</style>
