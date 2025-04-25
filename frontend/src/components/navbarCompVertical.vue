<template>
  <div class="frontDIV min-h-screen">
    <nav class="bg-grey text-white w-full min-h-screen p-5 shadow-lg">
      <h2
        class="text-2xl font-bold mb-6 text-center bg-primary-content text-accent p-2 rounded-lg"
      >
        ADMIN
      </h2>
      <ul class="space-y-4">
        <li>
          <a
            @click="goToHome()"
            class="block text-white hover:bg-accent p-3 rounded-lg"
          >
            Home
          </a>
        </li>
        <li>
          <a
            @click="goToLibrary()"
            class="block text-white hover:bg-accent p-3 rounded-lg"
          >
            Game Library
          </a>
        </li>
        <li>
          <a
            @click="goToAddGame()"
            class="block text-white hover:bg-accent p-3 rounded-lg"
          >
            Add Game
          </a>
        </li>
        <li>
          <a
            @click="goToAddGenre()"
            class="block text-white hover:bg-accent p-3 rounded-lg"
          >
            Add Genre
          </a>
        </li>
        <li>
          <a
            @click="goToUsers()"
            class="block text-white hover:bg-accent p-3 rounded-lg"
          >
            Manage Users
          </a>
        </li>
        <li>
          <a
            @click="goToReviews()"
            class="block text-white hover:bg-accent p-3 rounded-lg"
          >
            Manage Reviews
          </a>
        </li>
        <li>
          <a
            @click="goToSubscribes()"
            class="block text-white hover:bg-accent p-3 rounded-lg"
          >
            Manage Subscriptions
          </a>
        </li>
        <li>
          <a
            @click="goToOrders()"
            class="block text-white hover:bg-accent p-3 rounded-lg"
          >
            Manage Purchased Orders
          </a>
        </li>
        <li>
          <a
            @click="logout()"
            class="block text-white hover:bg-accent p-3 rounded-lg"
          >
            Logout
          </a>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
// JS
export default {
  name: 'navbarCompVertical',
  data() {
    return {}
  },
  props: {},
  methods: {
    logout() {
      this.$store.dispatch('set_state_after_logout').then(() => {
        this.$router.push({ name: 'landingView' })
      })
    },
    goToHome() {
      this.$router.push({ name: 'adminDash' })
    },
    goToLibrary() {
      this.$router.push({ name: 'adminAllGamesView' })
    },
    goToAddGame() {
      this.$router.push({ name: 'gameView' })
    },
    goToAddGenre() {
      this.$router.push({ name: 'genreView' })
    },
    goToUsers() {
      this.$router.push({ name: 'adminManageUsers' })
    },
    goToReviews() {
      this.$router.push({ name: 'adminManageReviews' })
    },
    goToSubscribes() {
      this.$router.push({ name: 'adminManageSubscriptions' })
    },
    goToOrders() {
      this.$router.push({ name: 'adminManageOrders' })
    },
  },
}
</script>

<style>
/* CSS */
.frontDIV {
  width: 20%;
}
</style>
