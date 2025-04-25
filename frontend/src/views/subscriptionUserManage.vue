<template>
  <div>
    <!-- html code -->
    <navbar-comp></navbar-comp>
    <div class="container mx-auto mt-6">
      <div
        class="flex justify-between items-center bg-base-100 shadow p-6 mb-8 rounded-lg"
      ></div>
      <h1 class="text-3xl font-bold mb-4">Manage User Subscriptions</h1>
      <h3 v-if="set_subscription == true">
        Your subscription status: <b>Active</b>
      </h3>
      <h3 v-else>Your subscription status: <b>Inactive</b></h3>
      <h3 v-if="set_subscription == true">
        Your subscription end date: <b>{{ formattedEndDate }}</b>
      </h3>

      <div class="mt-4">
        <a>You can extend your subscription:</a> &nbsp;
        <button class="btn btn-primary" @click="openModal()">
          Extend Subscription
        </button>
      </div>
      <section class="mt-12">
        <div
          v-if="allGames.length > 0"
          class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-6 gap-6"
        >
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
                Play Again
              </button>
            </div>
          </div>
        </div>
        <div v-else>
          <p class="text-gray-600">No subscribed games found.</p>
        </div>
      </section>
    </div>

    <!-- SUBSCRIPTION EXTENSION MODAL. -->
    <dialog id="subscription_modal" class="modal">
      <div class="modal-box w-11/12 max-w-xl h-auto">
        <h3 class="text-lg font-bold mb-4">Subscribe & Pay</h3>

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
          <button class="btn btn-primary" @click="handlePayment">Pay</button>
        </div>
      </div>
    </dialog>
  </div>
</template>

<script>
// JS
import axios from 'axios'
import navbarComp from '../components/navbarComp.vue'
export default {
  name: 'subscriptionUserManage',
  components: {
    navbarComp: navbarComp,
  },
  data() {
    return {
      set_subscription: false,
      allGames: [],
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
    }
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
        this.getAllGames()
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
            this.getAllGames()
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
    getAllGames() {
      axios
        .get(
          `http://127.0.0.1:5000/api/subscription/${this.$store.getters.get_userid}/games`
        )
        .then((response) => {
          this.allGames = response.data.games
        })
        .catch((error) => {
          console.error('Error fetching games:', error)
        })
    },
    openGame(gameid) {
      this.$router.push({ name: 'gamePageView', params: { gameid } })
    },
    handlePayment() {},
  },
  created() {
    this.checkSubscription()
  },
}
</script>

<style scoped>
.modal-box img {
  border-radius: 8px;
  border: 1px solid #ccc;
}
</style>
