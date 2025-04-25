<template>
  <div class="min-w-screen flex">
    <navbarCompVertical></navbarCompVertical>

    <div class="flex-1">
      <div
        class="bg-accent-content text-white p-6 rounded-lg shadow-lg w-full h-full"
      >
        <h1 class="text-3xl text-center bg-grey text-accent p-4 font-bold">
          Manage Purchased Orders
        </h1>
        <hr class="my-4" />
        <!-- Alert Message -->
        <div v-if="showMessage" class="alert alert-success m-3">
          {{ message }}
        </div>

        <div class="flex space-x-2 mb-2">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search Username..."
            class="input input-bordered w-2xl"
          />

          <select
            v-model="selectedTitle"
            class="select select-bordered w-full max-w-xs"
          >
            <option value="">All Games</option>
            <option
              v-for="(purchase, index) in purchases"
              :key="index"
              :value="purchase.game_title"
            >
              {{ purchase.game_title }}
            </option>
          </select>
        </div>

        <!-- Show Data Button -->

        <!-- start -->
        <div style="overflow: auto; height: 550px">
          <table class="table w-full">
            <p v-if="filterUsers.length === 0" class="text-gray-600">
              No purchase record found.
            </p>
            <thead v-if="filterUsers.length > 0" class="text-accent">
              <tr>
                <th>Id</th>
                <th>Username</th>
                <th>Email</th>
                <th>Game</th>
                <th>Purchase Date</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(purchase, id) in filterUsers"
                :key="id"
                class="text-grey"
              >
                <td>{{ id + 1 }}</td>
                <td>{{ purchase.username }}</td>
                <td>{{ purchase.email }}</td>
                <td>{{ purchase.game_title }}</td>
                <td>{{ purchase.purchase_date }}</td>
                <td></td>
              </tr>
            </tbody>
          </table>
        </div>
        <!-- end -->
      </div>
    </div>
  </div>
</template>

<script>
// JS
import axios from 'axios'
import navbarCompVertical from '../components/navbarCompVertical.vue'
export default {
  name: 'adminManageOrders',
  components: {
    navbarCompVertical,
  },
  data() {
    return {
      purchases: [],
      searchQuery: '',
      selectedTitle: '',
    }
  },
  computed: {
    filterUsers() {
      let filtered = this.purchases
      // Filter by search query
      if (this.searchQuery) {
        filtered = filtered.filter((purchase) =>
          purchase.username
            .toLowerCase()
            .includes(this.searchQuery.toLowerCase())
        )
      }

      // Filter by selected Game_title
      if (this.selectedTitle) {
        filtered = filtered.filter(
          (purchase) => purchase.game_title == this.selectedTitle
        )
      }
      console.log(filtered)
      return filtered
    },
  },
  methods: {
    getOrders() {
      const path = 'http://127.0.0.1:5000/admin/purchases'
      axios
        .get(path)
        .then((res) => {
          this.purchases = res.data.purchases
        })
        .catch((e) => {
          console.log(e)
        })
    },
  },
  created() {
    this.getOrders()
  },
}
</script>

<style>
/* CSS */
</style>
