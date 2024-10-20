<template>
  <div>
    <navbar-comp />

    <div class="container mx-auto mt-6">
      <!-- Main Content -->

      <!-- Top Navbar -->
      <div
        class="flex justify-between items-center bg-base-100 shadow p-6 mb-8 rounded-lg"
      >
        <div class="text-2xl font-bold text-white-800">
          Welcome, {{ this.$store.getters.get_username }}
        </div>
      </div>

      <!-- Featured Games Section -->
      <section>
        <h3 class="text-3xl font-bold mb-6">Featured Games</h3>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <div
            v-for="(game, index) in topGames"
            :key="index"
            class="card bg-white shadow-lg rounded-lg overflow-hidden"
          >
            <img
              :src="game.poster"
              :alt="game.title"
              class="w-full object-cover h-64"
            />
            <div class="p-4">
              <h4 class="font-bold text-lg mb-2 text-black">
                {{ game.title }}
              </h4>
              <p class="text-sm text-gray-600">{{ game.description }}</p>
              <button
                class="btn btn-secondary mt-4 w-full"
                @click="openGame(game.id)"
              >
                Play Now
              </button>
            </div>
          </div>
        </div>
      </section>

      <!-- Game Library Section -->
      <section class="mt-12">
        <h3 class="text-3xl font-bold mb-6">All Games</h3>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <div
            v-for="(game, index) in allGames"
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
                {{ game.description }}
              </p>
              <button class="btn btn-primary mt-4 w-full">Play</button>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import navbarComp from '../components/navbarComp.vue'
import axios from 'axios'
export default {
  name: 'UserDash',
  components: {
    navbarComp,
  },
  data() {
    return {
      topGames: [],
      userGames: [],
    }
  },
  methods: {
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
  },
  created() {
    this.getTopGames()
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
