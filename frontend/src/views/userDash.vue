<template>
  <div>
    <navbar-comp />

    <div class="container mx-auto mt-6">
      <!-- Main Content -->
      <h1 class="text-3xl font-bold mb-4">User Dashboard</h1>
      <UserStatsChart
        v-if="stats"
        :stats="stats"
        class="mb-12"
      ></UserStatsChart>
      <hr style="border-color: darkslategray" />
      <br />
      <!-- Featured Games Section -->
      <section>
        <h3 class="text-3xl font-bold mb-6">Top Rated Games</h3>

        <!-- Flex row layout -->
        <div class="flex flex-wrap gap-6">
          <div
            v-for="(game, index) in topGames"
            :key="index"
            class="flex flex-col sm:flex-row bg-white shadow-lg rounded-lg overflow-hidden w-full sm:w-[48%] lg:w-[32%]"
          >
            <!-- Image on the left -->
            <img
              :src="game.poster"
              :alt="game.title"
              class="w-full sm:w-1/3 object-cover h-64 sm:h-auto"
            />

            <!-- Text on the right -->
            <div class="p-4 flex flex-col justify-between sm:w-2/3">
              <div>
                <h4 class="font-bold text-xl mb-2 text-black">
                  {{ game.title }}
                </h4>
                <p class="text-sm text-gray-600 mb-2">
                  {{ game.description }}
                </p>
                <p class="text-gray-700 font-medium">
                  Rating: {{ game.rating }} ★
                </p>
              </div>
              <button
                class="btn btn-secondary mt-4 sm:mt-6 w-full sm:w-auto"
                @click="openGame(game.id)"
              >
                Play Now
              </button>
            </div>
          </div>
        </div>

        <br />
        <hr style="border-color: darkslategray" />
        <br />
        <button class="btn btn-primary mb-4" @click="goToLibrary()">
          View All Games
        </button>
      </section>

      <section class="mt-12">
        <h3 class="text-3xl font-bold mb-6">Games you completed</h3>
        <div
          v-if="completedGames.length > 0"
          class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-6 gap-6"
        >
          <div
            v-for="(game, index) in completedGames"
            :key="index"
            class="card bg-white shadow-lg rounded-lg overflow-hidden flex flex-col"
          >
            <img
              :src="game.poster"
              :alt="game.title"
              class="w-full object-cover h-auto"
            />
            <div class="p-4 flex flex-col flex-grow">
              <h4 class="font-bold text-lg mb-2 text-black">
                {{ game.title }}
              </h4>
              <p class="text-sm text-gray-600 flex-grow">
                {{
                  game.description.length > 100
                    ? game.description.slice(0, 100) + '...'
                    : game.description
                }}
              </p>
              <button
                class="btn btn-primary mt-4 w-full"
                @click="openGame(game.id)"
              >
                Play
              </button>
            </div>
          </div>
        </div>
        <div v-else>
          <p class="text-gray-600">No completed games found.</p>
        </div>
      </section>
      <section class="mt-12">
        <h3 class="text-3xl font-bold mb-6">Games you purchased</h3>
        <div
          v-if="purchasedGames.length > 0"
          class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-6 gap-6"
        >
          <div
            v-for="(game, index) in purchasedGames"
            :key="index"
            class="card bg-white shadow-lg rounded-lg overflow-hidden flex flex-col"
          >
            <img
              :src="game.poster"
              :alt="game.title"
              class="w-full object-cover h-auto"
            />
            <div class="p-4 flex flex-col flex-grow">
              <h4 class="font-bold text-lg mb-2 text-black">
                {{ game.title }}
              </h4>
              <p class="text-sm text-gray-600 flex-grow">
                {{
                  game.description.length > 100
                    ? game.description.slice(0, 100) + '...'
                    : game.description
                }}
              </p>
              <button
                class="btn btn-primary mt-4 w-full"
                @click="openGame(game.id)"
              >
                Download
              </button>
            </div>
          </div>
        </div>
        <div v-else>
          <p class="text-gray-600">No purchased games found.</p>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import navbarComp from '../components/navbarComp.vue'
import UserStatsChart from '../components/UserStatsChart.vue'
import axios from 'axios'
export default {
  name: 'UserDash',
  components: {
    navbarComp,
    UserStatsChart,
  },
  data() {
    return {
      topGames: [],
      userGames: [],
      allGames: [],
      purchasedGames: [],
      completedGames: [],
      isvisible: false,
      message: '',
      stats: null,
    }
  },
  methods: {
    getUserStats() {
      const path = `http://127.0.0.1:5000/api/user/stats/${this.$store.getters.get_userid}`
      axios
        .get(path)
        .then((res) => {
          if (res.data.status === 'success') {
            this.stats = res.data.data
            console.log(this.stats)
          }
        })
        .catch(() => {
          this.isvisible = true
          this.message = 'Failed to fetch user stats'
          this.alert_type = 'alert-error'
        })
    },
    getTopGames() {
      const path = `http://127.0.0.1:5000/api/games/top/${3}`
      axios
        .get(path, {})
        .then((res) => {
          if (res.data.status == 'success') {
            this.topGames = res.data.games
          } else if (res.data.status == 'failure') {
            this.isvisible = true
            this.message = res.data.message
            this.alert_type = 'alert-error'
          }
        })
        .catch(() => {
          this.isvisible = true
          this.message = res.data.message
          this.alert_type = 'alert-error'
        })
    },
    openGame(gameid) {
      this.$router.push({ name: 'gamePageView', params: { gameid } })
    },
    goToLibrary() {
      this.$router.push({ name: 'allGamesView' })
    },
    getCompletedGames() {
      const path = `http://127.0.0.1:5000/api/games/completed/${this.$store.getters.get_userid}`
      axios
        .get(path, {})
        .then((res) => {
          if (res.data.status == 'success') {
            this.completedGames = res.data.games
            console.log(this.completedGames)
          } else if (res.data.status == 'failure') {
            this.isvisible = true
            this.message = res.data.message
            this.alert_type = 'alert-error'
          }
        })
        .catch(() => {
          this.isvisible = true
          this.message = res.data.message
          this.alert_type = 'alert-error'
        })
    },
    getPurchasedGames() {
      const path = `http://127.0.0.1:5000/api/purchase/${this.$store.getters.get_userid}/purchased`
      axios
        .get(path, {})
        .then((res) => {
          if (res.data.status == 'success') {
            this.purchasedGames = res.data.games
          } else if (res.data.status == 'failure') {
            this.isvisible = true
            this.message = res.data.message
            this.alert_type = 'alert-error'
          }
        })
        .catch((res) => {
          this.isvisible = true
          this.message = res.data.message
          this.alert_type = 'alert-error'
        })
    },
  },
  created() {
    this.getTopGames()
    this.getCompletedGames()
    this.getPurchasedGames()
    this.getUserStats()
  },
}
</script>

<style scoped>
.container {
  max-width: 1280px;
}

.card img {
  transition: transform 0.2s ease-in-out;
}

.card img:hover {
  transform: scale(1.05);
}
</style>
