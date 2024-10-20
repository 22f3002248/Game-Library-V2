<template>
  <div>
    <div><navbar-comp /></div>
    <div class="container mx-auto py-8">
      <!-- Carousel Section -->
      <div class="carousel w-full custom-carousel">
        <div
          v-for="(image, index) in images"
          :key="index"
          :id="'slide' + (index + 1)"
          class="carousel-item relative w-full"
        >
          <img :src="image" class="w-full h-full object-cover" />
          <div
            class="absolute left-5 right-5 top-1/2 flex -translate-y-1/2 transform justify-between"
          >
            <a
              :href="'#slide' + (index === 0 ? images.length : index)"
              class="btn btn-circle"
            >
              ❮
            </a>
            <a
              :href="'#slide' + (index === images.length - 1 ? 1 : index + 2)"
              class="btn btn-circle"
            >
              ❯
            </a>
          </div>
        </div>
      </div>
      <br /><br /><br />
      <h1 class="text-4xl font-bold text-center mb-3">{{ modal_title }}</h1>
      <br />
      <!-- Game Information Section -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-8">
        <!-- Left: Game Cover and Actions -->
        <div class="flex flex-col items-center">
          <img
            :src="modal_poster"
            alt="Game Cover"
            class="shadow-lg rounded-lg"
            style="width: 300px; height: 400px"
          />
          <br />
          <div class="flex flex-col space-y-2">
            <button class="btn btn-primary w-full">Buy</button>
            <button class="btn btn-secondary w-full">Subscribe</button>
            <button class="btn w-full">Add to Wishlist</button>
          </div>
        </div>

        <!-- Right: Game Details -->
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
            <strong>Multiplayer:</strong> {{ modal_multiplayer ? 'Yes' : 'No' }}
          </div>
          <div class="mb-2">
            <strong>No. of Downloads:</strong> {{ modal_no_of_downloads }}
          </div>
        </div>
      </div>

      <!-- Reviews Section -->
      <div class="mt-4">
        <h4 class="text-md font-semibold">Reviews:</h4>
        <!-- Add review section or display reviews -->
        <textarea
          class="textarea w-full h-24 mt-2"
          placeholder="Write your review here..."
        ></textarea>
      </div>
    </div>
  </div>
</template>

<script>
import navbarComp from '../components/navbarComp.vue'
import axios from 'axios'
export default {
  name: 'gamePageView',
  components: {
    navbarComp,
  },
  data() {
    return {
      gameid: this.$route.params.gameid,
      images: [
        'https://img.daisyui.com/images/stock/photo-1625726411847-8cbb60cc71e6.webp',
        'https://img.daisyui.com/images/stock/photo-1609621838510-5ad474b7d25d.webp',
        'https://img.daisyui.com/images/stock/photo-1414694762283-acccc27bca85.webp',
        'https://img.daisyui.com/images/stock/photo-1665553365602-b2fb8e5d1707.webp',
      ],
      // Example game data
      modal_title: '',
      modal_poster: '',
      modal_genre: '',
      modal_release_date: '',
      modal_developer: '',
      modal_publisher: '',
      modal_platform: '',
      modal_rating: '',
      modal_description: '',
      modal_price: 0.0,
      modal_multiplayer: false,
      modal_no_of_downloads: 0,
      isvisible: false,
      message: '',
    }
  },
  methods: {
    getGame() {
      const path = `http://127.0.0.1:5000/api/game/${this.gameid}`
      axios
        .get(path, {})
        .then((res) => {
          // console.log(res)
          if (res.data.status == 'success') {
            this.modal_title = res.data.game.title
            let gs = res.data.game.genres
            let grs = ''
            for (let i = 0; i < gs.length; i++) {
              grs = grs.concat(gs[i].title)
              if (i < gs.length - 1) {
                grs = grs.concat(', ')
              }
            }
            this.modal_genre = grs
            this.modal_poster = res.data.game.poster
            this.modal_release_date = res.data.game.release_date
            this.modal_developer = res.data.game.developer
            this.modal_publisher = res.data.game.publisher
            this.modal_platform = res.data.game.platform
            this.modal_rating = res.data.game.rating
            this.modal_description = res.data.game.description
            this.modal_price = res.data.game.price
            this.modal_multiplayer = res.data.game.multiplayer
            this.modal_no_of_downloads = res.data.game.no_of_downloads
          } else if (res.data.status == 'failure') {
            this.isvisible = true
            this.message = res.data.message
            this.alert_type = 'alert-error'
          }
        })
        .catch(() => {
          // console.log(res)
          this.isvisible = true
          this.message = 'some error'
          this.alert_type = 'alert-error'
        })
    },
  },
  created() {
    this.getGame()
  },
  beforeMount() {
    this.getGame()
  },
}
</script>

<style scoped>
.container {
  max-width: 1200px;
}

/* Custom carousel */
.custom-carousel {
  max-width: 1200px;
  margin: 0 auto;
}

.carousel-item {
  position: relative;
  padding-top: 56.25%; /* 16:9 aspect ratio */
}

.carousel-item img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

@media (max-width: 768px) {
  .custom-carousel {
    max-width: 600px;
  }
}

@media (max-width: 480px) {
  .custom-carousel {
    max-width: 350px;
  }
}

/* Styling for game information section */
.modal-box {
  border-radius: 10px;
}

.flex-col {
  display: flex;
  flex-direction: column;
}

.shadow-lg {
  box-shadow: 2px 2px 30px rgb(205, 204, 204);
}

.btn {
  padding: 10px;
  font-size: 16px;
}

@media (max-width: 768px) {
  .game-info {
    grid-template-columns: 1fr;
  }
}
</style>
