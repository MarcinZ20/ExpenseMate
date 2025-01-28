<script setup lang="ts">

import TransactionTableElement from '@/components/TransactionTableElement.vue'
</script>

<template>
  <div class="p-3 border rounded-lg border-gray-300 dark:border-gray-600 h-32 md:h-64 mb-4">
    <p class="text-base font-medium">Transaction History</p>
    <section class="dark:bg-gray-900 py-3 sm:py-5">
      <div class=" mx-auto max-w-screen-2xl">
        <div class="relative overflow-hidden bg-white dark:bg-gray-800 sm:rounded-lg">
          <div class="overflow-x-auto overflow-y-scroll">
            <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
              <thead class="text-xs text-gray-400  dark:bg-gray-700 dark:text-gray-400">
              <tr>
                <th scope="col" class="p-4">
                  <div class="flex items-center">
                    <input id="checkbox-all" type="checkbox" class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                    <label for="checkbox-all" class="sr-only">checkbox</label>
                  </div>
                </th>
                <th scope="col" class="px-4 py-3">Transaction</th>
                <th scope="col" class="px-4 py-3">Amount</th>
                <th scope="col" class="px-4 py-3">Category</th>
                <th scope="col" class="px-4 py-3">Date</th>
                <th scope="col" class="px-4 py-3">Method</th>
              </tr>
              </thead>
              <tbody v-for="i in 3" :key="i">
                <transaction-table-element :transaction="i"></transaction-table-element>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>

</style>
