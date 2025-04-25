<template>
  <div class="min-w-screen flex">
    <navbarCompVertical></navbarCompVertical>

    <div class="flex-1">
      <div
        class="bg-accent-content text-white p-6 rounded-lg shadow-lg w-full h-full"
      >
        <h1 class="text-3xl text-center bg-grey text-accent p-4 font-bold">
          Manage Subscriptions
        </h1>
        <hr class="my-4" />
        <!-- Alert Message -->
        <div v-if="showMessage" class="alert alert-success m-3">
          {{ message }}
        </div>
        <!-- start -->
        <div style="overflow: auto; height: 550px">
          <table class="table w-full">
            <thead class="text-accent">
              <tr>
                <th>Id</th>
                <th>Username</th>
                <th>Email</th>
                <th>Subscription Date</th>
                <th>Subscription End Date</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(sub, id) in subscriptions"
                :key="id"
                class="text-grey"
              >
                <td>{{ id + 1 }}</td>
                <td>{{ sub.username }}</td>
                <td>{{ sub.email }}</td>
                <td>{{ sub.subscription_date.slice(0, 10) }}</td>
                <td>{{ sub.subscription_end_date.slice(0, 10) }}</td>
                <td>
                  <div>
                    <p
                      v-if="sub.subscription_status"
                      class="bg-green-600 w-14 border rounded font-bold text-center p-1"
                    >
                      Active
                    </p>
                    <p
                      v-if="!sub.subscription_status"
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
  name: 'adminManageSubscriptions',
  components: {
    navbarCompVertical,
  },
  data() {
    return {
      subscriptions: [],
    }
  },
  methods: {
    getSubscriptions() {
      const path = 'http://127.0.0.1:5000/admin/subscriptions'
      axios
        .get(path)
        .then((res) => {
          this.subscriptions = res.data.subscriptions
        })
        .catch((e) => {
          console.log(e)
        })
    },
  },
  created() {
    this.getSubscriptions()
  },
}
</script>

<style>
/* CSS */
</style>
