<template>
  <div>
    <div><navbar-comp /></div>
    <div class="container mx-auto">
      <!-- Header Section -->
      <div role="alert" :class="['alert', alert_type]" v-show="isvisible">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          class="stroke-info h-6 w-6 shrink-0"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
          ></path>
        </svg>
        <span>{{ message }}</span>
      </div>

      <div class="card shadow-lg bg-base-200 p-5 mb-5">
        <div class="card-body">
          <h1 class="text-4xl font-bold text-center mb-3">GameVault</h1>
          <!-- Make a grid layout for the buttons -->
          <div class="flex flex-col items-center space-y-4">
            <!-- Guest button, adjustable width and centered -->
            <button class="btn btn-accent px-10 w-2/5">
              Continue as Guest
            </button>
            <!-- Login and Register buttons are placed in a grid -->
            <div class="flex justify-center space-x-4">
              <button class="btn btn-primary px-6 w-full" @click="openModal">
                Login
              </button>
              <button class="btn btn-secondary px-6 w-full">Register</button>
            </div>
          </div>
        </div>
      </div>

      <!-- Modal Structure -->
      <dialog id="login_modal" class="modal">
        <div class="modal-box w-11/12 max-w-xl">
          <h3 class="text-lg font-bold">Login</h3>

          <!-- Login form -->
          <form class="py-4">
            <!-- Email input -->
            <div class="form-control mb-4">
              <label class="label" for="email">
                <span class="label-text">Email</span>
              </label>
              <input
                v-model="email"
                id="email"
                type="email"
                placeholder="Enter your email"
                class="input input-bordered w-full"
                required
              />
            </div>

            <!-- Password input -->
            <div class="form-control mb-4">
              <label class="label" for="password">
                <span class="label-text">Password</span>
              </label>
              <input
                v-model="password"
                id="password"
                type="password"
                placeholder="Enter your password"
                class="input input-bordered w-full"
                required
              />
            </div>
          </form>

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

      <!-- GAME MODAL -->
      <button class="btn">open modal</button>
      <dialog id="game_modal" class="modal">
        <div class="modal-box w-11/12 max-w-5xl">
          <h3 class="text-lg font-bold">Hello!</h3>
          <p class="py-4">Click the button below to close</p>
          <div class="modal-action">
            <form method="dialog">
              <button class="btn">Close</button>
            </form>
          </div>
        </div>
      </dialog>

      <!-- END OF MODALS. -->

      <div style="margin-bottom: 200px; margin-top: 200px"></div>
      <!-- Top Games Section -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <!-- Card 1 -->
        <div class="card shadow-lg bg-base-100">
          <div class="card-body">
            <h2 class="card-title self-center">The Quest of Mystica</h2>
            <p>Immerse yourself in a magical adventure across unknown lands.</p>
            <button class="btn btn-primary btn-sm">Play Now</button>
          </div>
        </div>
        <!-- Card 2 -->
        <div class="card shadow-lg bg-base-100">
          <div class="card-body">
            <h2 class="card-title self-center" onclick="game_modal.showModal()">
              Speed Racer: Nitro Blast
            </h2>
            <p>
              Feel the adrenaline rush in this high-speed racing experience.
            </p>
            <button
              class="btn btn-primary btn-sm"
              onclick="game_modal.showModal()"
            >
              Play Now
            </button>
          </div>
        </div>
        <!-- Card 3 -->
        <div class="card shadow-lg bg-base-100">
          <div class="card-body">
            <h2 class="card-title self-center">Galactic Conqueror</h2>
            <p>Battle across galaxies and conquer enemy territories.</p>
            <button
              class="btn btn-primary btn-sm"
              onclick="game_modal.showModal()"
            >
              Play Now
            </button>
          </div>
        </div>
      </div>

      <!-- Footer Section -->
      <footer class="mt-10 p-5 bg-neutral text-neutral-content">
        <div class="flex justify-between">
          <div>
            <h3 class="text-lg font-bold">Contact Us</h3>
            <p>Email: support@gamevault.com</p>
          </div>
          <div>
            <h3 class="text-lg font-bold">Newsletter</h3>
            <p>Sign up for the latest news and updates.</p>
            <button class="btn btn-sm btn-accent">Subscribe</button>
          </div>
        </div>
      </footer>
    </div>
  </div>
</template>

<script>
import navbarComp from '../components/navbarComp.vue'
import axios from 'axios'
export default {
  name: 'LandingView',
  components: {
    navbarComp: navbarComp,
  },
  data() {
    return {
      email: '',
      password: '',
      message: '',
      isvisible: false,
      alert_type: '',
    }
  },
  methods: {
    submitLoginForm() {
      const path = 'http://127.0.0.1:5000/api/login'
      axios
        .post(path, { email: this.email, password: this.password }, {})
        .then((res) => {
          if (res.data.status == 'success') {
            this.isvisible = true
            this.message = res.data.message
            this.alert_type = 'alert-success'
          } else if (res.data.status == 'failure') {
            this.isvisible = true
            this.message = res.data.message
            this.alert_type = 'alert-error'
          } else {
            this.isvisible = true
            this.message = 'There was an error.'
            this.alert_type = 'alert-error'
          }
          this.closeModal()
        })
        .catch(() => {
          this.isvisible = true
          this.message = 'There was an error...'
          this.alert_type = 'alert-error'
          this.closeModal()
        })
      this.closeModal()
    },
    openModal() {
      document.getElementById('login_modal').showModal()
    },
    closeModal() {
      document.getElementById('login_modal').close()
    },
  },
}
</script>

<style scoped>
.container {
  max-width: 1200px;
}
</style>
