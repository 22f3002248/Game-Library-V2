<template>
  <div class="min-w-screen flex">
    <navbarCompVertical></navbarCompVertical>
    <div class="flex-1">
      <div
        class="bg-accent-content text-white p-6 rounded-lg shadow-lg w-full h-full"
      >
        <h1 class="text-3xl text-center bg-grey text-accent p-4">
          Manage Users
        </h1>
        <hr class="my-4" />

        <table class="table w-full">
          <thead class="text-accent">
            <tr>
              <th>Id</th>
              <th>Username</th>
              <th>Email</th>
              <th>Active</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(user, id) in users" :key="id" class="text-grey">
              <td>{{ user.id }}</td>
              <td>{{ user.username }}</td>
              <td>{{ user.email }}</td>
              <td>
                {{ user.active ? 'Yes' : 'No' }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
// JS
import axios from 'axios'
import navbarCompVertical from '../components/navbarCompVertical.vue'
export default {
  name: 'adminManageUsers',
  components: {
    navbarCompVertical,
  },
  data() {
    return {
      users: [],
    }
  },
  methods: {
    getUsers() {
      const path = 'http://127.0.0.1:5000/admin/users'
      axios
        .get(path)
        .then((res) => {
          this.users = res.data.users
          console.log(this.users)
        })
        .catch((e) => {
          console.error(e)
        })
    },
  },
  created() {
    this.getUsers()
  },
}
</script>

<style>
/* CSS */
</style>
