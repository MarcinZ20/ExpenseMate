<script setup lang="ts">
import IncomeWidget from '@/views/Dashboard/Widgets/IncomeWidget.vue'
import ExpenseWidget from '@/views/Dashboard/Widgets/ExpenseWidget.vue'
import ProfitWidget from '@/views/Dashboard/Widgets/ProfitWidget.vue'
import GeneralBudgetWidget from '@/views/Dashboard/Widgets/GeneralBudgetWidget.vue'
import InvestmentsWidget from '@/views/Dashboard/Widgets/InvestmentsWidget.vue'
import TransactionsWidget from '@/views/Dashboard/Widgets/TransactionsWidget.vue'
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
