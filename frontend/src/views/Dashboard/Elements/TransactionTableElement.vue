<script setup lang="ts">
import { Transaction } from '@/models/Transaction';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faMoneyCheckDollar, faMugHot, faCarSide, faCartShopping, faStaffSnake, faUserGraduate, faMoneyBillTrendUp, faBoxArchive} from '@fortawesome/free-solid-svg-icons';
import { capitalize } from '@/helpers/helpers';

const props = defineProps<{
  transaction: Transaction
}>()

const transactionIcons: Record<string, any> = {
  food: faMugHot,
  bills: faMoneyCheckDollar,
  transport: faCarSide,
  shopping: faCartShopping,
  health: faStaffSnake,
  education: faUserGraduate,
  savings: faMoneyBillTrendUp,
  other: faBoxArchive
}

const getTransactionIcon = (category: string) => {
  return transactionIcons[category] || faBoxArchive;
}

</script>

<template>
  <tr class="border-b dark:border-gray-600 hover:bg-gray-100 dark:hover:bg-gray-700">
    <td class="w-4 px-4 py-3">
      <div class="flex items-center">
        <input id="checkbox-table-search-1" type="checkbox" onclick="event.stopPropagation()" class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
        <label for="checkbox-table-search-1" class="sr-only">checkbox</label>
      </div>
    </td>
    <th scope="row" class="px-4 py-2 font-medium text-gray-900 whitespace-nowrap dark:text-white">
      <p class="ml-2">{{ transaction._description }}</p>
    </th>
    <td class="px-4 py-2">
      <span class="bg-primary-100 text-primary-800 text-xs font-medium px-2 py-0.5 rounded dark:bg-primary-900 dark:text-primary-300">${{ transaction.amount }}</span>
    </td>
    <td class="px-4 py-2 font-normal text-gray-500 whitespace-nowrap dark:text-white">
      <div class="flex items-center">
        <div class="flex justify-center items-center inline-block w-6 h-6 mr-2 bg-transparent rounded-full">
          <FontAwesomeIcon :icon="getTransactionIcon(transaction.category)"/> 
        </div>
        {{ capitalize(transaction.category) }}
      </div>
    </td>
    <td class="px-4 py-2 font-medium text-gray-500 whitespace-nowrap dark:text-white">{{ transaction.date.toDateString() }}, {{ transaction.time }}</td>
    <td class="px-4 py-2 font-medium text-gray-900 whitespace-nowrap dark:text-white">{{ transaction.type }}</td>
  </tr>
</template>

<style scoped>

</style>
