<script setup lang="ts">
import TransactionTableElement from '@/views/Dashboard/Elements/TransactionTableElement.vue'
import { useTransactionStore } from '@/stores/transactions'
import { computed, onMounted } from 'vue'

const transactionsStore = useTransactionStore()

onMounted(async () => {
  await transactionsStore.getUserTransactions(1)
})

const transactions = computed(() => transactionsStore.lastMonthExpenses)

</script>

<template>
  <div class="overflow-auto p-3 border rounded-lg border-gray-300 dark:border-gray-600 h-32 md:h-64 mb-4">
    <p class="text-base font-medium">Transaction History</p>
    <section class="dark:bg-gray-900 py-3 sm:py-5">
      <div class=" mx-auto max-w-screen-2xl">
        <div class="relative overflow-hidden bg-white dark:bg-gray-800 sm:rounded-lg">
          <div class="">
            <table 
              v-if="transactions.length"
              class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
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
                <th scope="col" class="px-4 py-3">Type</th>
              </tr>
              </thead>
              <tbody>
                <tr v-if="transactions.length === 0">
                  <td colspan="6" class="text-center py-4">No transactions found</td>
                </tr>
                <TransactionTableElement 
                  v-for="transaction in transactions" 
                  :key="transaction.id"
                  :transaction="transaction">
                </TransactionTableElement>
              </tbody>
            </table>
            <div v-else>

            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>

</style>
