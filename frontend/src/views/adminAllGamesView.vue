<template>
  <div class="min-w-screen flex">
    <navbarCompVertical></navbarCompVertical>
    <div class="flex-1">
      <div
        class="bg-accent-content text-white p-6 rounded-lg shadow-lg w-full h-full"
      >
        <div class="flex justify-between mb-6">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search games..."
            class="input input-bordered w-full max-w-2xl"
          />
          <select
            v-model="selectedGenre"
            @change="filterByGenre"
            class="select select-bordered w-full max-w-xs"
          >
            <option value="">All Genres</option>
            <option v-for="genre in genres" :key="genre.id" :value="genre.name">
              {{ genre.name }}
            </option>
          </select>
        </div>

        <!-- Section moved outside of flex for proper structure -->
        <section class="mt-12" style="overflow: auto; height: 550px">
          <h3 class="text-3xl font-bold mb-6 text-accent">
            All Games ({{ filteredGames.length }})
          </h3>
          <hr>
          <br>
          <p v-if="filteredGames.length === 0" class="text-gray-600">
            No games found.
          </p>
          <div
            v-if="filteredGames.length > 0"
            class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6"
          >
            <div
              v-for="(game, index) in filteredGames"
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
              </div>
              <button
                class="btn btn-primary mt-4 w-full"
                @click="openGame(game.id)"
              >
                Play
              </button>
            </div>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
// JS
import axios from 'axios' // Import axios
import navbarCompVertical from '../components/navbarCompVertical.vue'
export default {
  name: 'adminAllGamesView',
  components: {
    navbarCompVertical,
  },
  data() {
    return {
      allGames: [],
      genres: [], // This will hold all available genres
      searchQuery: '',
      selectedGenre: '',
    }
  },
  computed: {
    filteredGames() {
      let filtered = this.allGames

      // Filter by search query
      if (this.searchQuery) {
        filtered = filtered.filter((game) =>
          game.title.toLowerCase().includes(this.searchQuery.toLowerCase())
        )
      }

      // Filter by selected genre)
      if (this.selectedGenre) {
        filtered = filtered.filter((game) => {
          return game.genres.some((genre) => genre === this.selectedGenre)
        })
      }

      return filtered
    },
  },
  methods: {
    getallGames() {
      const path = `http://localhost:5000/admin/games`
      axios
        .get(path)
        .then((res) => {
          if (res.data.status == 'success') {
            this.allGames = res.data.games
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
    getAllGenres() {
      const path = `http://localhost:5000/admin/genre`
      axios
        .get(path)
        .then((res) => {
          if (res.data.status == 'success') {
            // Map genres after fetching them
            this.genres = res.data.genres.map((genre) => {
              return {
                id: genre.id,
                name: genre.title,
              }
            })
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
    filterByGenre() {
      // This is handled by the computed property "filteredGames"
    },
    openGame(gameid) {
      this.$router.push({ name: 'gamePageView', params: { gameid } })
    },
  },
  created() {
    this.getallGames()
    this.getAllGenres()
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
