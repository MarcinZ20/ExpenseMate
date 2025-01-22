<script setup lang="ts">
import ApexCharts from 'apexcharts';

const options = {
  chart: {
    type: 'area',
    toolbar: {
      show: false,
    },
  },
  colors: ['#9b5de5', '#e6aace', '#3fa79a', '#f4b539'],
  xaxis: {
    type: 'datetime',
  },
  yaxis: {
    labels: {
      formatter: function (value: number) {
        return value / 1000 + 'k'
      }
    }
  },
  legend: {
    show: true,
    position: 'top',
    horizontalAlign: 'right',
    offsetX: 0,
    offsetY: 0,
  },
  stroke: {
    width: 4,
    curve: 'smooth',
  },
  grid: {
    show: true,
    strokeDasharray: 4,
    padding: {
      left: 2,
      right: 2,
      top: 0,
      bottom: 0,
    },
  },
  tooltip: {
    enabled: true,
    x: {
      show: false,
    },
  },
  fill: {
    type: 'gradient',
    gradient: {
      shadeIntensity: 1,
      opacityFrom: 0.7,
      opacityTo: 0.9,
      stops: [0, 90, 100],
    },
  },
  dataLabels: {
    enabled: false,
  },
}

const series = [
  {
    name: 'Income',
    type: 'area',
    data: [
      [1486684800000, 3400],
      [1486771200000, 4300],
      [1486857600000, 3100] ,
      [1486944000000, 4300],
      [1487030400000, 3300],
      [1487116800000, 5200]
    ]
  },
  {
    name: 'Expenses',
    type: 'area',
    data: [
      [1486684800000, 1200],
      [1486771200000, 3300],
      [1486857600000, 5100] ,
      [1486944000000, 2300],
      [1487030400000, 1300],
      [1487116800000, 3200]
    ]
  }

]

const chart = new ApexCharts(document.querySelector('#area-chart'), options)
chart.render()

</script>

<template>
  <div class="p-3 border rounded-lg border-gray-300 dark:border-gray-600 h-96 mb-4 col-span-2">
   <div class="flex justify-between items-center">
    <div class="inline-flex items-center justify-between gap-3">
      <p class="text-base font-medium">General Budget</p>
      <button>
        <span>
          <svg class="w-4 h-4 text-gray-400 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
           <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.651 7.65a7.131 7.131 0 0 0-12.68 3.15M18.001 4v4h-4m-7.652 8.35a7.13 7.13 0 0 0 12.68-3.15M6 20v-4h4"/>
          </svg>
        </span>
      </button>
   </div>
   <div>
     <button>
       <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
         <path stroke="currentColor" stroke-linecap="round" stroke-width="2" d="M6 12h.01m6 0h.01m5.99 0h.01"/>
       </svg>
     </button>
   </div>
  </div>

<!--    CHART     -->
    <div class="">
      <div class="flex justify-between items-center">
<!--        Left side     -->
        <div class="flex justify-between mt-2 mb-3 gap-4 items-center">
            <p class="text-2xl font-bold">$25,023.79</p>
            <span class="bg-green-200 text-green-600 text-xs px-2 py-1 rounded-full inline-flex items-center">
          <svg
            class="w-3 h-3 text-green-600 dark:text-white mr-1"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="none"
            viewBox="0 0 24 24">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4.5V19a1 1 0 0 0 1 1h15M7 14l4-4 4 4 5-5m0 0h-3.207M20 9v3.207"/>
          </svg>
          <span class="text-xs">17,28%</span>
        </span>
          </div>
<!--        Right side    -->
        <div>
          <button
            id="dropdownDefaultButton"
            data-dropdown-toggle="lastDaysdropdown"
            data-dropdown-placement="bottom"
            type="button"
            class="px-3 py-2 inline-flex items-center text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700"
          >
            Last week
            <svg
              class="w-2.5 h-2.5 ms-2.5"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 10 6"
            >
              <path
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="m1 1 4 4 4-4"
              />
            </svg>
          </button>
          <div
            id="lastDaysdropdown"
            class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700"
          >
            <ul
              class="py-2 text-sm text-gray-700 dark:text-gray-200"
              aria-labelledby="dropdownDefaultButton"
            >
              <li>
                <a
                  href="#"
                  class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                >Yesterday</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                >Today</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                >Last 7 days</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                >Last 30 days</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                >Last 90 days</a
                >
              </li>
            </ul>
          </div>
        </div>
      </div>
      <apexchart
        id="area-chart"
        :options="options"
        :series="series"
      height="250">
      </apexchart>
    </div>
  </div>
</template>

<style scoped></style>
