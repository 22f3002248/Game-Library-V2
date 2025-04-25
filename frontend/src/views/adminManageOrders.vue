<template>
  <div class="min-w-screen flex">
    <navbarCompVertical></navbarCompVertical>

    <div class="flex-1">
      <div
        class="bg-accent-content text-white p-6 rounded-lg shadow-lg w-full h-full"
      >
        <h1 class="text-3xl text-center bg-grey text-accent p-4">
          Manage Orders
        </h1>
        <hr class="my-4" />
        <!-- Alert Message -->
        <div v-if="showMessage" class="alert alert-success m-3">
          {{ message }}
        </div>

        <!-- start -->
        <table class="table w-full">
          <thead class="text-accent">
            <tr>
              <th>Id</th>
              <th>Username</th>
              <th>Email</th>
              <th>Status</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(order, id) in orders" :key="id" class="text-grey">
              <td>{{ order.id }}</td>
              <td>{{ order.username }}</td>
              <td>{{ order.email }}</td>
              <td>
                <div>
                  <p
                    v-if="order.active"
                    class="bg-green-600 w-14 border rounded font-bold text-center p-1"
                  >
                    Active
                  </p>
                  <p
                    v-if="!order.active"
                    class="bg-red-600 w-16 border rounded font-bold text-center p-1"
                  >
                    Inactive
                  </p>
                </div>
              </td>
              <td></td>
            </tr>
          </tbody>
        </table>
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
      orders: [],
    }
  },
  methods: {
    getOrders() {
      const path = ''
      axios
        .get(path)
        .then((res) => {
          console.log(res)
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
