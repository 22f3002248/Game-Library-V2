<template>
  <div>
    <div><navbar-comp /></div>
    <div class="container mx-auto py-8">
      <!-- Carousel Section -->
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
          <br /><br />

          <div class="flex flex-col space-y-4">
            <!-- Top Row: Status on left, Purchased/Subscribed on right -->
            <div class="flex justify-between w-full">
              <!-- Left: Status -->
              <div class="pr-4 w-1/2">
                <p v-if="this.completed == true"><b>Status: </b>Completed</p>
                <p v-else><b>Status: </b>Incomplete</p>
              </div>

              <!-- Right: Purchased and Subscribed with vertical separator -->
              <div class="pl-4 w-1/2 border-l border-gray-300">
                <p v-if="this.purchased == true"><b>Purchased: </b>Yes</p>
                <p v-else><b>Purchased: </b>No</p>
                <p v-if="this.subscribed == true"><b>Subscribed: </b>Yes</p>
                <p v-else><b>Subscribed: </b>No</p>
              </div>
            </div>

            <!-- Download Button (below both) -->
            <div
              v-if="
                this.purchased == true ||
                (this.subscribed == true && this.gu_subscribed == true)
              "
              class="flex justify-center"
            >
              <button class="btn btn-secondary w-32" @click="yourGames()">
                Download
              </button>
            </div>
            <div
              v-if="this.subscribed == true && this.gu_subscribed == false"
              class="flex justify-center"
            >
              <button class="btn btn-secondary w-48" @click="subAndDownload()">
                Sub & Download
              </button>
            </div>
          </div>

          <br />
          <div>
            <div
              class="flex flex-col space-y-2"
              v-if="this.subscribed == false && this.gu_subscribed == false"
            >
              <button
                class="btn btn-secondary w-32"
                @click="manageUserSubscription()"
              >
                Subscribe
              </button>
            </div>
          </div>
          <div class="flex flex-col space-y-2" v-if="this.purchased == false">
            <button class="btn btn-primary w-32" @click="openModal()">
              Buy
            </button>
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
            <strong>No. of Downloads:</strong>
            {{ modal_no_of_downloads.toLocaleString('en-IN') }}
          </div>
        </div>
      </div>

      <h1 key="" class="text-4xl font-bold text-center mb-3 mt-8">
        Screenshots
      </h1>
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
      <!-- Reviews Section -->
      <br /><br />
      <hr style="border-color: darkslategray" />
      <br />
      <div class="mt-4">
        <h1 class="text-2xl font-bold mb-4">Reviews</h1>
        <h4 class="text-md font-semibold">Your Review:</h4>

        <!-- User rating -->
        <div class="rating mt-2">
          <input
            type="radio"
            name="user-rating"
            value="1"
            v-model="userRating"
            class="mask mask-star"
          />
          <input
            type="radio"
            name="user-rating"
            value="2"
            v-model="userRating"
            class="mask mask-star"
          />
          <input
            type="radio"
            name="user-rating"
            value="3"
            v-model="userRating"
            class="mask mask-star"
          />
          <input
            type="radio"
            name="user-rating"
            value="4"
            v-model="userRating"
            class="mask mask-star"
          />
          <input
            type="radio"
            name="user-rating"
            value="5"
            v-model="userRating"
            class="mask mask-star"
          />
        </div>

        <textarea
          v-model="user_review.feedback"
          class="textarea w-full h-24 mt-2"
          placeholder="Write your review here..."
        ></textarea>
        <button @click="submitReview" class="btn mt-2">
          {{ userHasReviewed ? 'Update Review' : 'Submit Review' }}
        </button>

        <div v-if="userHasReviewed" class="mt-4">
          <button @click="deleteReview()" class="btn btn-error">
            Delete Review
          </button>
        </div>

        <h4 class="text-md font-semibold mt-6">All Reviews:</h4>
        <div v-for="review in reviews" :key="review.id" class="border-b py-2">
          <p>
            <strong>{{ review.username }}</strong> ({{ review.email }})
          </p>

          <!-- Other user rating -->
          <div class="rating mt-2">
            <input
              type="radio"
              :name="'rating-' + review.id"
              value="1"
              :checked="review.rating === 1"
              class="mask mask-star"
              disabled
            />
            <input
              type="radio"
              :name="'rating-' + review.id"
              value="2"
              :checked="review.rating === 2"
              class="mask mask-star"
              disabled
            />
            <input
              type="radio"
              :name="'rating-' + review.id"
              value="3"
              :checked="review.rating === 3"
              class="mask mask-star"
              disabled
            />
            <input
              type="radio"
              :name="'rating-' + review.id"
              value="4"
              :checked="review.rating === 4"
              class="mask mask-star"
              disabled
            />
            <input
              type="radio"
              :name="'rating-' + review.id"
              value="5"
              :checked="review.rating === 5"
              class="mask mask-star"
              disabled
            />
          </div>

          <p>{{ review.feedback }}</p>
        </div>
      </div>
    </div>

    <!-- PURCHASE EXTENSION MODAL. -->
    <dialog id="subscription_modal" class="modal">
      <div class="modal-box w-11/12 max-w-xl h-auto">
        <h3 class="text-lg font-bold mb-4">
          Purchase the game {{ modal_title }}
        </h3>

        <div class="form-control mb-4">
          <label class="label">
            <span class="label-text">Select Payment Method</span>
          </label>
          <select v-model="paymentMethod" class="select select-bordered w-full">
            <option disabled value="">Choose one</option>
            <option value="card">Credit / Debit Card</option>
            <option value="upi">UPI</option>
            <option value="netbanking">Net Banking</option>
            <option value="wallet">Paytm / Wallet</option>
          </select>
        </div>

        <!-- Dynamic form based on selected payment method -->
        <div v-if="paymentMethod === 'card'">
          <div class="form-control mb-2">
            <label class="label"
              ><span class="label-text">Cardholder Name</span></label
            >
            <input
              v-model="paymentDetails.cardName"
              type="text"
              placeholder="John Doe"
              class="input input-bordered"
            />
          </div>
          <div class="form-control mb-2">
            <label class="label"
              ><span class="label-text">Card Number</span></label
            >
            <input
              v-model="paymentDetails.cardNumber"
              type="text"
              placeholder="XXXX-XXXX-XXXX-XXXX"
              class="input input-bordered"
            />
          </div>
          <div class="flex gap-2">
            <div class="form-control flex-1">
              <label class="label"
                ><span class="label-text">Expiry Date</span></label
              >
              <input
                v-model="paymentDetails.expiry"
                type="text"
                placeholder="MM/YY"
                class="input input-bordered"
              />
            </div>
            <div class="form-control flex-1">
              <label class="label"><span class="label-text">CVV</span></label>
              <input
                v-model="paymentDetails.cvv"
                type="password"
                placeholder="123"
                class="input input-bordered"
              />
            </div>
          </div>
        </div>
        <br />
        <div v-if="paymentMethod === 'upi'" class="mt-4">
          <div class="flex justify-center mt-2">
            <img
              src="https://help.spreadsheetconverter.com/wp-content/uploads/2013/07/car-loan-amortization-mobile-qrcode.png"
              alt="UPI QR Code"
              class="w-32 h-32 rounded-lg border border-gray-300"
              height="100"
              width="100"
            />
          </div>
          <div class="form-control mb-2">
            <label class="label"><span class="label-text">UPI ID</span></label>
            <input
              v-model="paymentDetails.upiId"
              type="text"
              placeholder="yourname@upi"
              class="input input-bordered"
            />
          </div>
        </div>

        <div v-if="paymentMethod === 'netbanking'" class="mt-4">
          <div class="form-control">
            <label class="label"
              ><span class="label-text">Select Bank</span></label
            >
            <select
              v-model="paymentDetails.bank"
              class="select select-bordered w-full"
            >
              <option disabled value="">Choose Bank</option>
              <option>State Bank of India</option>
              <option>HDFC Bank</option>
              <option>ICICI Bank</option>
              <option>Axis Bank</option>
              <option>Other</option>
            </select>
          </div>
        </div>

        <div v-if="paymentMethod === 'wallet'" class="mt-4">
          <div class="form-control">
            <label class="label"
              ><span class="label-text">Mobile Number</span></label
            >
            <input
              v-model="paymentDetails.walletNumber"
              type="text"
              placeholder="Enter mobile number linked with wallet"
              class="input input-bordered"
            />
          </div>
        </div>

        <!-- Modal action buttons -->
        <div class="modal-action mt-6">
          <form method="dialog">
            <button class="btn">Close</button>
          </form>
          <button class="btn btn-primary" @click="handlePayment()">Pay</button>
        </div>
      </div>
    </dialog>
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
      purchased: false,
      subscribed: false,
      access: false,
      completed: false,
      user_review: '',
      reviews: '',
      userHasReviewed: false, // Track if the user has added a review
      currentReviewId: null,
      userRating: 0,
      set_subscription: false,
      gu_subscribed: false,
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
              grs = grs.concat(gs[i])
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
    getGamePhotos() {
      const path = `http://127.0.0.1:5000/api/game/${this.gameid}/photos`
      axios
        .get(path, {})
        .then((res) => {
          // console.log(res)
          if (res.data.status == 'success') {
            this.images = res.data.photos
          }
        })
        .catch(() => {
          // console.log(res)
          this.isvisible = true
          this.message = 'some error'
          this.alert_type = 'alert-error'
        })
    },
    checkSubscription() {
      axios
        .get(
          `http://127.0.0.1:5000/api/check/subscription/${this.$store.getters.get_userid}`
        )
        .then((response) => {
          if (response.data.subscription == true) {
            this.subscribed = true
          } else {
            this.set_subscription = false
          }
        })
    },
    checkPurchase() {
      const userid = this.$store.getters.get_userid
      const path = `http://127.0.0.1:5000/api/check/purchase/${userid}/${this.gameid}`
      axios
        .get(path, {})
        .then((res) => {
          // console.log(res)
          if (res.data.status == 'success') {
            this.purchased = res.data.purchased
            this.completed = res.data.completed
            this.gu_subscribed = res.data.subscribed
          }
        })
        .catch(() => {
          // console.log(res)
          this.isvisible = true
          this.message = 'some error'
          this.alert_type = 'alert-error'
        })
    },
    checkReview() {
      const userid = this.$store.getters.get_userid
      const path = `http://127.0.0.1:5000/api/review/modify/${userid}/${this.gameid}`
      axios
        .get(path, {})
        .then((res) => {
          // console.log(res)
          if (res.data.status == 'success') {
            this.userRating = res.data.review.rating
            this.userHasReviewed = true
            this.user_review = res.data.review
            // console.log(this.userRating, this.user_review)
          }
        })
        .catch(() => {
          // console.log(res)
          this.isvisible = true
          this.message = 'some error'
          this.alert_type = 'alert-error'
        })
    },
    getAllReviews() {
      const path = `http://127.0.0.1:5000/api/review/${this.$route.params.gameid}`
      axios
        .get(path, {})
        .then((res) => {
          console.log(res)
          if (res.data.status == 'success') {
            this.reviews = res.data.reviews
          }
        })
        .catch(() => {
          // console.log(res)
          this.isvisible = true
          this.message = 'some error'
          this.alert_type = 'alert-error'
        })
    },
    deleteReview() {
      const userid = this.$store.getters.get_userid
      const path2 = `http://127.0.0.1:5000/api/review/modify/${userid}/${this.gameid}`
      axios
        .delete(path2, {
          rating: this.userRating,
          feedback: this.user_review.feedback,
          user_id: userid,
          game_id: this.gameid,
        })
        .then((res) => {
          if (res.data.status == 'success') {
            this.checkReview()
            this.userHasReviewed = false
            this.userRating = 0
            this.user_review = ''
            this.getAllReviews()
          }
        })
    },
    submitReview() {
      const userid = this.$store.getters.get_userid
      const path1 = `http://127.0.0.1:5000/api/review`
      const path2 = `http://127.0.0.1:5000/api/review/modify/${userid}/${this.gameid}`
      if (this.userHasReviewed) {
        axios
          .put(path2, {
            rating: this.userRating,
            feedback: this.user_review.feedback,
            user_id: userid,
            game_id: this.gameid,
          })
          .then((res) => {
            if (res.data.status == 'success') {
              this.checkReview()
              this.getAllReviews()
            }
          })
      } else {
        axios
          .post(path1, {
            rating: this.userRating,
            feedback: this.user_review.feedback,
            user_id: userid,
            game_id: this.gameid,
          })
          .then((res) => {
            if (res.data.status == 'success') {
              this.checkReview()
              this.getAllReviews()
            }
          })
      }
    },
    yourGames() {
      this.$router.push({ name: 'downloadView' })
    },
    handlePayment() {
      axios
        .get(
          `http://127.0.0.1:5000/api/purchase/${this.$store.getters.get_userid}/${this.gameid}`,
          {}
        )
        .then((response) => {
          if (response.data.status == 'success') {
            this.closeModal()
            this.checkPurchase()
          }
        })
        .catch(() => {
          this.closeModal()
          this.checkPurchase()
        })
    },
    openModal() {
      document.getElementById('subscription_modal').showModal()
    },
    closeModal() {
      document.getElementById('subscription_modal').close()
    },
    manageUserSubscription() {
      this.$router.push({ name: 'subscriptionUserManage' })
    },
    subAndDownload() {
      const userid = this.$store.getters.get_userid
      const gameid = this.gameid
      const path = `http://127.0.0.1:5000/api/subscribe/download/${userid}/${gameid}`
      axios.get(path, {}).then((res) => {
        if (res.data.status == 'success') {
          this.checkSubscription()
        }
      })
    },
  },
  beforeMount() {
    this.getGame()
    this.getGamePhotos()
    this.checkPurchase()
    this.checkReview()
    this.getAllReviews()
    this.checkSubscription()
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
