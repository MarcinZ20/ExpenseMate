<script setup lang="ts">
import { useTransactionStore } from '@/stores/transactions';
import { ref } from 'vue'

const transactionStore = useTransactionStore()

const expenseAmount = ref(transactionStore.MonthlyExpenseTotal)
const date = ref(new Date().toDateString())

</script>

<template>
  <div class="border p-3 border-gray-300 rounded-lg dark:border-gray-600 h-32 md:h-48 flex flex-col justify-between">
    <p class="text-base font-medium">Total Expenses</p>
    <div>
      <div class="flex justify-between mt-2 mb-3">
        <p class="text-2xl font-bold">${{ expenseAmount }}</p>
        <span class="bg-red-200 text-red-800 text-xs px-2 py-1 rounded-full inline-flex items-center">
          <svg
            class="w-3 h-3 text-red-800 dark:text-white mr-1"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="none"
            viewBox="0 0 24 24">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4.5V19a1 1 0 0 0 1 1h15M7 10l4 4 4-4 5 5m0 0h-3.207M20 15v-3.207"/>
          </svg>
          <span class="text-xs">9,28%</span>
        </span>
      </div>
      <p class="text-xs text-gray-400">{{ date }}</p>
    </div>
  </div>
</template>

<style scoped>

</style>
