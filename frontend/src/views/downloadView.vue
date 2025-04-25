<!-- <template>
  <div>
    <navbar-comp />

    <button @click="downloadInstaller()">Download</button>
    <div v-if="isWaiting">
      <span class="loading loading-dots loading-lg"></span>
      <span class="loading loading-dots loading-lg"></span>
    </div>

  </div>
</template> -->
<template>
  <div>
    <!-- html code -->
    <navbar-comp></navbar-comp>
    <div class="container mx-auto">
      <div
        class="flex justify-between items-center bg-base-100 shadow p-6 mb-8 rounded-lg"
      ></div>
      <h1 class="text-3xl font-bold mb-4">Download Games</h1>
      <section class="mt-12">
        <h1 class="text-2xl font-bold mb-4">Purchased Games</h1>
        <div v-if="purchasedGames.length > 0" class="overflow-x-auto">
          <table
            class="table-auto w-full text-left border-collapse rounded shadow-lg bg-dark"
          >
            <thead class="bg-gray-600">
              <tr>
                <th class="px-4 py-2">Picture & Name</th>
                <th class="px-4 py-2">Genre</th>
                <th class="px-4 py-2">Rating</th>
                <th class="px-4 py-2">Completed?</th>
                <th class="px-4 py-2">Hash</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(game, index) in purchasedGames"
                :key="index"
                class="border-t hover:bg-gray-700"
              >
                <!-- Picture & Name -->
                <td class="px-4 py-3 flex items-center gap-3">
                  <a
                    key=""
                    @click="openGame(game.id)"
                    class="flex items-center gap-3 cursor-pointer"
                  >
                    <img
                      :src="game.poster"
                      :alt="game.title"
                      class="w-12 h-12 object-cover rounded"
                    />
                    <span class="text-white font-medium">{{ game.title }}</span>
                  </a>
                </td>

                <!-- Genre -->
                <td class="px-4 py-3 text-white">
                  {{ game.genres.map((g) => g.title).join(', ') || 'TBD' }}
                </td>

                <!-- Rating -->
                <td class="px-4 py-3 text-white">
                  {{ game.rating || 'N/A' }}
                </td>

                <!-- Completed -->
                <td class="px-4 py-3 text-white">
                  {{ game.id in completedGames ? 'Yes' : 'No' }}
                </td>

                <!-- Hash -->
                <td class="px-4 py-3 text-white">
                  <div v-if="hashes[game.id]">
                    {{ hashes[game.id] }}
                  </div>
                  <div v-else>
                    <button
                      class="btn btn-primary"
                      @click="showHash(game.id)"
                      :disabled="loadingHashes[game.id]"
                    >
                      {{ loadingHashes[game.id] ? 'Loading...' : 'Show Hash' }}
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div v-else class="mt-4 text-white">
          <p>No purchased games found.</p>
        </div>
      </section>
      <br /><br />
      <hr style="border-color: darkslategray" />

      <section class="mt-12">
        <h2 class="text-2xl font-bold mb-4">Subscribed Games</h2>
        <h3 v-if="set_subscription == true">
          Your subscription status: <b>Active</b>
        </h3>
        <h3 v-else>Your subscription status: <b>Inactive</b></h3>
        <h3 v-if="set_subscription == true">
          Your subscription end date: <b>{{ formattedEndDate }}</b>
        </h3>
        <br /><br />
        <div v-if="subOnlyGames.length > 0" class="overflow-x-auto">
          <table
            class="table-auto w-full text-left border-collapse rounded shadow-lg bg-dark"
          >
            <thead class="bg-gray-600">
              <tr>
                <th class="px-4 py-2">Picture & Name</th>
                <th class="px-4 py-2">Genre</th>
                <th class="px-4 py-2">Rating</th>
                <th class="px-4 py-2">Completed?</th>
                <th class="px-4 py-2">Hash</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(game, index) in subOnlyGames"
                :key="index"
                class="border-t hover:bg-gray-700"
              >
                <!-- Picture & Name -->
                <td class="px-4 py-3 flex items-center gap-3">
                  <a
                    key=""
                    @click="openGame(game.id)"
                    class="flex items-center gap-3 cursor-pointer"
                  >
                    <img
                      :src="game.poster"
                      :alt="game.title"
                      class="w-12 h-12 object-cover rounded"
                    />
                    <span class="text-white font-medium">{{ game.title }}</span>
                  </a>
                </td>

                <!-- Genre -->
                <td class="px-4 py-3 text-white">
                  {{ game.genres.map((g) => g.title).join(', ') || 'TBD' }}
                </td>

                <!-- Rating -->
                <td class="px-4 py-3 text-white">
                  {{ game.rating || 'N/A' }}
                </td>

                <!-- Completed -->
                <td class="px-4 py-3 text-white">
                  {{ game.id in completedGames ? 'Yes' : 'No' }}
                </td>

                <!-- Hash -->
                <td class="px-4 py-3 text-white">
                  <div v-if="hashes[game.id]">
                    {{ hashes[game.id] }}
                  </div>
                  <div v-else>
                    <button
                      class="btn btn-primary"
                      @click="showHash(game.id)"
                      :disabled="loadingHashes[game.id]"
                    >
                      {{ loadingHashes[game.id] ? 'Loading...' : 'Show Hash' }}
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div v-else class="mt-4 text-white">
          <p>No subscribed games found.</p>
        </div>
      </section>
    </div>
    <div class="container mx-auto mt-6">
      <div
        class="flex justify-between items-center bg-base-100 shadow p-6 mb-8 rounded-lg"
      ></div>
      <h1 class="text-3xl font-bold mb-4">Download Installer</h1>
      <button @click="downloadInstaller()" class="btn btn-primary">
        Download Installer</button
      ><br /><br />
      <div v-if="isWaiting" class="loading loading-dots loading-lg"></div>
      <div v-else class="text-gray-600">
        <p>Click the button to download the installer.</p>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import navbarComp from '../components/navbarComp.vue'
