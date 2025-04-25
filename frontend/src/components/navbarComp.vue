<template>
  <div>
    <div class="navbar bg-base-100">
      <div class="navbar-start">
        <div class="dropdown">
          <div tabindex="0" role="button" class="btn btn-ghost btn-circle">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h7"
              />
            </svg>
          </div>
          <ul
            tabindex="0"
            class="menu menu-sm dropdown-content bg-base-100 rounded-box z-[1] mt-3 w-52 p-2 shadow"
          >
            <li><a @click="goToHome()">Homepage</a></li>
            <li><a @click="goToLibrary()">Library</a></li>
            <li><a @click="goToProfile()">Profile</a></li>
            <li>
              <a @click="manageUserSubscription()">Manage Subscription</a>
            </li>
            <li><a @click="yourGames()">Download Games</a></li>
            <li><a @click="logout()">Logout</a></li>
          </ul>
        </div>
      </div>
      <div class="navbar-center">
        <a class="btn btn-ghost text-2xl" @click="goToHome()">GameVault</a>
      </div>
      <div class="navbar-end">
        <button class="btn btn-ghost btn-circle" @click="goToLibrary()">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            />
          </svg>
        </button>
      </div>
    </div>
    <!-- LOGOUT MODAL. -->
    <dialog id="login_modal" class="modal">
      <div class="modal-box w-11/12 max-w-xl">
        <h3 class="text-lg font-bold">Logout</h3>
        <p class="py-4">Are you sure you want to logout?</p>
        <p class="py-4">You will be redirected to the landing page.</p>
        <!-- Modal action buttons -->
        <div class="modal-action">
          <!-- Close button -->
          <form method="dialog">
            <button class="btn">Close</button>
          </form>
          <!-- Submit button -->
          <button class="btn btn-primary" @click="submitLoginForm">
            Login
          </button>
        </div>
      </div>
    </dialog>
  </div>
</template>

<script>
export default {
  name: 'navbarComp',
  props: {},
  data() {
    return {}
  },
  methods: {
    goToHome() {
      if (this.$store.getters.get_type == 'admin') {
        this.$router.push({ name: 'adminDash' })
      } else if (this.$store.getters.get_type == 'user') {
        this.$router.push({ name: 'userDash' })
      } else {
        this.$router.push({ name: 'landingView' })
      }
    },
    goToLibrary() {
      this.$router.push({ name: 'allGamesView' })
    },
    logout() {
      this.$store.dispatch('set_state_after_logout').then(() => {
        this.$router.push({ name: 'landingView' })
      })
    },
    submitLoginForm() {
      const form = document.getElementById('login_modal')
      if (form) {
        form.close()
      }
    },
    manageUserSubscription() {
      this.$router.push({ name: 'subscriptionUserManage' })
    },
    yourGames() {
      this.$router.push({ name: 'downloadView' })
    },
    openGame(gameid) {
      this.$router.push({ name: 'gamePageView', params: { gameid } })
    },
    goToProfile() {
      this.$router.push({ name: 'userProfile' })
    },
    goToLibrary() {
      this.$router.push({ name: 'allGamesView' })
    },
  },
}
</script>

<style>
/* CSS */
</style>
