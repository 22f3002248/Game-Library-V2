<template>
  <div class="flex h-screen">
    <navbarCompVertical />
    <div class="flex-1 p-5 border border-accent-500 m-5 rounded-md">
      <Bar :data="data" :options="options" />
    </div>

    <div class="flex-2 p-5 w-[400px]">
      <div class="border border-white p-5 rounded-md">
        <p class="font-bold text-xl text-accent">Top 3 Games by Downloads</p>
        <hr />
        <br />
        <div
          v-for="(game, index) in top3"
          :key="index"
          class="shadow-lg flex flex-col"
        >
          <div class="border border-white mb-3 p-2 rounded-md">
            <div class="flex gap-5">
              <span>{{ index + 1 }}.</span>
              <img :src="game.poster" alt="game poster" class="w-14 h-14" />
              <span class="font-bold text-md"
                >{{ game.title }} <br />
                <span class="font-bold text-sm"
                  >Downloads:
                  {{
                    // Use the toLocaleString method to add suffixes to the number
                    game.no_of_downloads.toLocaleString('en-US', {
                      // add suffixes for thousands, millions, and billions
                      // the maximum number of decimal places to use
                      maximumFractionDigits: 2,
                      // specify the abbreviations to use for the suffixes
                      notation: 'compact',
                      compactDisplay: 'short',
                    })
                  }}</span
                >
              </span>
            </div>
          </div>
        </div>
      </div>
      <br />

      <div class="border border-white p-5 rounded-md"  style="overflow: auto; height: 320px;">
        <p class="font-bold text-xl text-accent">Top 5 Games by Rating</p>
        <hr />
        <br />
        <div
          v-for="(game, index) in top5"
          :key="index"
          class="shadow-lg flex flex-col"
        >
          <div class="border border-white rounded-md mb-3 p-2 ">
            <div class="flex gap-5">
              <span>{{ index + 1 }}.</span>
              <img :src="game.poster" alt="game poster" class="w-14 h-14" />
              <span class="font-bold text-md"
                >{{ game.title }} <br />
                <span class="font-bold text-sm">Rating: {{ game.rating }}</span>
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// JS
import axios from 'axios'
import navbarCompVertical from '../components/navbarCompVertical.vue'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from 'chart.js'
import { Bar } from 'vue-chartjs'
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

export default {
  name: 'adminDash',
  components: {
    navbarCompVertical,
    Bar,
  },
  data() {
    return {
      games: [],
      labels: [],
      data_downloads: [],
      top3: [],
      top5: [],
      options: {
        responsive: true,
        maintainAspectRatio: false, // Makes the chart responsive to window size
        plugins: {
          title: {
            display: true,
            text: 'Game Downloads',
            font: {
              size: 30,
              weight: 'bold',
            },
            color: '#1DCD9F', // Title color
          },
          tooltip: {
            backgroundColor: 'rgba(0, 0, 0, 0.7)', // Tooltip background color
            bodyColor: 'white', // Tooltip text color
          },
        },
        scales: {
          x: {
            title: {
              display: true,
              text: 'Games',
              font: {
                size: 20,
              },
              color: '#1DCD9F', // X-axis label color
            },
          },
          y: {
            title: {
              display: true,
              text: 'Downloads',
              font: {
                size: 20,
              },
              color: '#1DCD9F', // Y-axis label color
            },
          },
        },
      },
    }
  },
  computed: {
    data() {
      return {
        labels: this.labels,
        datasets: [
          {
            label: 'Number Of Downloads',
            backgroundColor: '#1DCD9F',
            borderColor: '#1DCD9F',
            borderWidth: 2,
            hoverBackgroundColor: 'rgba(0, 255, 0, 0.7)',
            hoverBorderColor: '#1DCD9F',
            hoverBorderWidth: 3,
            data: this.data_downloads,
          },
        ],
      }
    },
  },
  methods: {
    getGames() {
      const path = 'http://localhost:5000/admin/games'
      axios
        .get(path)
        .then((res) => {
          // console.log(res.data.games)
          this.games = res.data.games
          this.loadGamesToChart()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    loadGamesToChart() {
      let games = [...this.games] // shallow copy to avoid mutating original
        .sort((a, b) => b.no_of_downloads - a.no_of_downloads) // sort descending
      this.labels = games.map((game) => game.title)
      this.data_downloads = games.map((game) => game.no_of_downloads)
      this.loadGamesToTOP()
    },
    loadGamesToTOP() {
      this.top3 = [...this.games] // shallow copy to avoid mutating original
        .sort((a, b) => b.no_of_downloads - a.no_of_downloads) // sort descending
        .slice(0, 3) // take top 3
      console.log(this.top3)

      this.top5 = [...this.games]
        .sort((a, b) => b.rating - a.rating)
        .slice(0, 5) // take top 5
      console.log(this.top5)
    },
  },
  created() {
    this.getGames()
  },
}
</script>

<style>
/* CSS */
</style>
