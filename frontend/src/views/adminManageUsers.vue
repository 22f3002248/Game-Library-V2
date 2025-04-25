<template>
  <div class="min-w-screen flex">
    <navbarCompVertical></navbarCompVertical>
    <div class="flex-1">
      <div
        class="bg-accent-content text-white p-6 rounded-lg shadow-lg w-full h-full"
      >
        <h1 class="text-3xl text-center bg-grey text-accent p-4 font-bold">
          Manage Users
        </h1>
        <hr class="my-4" />
        <!-- Alert Message -->
        <div v-show="showMessage" class="alert alert-success m-2 mx-auto flex justify-between" style="max-width: 400px;">
          <span>{{ message }}</span> <button class=" rounded-md border border-black px-2 font-bold" @click="showMessage=false">X</button>
        </div>
        <div style="overflow: auto; height: 550px">
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
              <tr v-for="(user, id) in users" :key="id" class="text-grey">
                <td>{{ user.id }}</td>
                <td>{{ user.username }}</td>
                <td>{{ user.email }}</td>
                <td>
                  <div>
                    <p
                      v-if="user.active"
                      class="bg-green-600 w-14 border rounded font-bold text-center p-1"
                    >
                      Active
                    </p>
                    <p
                      v-if="!user.active"
                      class="bg-red-600 w-16 border rounded font-bold text-center p-1"
                    >
                      Blocked
                    </p>
                  </div>
                </td>
                <td>
                  <div>
                    <button
                      v-if="user.active"
                      @click="confirmBlock(user.id)"
                      class="btn btn-sm btn-error"
                    >
                      Block
                    </button>
                    <button
                      v-if="!user.active"
                      @click="confirmBlock(user.id)"
                      class="btn btn-sm btn-success"
                    >
                      Unlock
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <div>
          <TransitionRoot
            as="template"
            :show="showBlockBox"
            @close="showBlockBox = false"
          >
            <Dialog as="div" class="fixed z-10 inset-0 overflow-y-auto">
              <div class="flex items-center justify-center min-h-screen">
                <DialogPanel
                  class="bg-neutral p-6 rounded-lg w-[500px] shadow-lg"
                >
                  <DialogTitle class="text-accent font-bold text-[1.4rem] mb-4"
                    >Are you sure you want to block this user ?</DialogTitle
                  >
                  <button
                    type="button"
                    class="btn btn-sm btn-success ml-2"
                    @click="changeStatusUser(this.user_id)"
                  >
                    Confirm
                  </button>
                  <button
                    type="button"
                    class="btn btn-sm btn-error ml-2"
                    @click="resetBlock()"
                  >
                    Cancel
                  </button>
                </DialogPanel>
              </div>
            </Dialog>
          </TransitionRoot>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// JS
import axios from 'axios'
import navbarCompVertical from '../components/navbarCompVertical.vue'
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  TransitionRoot,
} from '@headlessui/vue'
export default {
  name: 'adminManageUsers',
  components: {
    navbarCompVertical,
    Dialog,
    DialogPanel,
    DialogTitle,
    TransitionRoot,
    navbarCompVertical,
  },

  data() {
    return {
      users: [],
      showBlockBox: false,
      user_id: 0,
      message: '',
      showMessage: false,
    }
  },

  methods: {
    getUsers() {
      const path = 'http://127.0.0.1:5000/admin/users'
      axios
        .get(path)
        .then((res) => {
          this.users = res.data.users
        })
        .catch((e) => {
          console.error(e)
        })
    },
    changeStatusUser(id) {
      const path = `http://127.0.0.1:5000/admin/users/${id}`
      axios
        .get(path)
        .then((res) => {
          console.log(res.data)
          this.message = res.data.message
          this.showMessage = true
          this.getUsers()
        })
        .catch((e) => {
          console.log('error', e)
        })
      this.showBlockBox = false
      this.user_id = 0
    },
    confirmBlock(id) {
      this.showBlockBox = true
      this.user_id = id
    },
    resetBlock() {
      this.showBlockBox = false
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
