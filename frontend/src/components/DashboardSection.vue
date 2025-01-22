<script setup lang="ts">
import IncomeWidget from '@/components/IncomeWidget.vue'
import ExpenseWidget from '@/components/ExpenseWidget.vue'
import ProfitWidget from '@/components/ProfitWidget.vue'
import GeneralBudgetWidget from '@/components/GeneralBudgetWidget.vue'
import InvestmentsWidget from '@/components/InvestmentsWidget.vue'
</script>

<template>
  <main class="p-4 md:ml-64 h-auto pt-20">
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-4">
      <income-widget/>
      <expense-widget/>
      <profit-widget/>
    </div>
    <div class="grid grid-cols-3 gap-4 mb-4">
      <general-budget-widget/>
      <investments-widget/>
    </div>
    <div
      class="border-2 rounded-lg border-gray-300 dark:border-gray-600 h-32 md:h-64 mb-4"
    ></div>
  </main>
</template>

<style scoped></style>
