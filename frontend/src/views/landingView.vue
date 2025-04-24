<template>
  <div>
    <div class="container mx-auto flex flex-row mt-3">
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
    </div>

    <div
      class="mt-3 w-[1200px] h-[680px] shadow-lg mx-auto rounded rounded-xl bg-[url(https://th.bing.com/th/id/R.d023351cd802d65c50f0f5cfd372f297?rik=AKM1qkQvw1KLsg&riu=http%3a%2f%2fwww.pixelstalk.net%2fwp-content%2fuploads%2f2016%2f05%2fDesktop-gaming-backgrounds-1080p-dosh-tosh.jpg&ehk=vdt7p4cwZQfq4ul%2fSKWfhGTpUBcqPgBwvX%2blPS93sKA%3d&risl=&pid=ImgRaw&r=0)] p-8 bg-cover"
    >
      <div>
        <!-- Make a grid layout for the buttons -->
        <div class="flex justify-end gap-3 mr-24">
          <!-- Login and Register buttons are placed in a grid -->
          <div>
            <button
              class="p-3 italic font-bold text-2xl hover:text-cyan-400 hover:underline"
            >
              Explore
            </button>
          </div>
          <div>
            <button
              class="p-3 italic font-bold text-2xl hover:text-cyan-400 hover:underline"
              @click="openModal"
            >
              Login
            </button>
          </div>
          <div>
            <button
              class="p-3 italic font-bold text-2xl hover:text-cyan-400 hover:underline"
              @click="openRegisterModal"
            >
              Register
            </button>
          </div>
        </div>
      </div>
      <div class="italic">
        <p class="text-6xl mt-10 ml-8 font-bold space-y-1">
          <span class="text-cyan-300 block animate-bounce">Discover.</span>
          <span class="block animate-pulse">Collect.</span>
          <span class="text-cyan-400 block animate-bounce">Play.</span>
          <span class="block animate-pulse">Repeat.</span>
        </p>
        <p
          class="ml-14 mt-3 font-bold w-[170px] opacity-0 animate-fade-in transition-opacity duration-1000 delay-700"
        >
          Whether you're a casual player or a hardcore collector, our game
          library helps you stay connected to the games you love, anytime and
          anywhere.
        </p>
      </div>
    </div>

    <br />
    <hr />
    <div class="container mx-auto">
      <div
        class="text-center text-4xl text-white-200 font-bold p-2 rounded-lg italic mb-3 p-5 opacity-0.9 animate-pulse hover:scale-105 hover:text-cyan-300 transition-all duration-500 ease-in-out"
      >
        Organize your games. Unleash your play.
      </div>

      <hr />
      <br />
      <div class="mr-3">
        <!-- Top Games Section -->
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
          <!-- Card 1 -->
          <div class="card shadow-lg bg-base-100">
            <div class="card-body">
              <img
                :src="topGames[0].poster"
                alt="Image"
                height="400px"
                width="300px"
                style="
                  box-shadow: 2px 2px 30px rgb(205, 204, 204);
                  border-radius: 10px;
                "
              />
              <br />
              <h2
                class="card-title self-center mb-2"
                style="font-size: x-large !important"
              >
                {{ topGames.length > 0 ? topGames[0].title : 'Loading...' }}
              </h2>

              <p class="self-center" style="font-weight: 700">
                Rating:
                {{ topGames.length > 0 ? topGames[0].rating : 'Loading...' }}
              </p>
              <p class="text-justify mb-4">
                {{
                  topGames.length > 0 ? topGames[0].description : 'Loading...'
                }}
              </p>
              <button class="btn btn-primary btn-sm" @click="openGameModal(0)">
                Play Now
              </button>
            </div>
          </div>

          <!-- Card 2 -->
          <div class="card shadow-lg bg-base-100">
            <div class="card-body">
              <img
                :src="topGames[1].poster"
                alt="Image"
                height="400px"
                width="300px"
                style="
                  box-shadow: 2px 2px 30px rgb(205, 204, 204);
                  border-radius: 10px;
                "
              />
              <br />
              <h2
                class="card-title self-center mb-2"
                style="font-size: x-large !important"
              >
                {{ topGames.length > 0 ? topGames[1].title : 'Loading...' }}
              </h2>

              <p class="self-center" style="font-weight: 700">
                Rating:
                {{ topGames.length > 0 ? topGames[1].rating : 'Loading...' }}
              </p>
              <p class="text-justify mb-4">
                {{
                  topGames.length > 0 ? topGames[1].description : 'Loading...'
                }}
              </p>
              <button class="btn btn-primary btn-sm" @click="openGameModal(1)">
                Play Now
              </button>
            </div>
          </div>

          <!-- Card 3 -->
          <div class="card shadow-lg bg-base-100">
            <div class="card-body">
              <img
                :src="topGames[2].poster"
                alt="Image"
                height="400px"
                width="300px"
                style="
                  box-shadow: 2px 2px 30px rgb(205, 204, 204);
                  border-radius: 10px;
                "
              />
              <br />
              <h2
                class="card-title self-center mb-2"
                style="font-size: x-large !important"
              >
                {{ topGames.length > 0 ? topGames[2].title : 'Loading...' }}
              </h2>

              <p class="self-center" style="font-weight: 700">
                Rating:
                {{ topGames.length > 0 ? topGames[2].rating : 'Loading...' }}
              </p>
              <p class="text-justify mb-4">
                {{
                  topGames.length > 0 ? topGames[2].description : 'Loading...'
                }}
              </p>
              <button class="btn btn-primary btn-sm" @click="openGameModal(2)">
                Play Now
              </button>
            </div>
          </div>
        </div>
        <!-- Footer Section -->
        <hr />
        <br />
        <div
          class="text-center italic mx-auto w-[400px] text-2xl text-grey-300 font-bold border border-white-400 p-2 rounded-lg"
        >
          Contact US:
        </div>
        <br />
        <footer
          class="mt-auto p-5 bg-neutral text-neutral-content"
          style="margin-bottom: -29px"
        >
          <div class="flex justify-between">
            <div>
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

    <!-- Modal Structure -->
    <dialog id="register_modal" class="modal">
      <div class="modal-box w-11/12 max-w-xl">
        <h3 class="text-lg font-bold">Register</h3>

        <!-- Register form -->
        <form class="py-4">
          <div class="form-control mb-4">
            <label class="label">
              <span class="label-text">Username</span>
            </label>
            <input
              v-model="username"
              type="text"
              placeholder="Enter your username"
              class="input input-bordered w-full"
              required
            />
          </div>

          <!-- Email input -->
          <div class="form-control mb-4">
            <label class="label">
              <span class="label-text">Email</span>
            </label>
            <input
              v-model="email"
              type="email"
              placeholder="Enter your email"
              class="input input-bordered w-full"
              required
            />
          </div>

          <!-- Password input -->
          <div class="form-control mb-4">
            <label class="label">
              <span class="label-text">Password</span>
            </label>
            <input
              v-model="password"
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
          <button class="btn btn-primary" @click="submitRegisterForm">
            Register
          </button>
        </div>
      </div>
    </dialog>

    <!-- GAME MODAL -->
    <dialog id="game_modal" class="modal">
      <div class="modal-box w-11/12 max-w-5xl">
        <div class="flex justify-between items-center">
          <h3 class="text-2xl font-bold">{{ modal_title }}</h3>
          <form method="dialog">
            <button class="btn">Close</button>
          </form>
        </div>
        <br />
        <br />
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="flex flex-col items-center">
            <img
              :src="modal_poster"
              alt="Image"
              height="400px"
              width="300px"
              style="
                box-shadow: 2px 2px 30px rgb(205, 204, 204);
                border-radius: 10px;
              "
            />
            <br />
            <div class="flex flex-col space-y-2">
              <button class="btn btn-primary">Buy</button>
              <button class="btn btn-secondary">Subscribe</button>
              <button class="btn">Add to Wishlist</button>
            </div>
          </div>
          <div class="flex flex-col">
            <div class="mb-2"><strong>Genre:</strong> {{ modal_genre }}</div>
            <div class="mb-2">
              <strong>Release Date:</strong> {{ modal_release_date }}
            </div>
            <div class="mb-2">
              <strong>Developer:</strong> {{ modal_developer }}
            </div>
            <div class="mb-2">
              <strong>Publisher:</strong> {{ modal_publisher }}
            </div>
            <div class="mb-2">
              <strong>Platform:</strong> {{ modal_platform }}
            </div>
            <div class="mb-2"><strong>Rating:</strong> {{ modal_rating }}</div>
            <div class="mb-2">
              <strong>Description:</strong>
              <p class="text-justify">{{ modal_description }}</p>
            </div>
            <div class="mb-2">
              <strong>Price:</strong> ${{ modal_price.toFixed(2) }}
            </div>
            <div class="mb-2">
              <strong>Multiplayer:</strong>
              {{ modal_multiplayer ? 'Yes' : 'No' }}
            </div>
            <div class="mb-2">
              <strong>No. of Downloads:</strong> {{ modal_no_of_downloads }}
            </div>
          </div>
        </div>
        <div class="mt-4">
          <h4 class="text-md font-semibold">Reviews:</h4>
          <!-- <textarea
              class="textarea w-full h-24 mt-2"
              placeholder="Write your review here..."
            ></textarea> -->
        </div>
      </div>
    </dialog>

    <!-- END OF MODALS. -->
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
      username: '',
      email: '',
      password: '',
      message: '',
      isvisible: false,
      alert_type: '',
      topGames: [],
      modal_title: '',
      modal_genre: '',
      modal_poster: '',
      modal_release_date: '',
      modal_developer: '',
      modal_publisher: '',
      modal_platform: '',
      modal_rating: 0.0,
      modal_description: '',
      modal_price: 0.0,
      modal_multiplayer: false,
      modal_no_of_downloads: 0,
    }
  },
  methods: {
    submitLoginForm() {
      // console.log(this.email, this.password)
      const path = 'http://127.0.0.1:5000/api/login'
      axios
        .post(path, { email: this.email, password: this.password })
        .then((res) => {
          // console.log(res)
          // if (res.data.status == 'success') {
          console.log(res.data.user)
          this.$store.dispatch('set_state_after_login', res.data.user)
          if (this.$store.getters.get_type == 'admin') {
            this.$router.push('/admin/dashboard')
          } else {
            this.$router.push('/user-dashboard')
          }
          // } else if (res.data.status == 'failure') {
          //   this.isvisible = true
          //   this.message = res.data.message
          //   this.alert_type = 'alert-error'
          // } else {
          //   this.isvisible = true
          //   this.message = 'There was an error.'
          //   this.alert_type = 'alert-error'
          // }
          //reset
          this.username = ''
          this.email = ''
          this.password = ''
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

    submitRegisterForm() {
      const path = 'http://127.0.0.1:5000/api/register'
      axios
        .post(path, {
          username: this.username,
          email: this.email,
          password: this.password,
        })
        .then((res) => {
          // console.log(res)
          this.closeRegisterModal()
          //reset
          this.username = ''
          this.email = ''
          this.password = ''
          //show message
          this.isvisible = true
          this.message = res.data.message
          this.alert_type = 'alert-success'
          this.openModal()
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
    openRegisterModal() {
      document.getElementById('register_modal').showModal()
    },
    closeRegisterModal() {
      document.getElementById('register_modal').close()
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
    openGameModal(n) {
      if (Array.isArray(this.topGames) && this.topGames[n]) {
        this.modal_title = this.topGames[n].title
        let gs = this.topGames[n].genres
        let grs = ''
        for (let i = 0; i < gs.length; i++) {
          grs = grs.concat(gs[i])
          if (i < gs.length - 1) {
            grs = grs.concat(', ') // Add comma between genres
          }
        }
        this.modal_genre = grs
        this.modal_poster = this.topGames[n].poster
        this.modal_release_date = this.topGames[n].release_date
        this.modal_developer = this.topGames[n].developer
        this.modal_publisher = this.topGames[n].publisher
        this.modal_platform = this.topGames[n].platform
        this.modal_rating = this.topGames[n].rating
        this.modal_description = this.topGames[n].description
        this.modal_price = this.topGames[n].price
        this.modal_multiplayer = this.topGames[n].multiplayer
        this.modal_no_of_downloads = this.topGames[n].no_of_downloads
        try {
          document.getElementById('game_modal').showModal()
        } catch (error) {
          console.error('Error opening modal:', error)
        }
      } else {
        console.error('Game not found at index:', n)
      }
    },
  },
  created() {
    this.getTopGames()
  },
  beforeMount() {
    this.getTopGames()
  },
}
</script>

<style scoped>
.container {
  max-width: 1200px;
}
.animate-fade-in {
  animation: fadeIn 1s ease-out forwards;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