// JS

export default {
  name: 'downloadView',
  data() {
    return {
      isWaiting: false,
      set_subscription: false,
      subOnlyGames: [],
      end_date: null,
      paymentMethod: '',
      paymentDetails: {
        cardName: '',
        cardNumber: '',
        expiry: '',
        cvv: '',
        upiId: '',
        bank: '',
        walletNumber: '',
      },
      hash: '',
      hash_show: false,
      hashes: {}, // Stores fetched hashes per game id
      loadingHashes: {}, // Optional: shows loading state per game
      timeoutHandles: {},
      purchasedGames: [],
      completedGames: [],
    }
  },
  components: {
    navbarComp: navbarComp,
  },
  computed: {
    formattedEndDate() {
      const dateObj = new Date(this.end_date.replace(' ', 'T')) // Convert to ISO 8601
      const options = {
        hour: '2-digit',
        minute: '2-digit',
        hour12: true,
      }
      const time = dateObj.toLocaleTimeString('en-US', options)
      const date = dateObj.toLocaleDateString('en-GB') // dd/mm/yyyy
      return `${time} ${date}`
    },
  },
  watch: {
    set_subscription(newValue) {
      if (newValue) {
        this.getSubOnlyGames()
      }
    },
  },
  methods: {
    checkSubscription() {
      axios
        .get(
          `http://127.0.0.1:5000/api/check/subscription/${this.$store.getters.get_userid}`
        )
        .then((response) => {
          if (response.data.subscription == true) {
            this.end_date = response.data.end_date
            this.set_subscription = true
            this.getSubOnlyGames()
          } else {
            this.set_subscription = false
          }
        })
    },
    openModal() {
      document.getElementById('subscription_modal').showModal()
    },
    closeModal() {
      document.getElementById('subscription_modal').close()
    },
    getSubOnlyGames() {
      axios
        .get(
          `http://127.0.0.1:5000/api/subscription/${this.$store.getters.get_userid}/games/only`
        )
        .then((response) => {
          this.subOnlyGames = response.data.games
        })
        .catch((error) => {
          console.error('Error fetching games:', error)
        })
    },
    getPurchasedGames() {
      axios
        .get(
          `http://127.0.0.1:5000/api/purchase/${this.$store.getters.get_userid}/purchased`
        )
        .then((response) => {
          this.purchasedGames = response.data.games
        })
        .catch((error) => {
          console.error('Error fetching games:', error)
        })
    },
    openGame(gameid) {
      this.$router.push({ name: 'gamePageView', params: { gameid } })
    },
    handlePayment() {
      axios
        .get(
          `http://127.0.0.1:5000/api/subscribe/${this.$store.getters.get_userid}`,
          {}
        )
        .then((response) => {
          if (response.data.status == 'success') {
            this.closeModal()
            this.checkSubscription()
          }
        })
        .catch((error) => {
          this.closeModal()
          this.checkSubscription()
        })
    },
    async downloadInstaller() {
      this.isWaiting = true
      const res = await fetch('http://127.0.0.1:5000/download-installer')
      const data = await res.json()
      if (res.ok) {
        const taskId = data['task_id']
        const intvl = setInterval(async () => {
          const installer_res = await fetch(
            `http://127.0.0.1:5000/result-download-installer/${taskId}`
          )
          if (installer_res.ok) {
            this.isWaiting = false
            clearInterval(intvl)
            window.location.href = `http://127.0.0.1:5000/result-download-installer/${taskId}`
          }
        }, 1000)
      }
    },
    openGame(gameid) {
      this.$router.push({ name: 'gamePageView', params: { gameid } })
    },
    getCompletedGames() {
      axios
        .get(
          `http://127.0.0.1:5000/api/${this.$store.getters.get_userid}/games/completed`
        )
        .then((response) => {
          console.log(response.data.games)
          this.completedGames = response.data.games
        })
    },
    showHash(gameId) {
      // Prevent multiple parallel requests
      if (this.loadingHashes[gameId]) return

      this.loadingHashes[gameId] = true

      const url = `http://127.0.0.1:5000/api/user/${this.$store.getters.get_userid}/game/${gameId}/hash`

      axios
        .get(url)
        .then((response) => {
          this.hashes[gameId] = response.data.hash
          this.loadingHashes[gameId] = false

          // Clear any existing timeout
          if (this.timeoutHandles[gameId]) {
            clearTimeout(this.timeoutHandles[gameId])
          }

          // Set timeout to remove hash after 30 seconds
          this.timeoutHandles[gameId] = setTimeout(() => {
            delete this.hashes[gameId]
            delete this.timeoutHandles[gameId]
          }, 30000)
        })
        .catch((error) => {
          console.error('Error fetching hash:', error)
          this.loadingHashes[gameId] = false
        })
    },
  },
  created() {
    this.checkSubscription()
    this.getPurchasedGames()
    this.getCompletedGames()
  },
}
</script>

<style>
/* CSS */
</style>
