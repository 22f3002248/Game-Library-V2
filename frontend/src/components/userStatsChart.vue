<template>
  <div
    class="flex flex-col items-center justify-center min-h-screen space-y-12 mt-12"
  >
    <!-- Row 1 -->
    <div class="flex flex-wrap justify-center items-center gap-8">
      <div class="chart-container">
        <h4 class="chart-title">Purchased Only vs Purchased & Completed</h4>
        <Doughnut :data="purchasedOnlyChartData" :options="chartOptions" />
      </div>
      <div class="chart-container">
        <h4 class="chart-title">Subscribed Only vs Subscribed & Completed</h4>
        <Pie :data="subscribedOnlyChartData" :options="chartOptions" />
      </div>
    </div>

    <!-- Row 2 -->
    <div class="flex flex-wrap justify-center items-center gap-8">
      <div class="chart-container">
        <h4 class="chart-title">Completed Games vs Total</h4>
        <Bar :data="completedChartData" :options="chartOptions" />
      </div>
      <div class="chart-container">
        <h4 class="chart-title">Purchased + Subscribed vs Completed</h4>
        <PolarArea :data="subAndPurChartData" :options="chartOptions" />
      </div>
    </div>
  </div>
</template>

<script setup>
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  BarElement,
  CategoryScale,
  LinearScale,
  RadialLinearScale,
} from 'chart.js'
import { Doughnut, Pie, Bar, PolarArea } from 'vue-chartjs'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  ArcElement,
  BarElement,
  CategoryScale,
  LinearScale,
  RadialLinearScale
)

const props = defineProps({
  stats: {
    type: Object,
    required: true,
  },
})

// 1. Purchased only vs purchased_completed
const purchasedOnlyChartData = {
  labels: ['Purchased Only', 'Purchased & Completed'],
  datasets: [
    {
      data: [props.stats.purchased, props.stats.purchased_completed],
      backgroundColor: ['#3b82f6', '#10b981'],
    },
  ],
}

// 2. Subscribed only vs subscribed_completed
const subscribedOnlyChartData = {
  labels: ['Subscribed Only', 'Subscribed & Completed'],
  datasets: [
    {
      data: [props.stats.subscribed, props.stats.subscribed_completed],
      backgroundColor: ['#f59e0b', '#84cc16'],
    },
  ],
}

// 3. Completed vs total
const completedChartData = {
  labels: ['Completed Games', 'Remaining Games'],
  datasets: [
    {
      label: 'Games',
      data: [props.stats.completed, props.stats.total - props.stats.completed],
      backgroundColor: ['#22d3ee', '#334155'],
    },
  ],
}

// 4. Purchased + Subscribed vs their completion
const subAndPurChartData = {
  labels: ['Purchased & Subscribed', 'Purchased & Subscribed & Completed'],
  datasets: [
    {
      data: [
        props.stats.purchased_and_subscribed,
        props.stats.purchased_and_subscribed_completed,
      ],
      backgroundColor: ['#c084fc', '#ec4899'],
    },
  ],
}

const chartOptions = {
  responsive: true,
  plugins: {
    legend: {
      position: 'bottom',
      labels: {
        color: '#fff',
      },
    },
    tooltip: {
      callbacks: {
        label: function (context) {
          return `${context.label}: ${context.raw} games`
        },
      },
    },
  },
  scales: {
    x: {
      ticks: { color: '#fff' },
      grid: { color: '#334155' },
    },
    y: {
      beginAtZero: true,
      ticks: { color: '#fff' },
      grid: { color: '#334155' },
    },
  },
}
</script>
<style scoped>
.chart-container {
  @apply bg-gray-900 shadow-lg p-6 rounded-lg flex flex-col items-center justify-center pt-10;
  width: 600px; /* 🔧 change this to resize chart */
  height: 400px; /* 🔧 change this to resize chart */
  border: 2px solid #ababab; /* Optional: add border for better visibility */
  border-radius: 10px; /* Optional: add border radius for better visibility */
}

.chart-title {
  @apply text-xl font-bold mb-2 text-white text-center;
}

.separator {
  @apply border-gray-600 w-full;
  border-top-width: 2px;
}
</style>
