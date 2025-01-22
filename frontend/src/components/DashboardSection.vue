<script setup lang="ts">
import IncomeWidget from '@/components/IncomeWidget.vue'
import ExpenseWidget from '@/components/ExpenseWidget.vue'
import ProfitWidget from '@/components/ProfitWidget.vue'
import GeneralBudgetWidget from '@/components/GeneralBudgetWidget.vue'
import InvestmentsWidget from '@/components/InvestmentsWidget.vue'
import TransactionsWidget from '@/components/TransactionsWidget.vue'
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
    <transactions-widget/>
  </main>
</template>

<style scoped></style>
