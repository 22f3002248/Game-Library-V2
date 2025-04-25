<template>
  <div class="min-w-screen flex">
    <navbarCompVertical></navbarCompVertical>
    <div class="flex-1">
      <div class="bg-accent-content text-white p-6 shadow-lg w-full h-full">
        <h1 class="text-3xl text-center bg-grey text-accent p-4 font-bold">
          Manage Reviews
        </h1>
        <hr class="my-4" />
        <!-- Alert Message -->
        <div
          v-show="showMessage"
          class="alert alert-success m-2 mx-auto flex justify-between"
          style="max-width: 400px"
        >
          <span>{{ message }}</span>
          <button
            class="rounded-md border border-black px-2 font-bold"
            @click="showMessage = false"
          >
            X
          </button>
        </div>

        <div
          class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10"
          style="overflow: auto; height: 550px"
        >
          <div v-for="(review, id) in reviews" :key="id" class="text-grey">
            <div class="card m-3 border border-grey p-3">
              <div class="flex justify-between">
                <span>{{ review.title }}</span>
                <button
                  @click="deleteReview(review.user_id, review.game_id)"
                  class="btn btn-error btn-sm"
                >
                  Delete
                </button>
              </div>
              <hr class="my-2" />
              <div class="text-sm">{{ review.feedback }}</div>
              <div>Rating: {{ review.rating }}</div>
              <div>
                <span>Date: {{ review.date.split(' ')[0] }}</span>
                <span class="ml-[100px] underline italic font-bold"
                  >@{{ review.username }}</span
                >
              </div>
            </div>
          </div>
        </div>

        <!-- delete confirm box -->
        <div>
          <TransitionRoot
            as="template"
            :show="showDeleteBox"
            @close="showDeleteBox = false"
          >
            <Dialog as="div" class="fixed z-10 inset-0 overflow-y-auto">
              <div class="flex items-center justify-center min-h-screen">
                <DialogPanel
                  class="bg-neutral p-6 rounded-lg w-[500px] shadow-lg"
                >
                  <DialogTitle class="text-accent font-bold text-[1.4rem] mb-4"
                    >Are you sure you want to delete this review ?
                  </DialogTitle>
                  <button
                    type="button"
                    class="btn btn-sm btn-success ml-2"
                    @click="removeReview(user_id, game_id)"
                  >
                    Confirm
                  </button>
                  <button
                    type="button"
                    class="btn btn-sm btn-error ml-2"
                    @click="resetDelete()"
                  >
                    Cancel
                  </button>
                </DialogPanel>
              </div>
            </Dialog>
          </TransitionRoot>
        </div>
        <!-- end box -->
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
  name: 'adminManageReviews',
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
      reviews: [],
      showMessage: false,
      showDeleteBox: false,
      user_id: 0,
      game_id: 0,
    }
  },
  methods: {
    getReviews() {
      const path = 'http://127.0.0.1:5000/admin/reviews'
      axios
        .get(path)
        .then((res) => {
          this.reviews = res.data.reviews
          console.log(this.reviews)
        })
        .catch((e) => {
          console.log(e)
        })
    },

    //remove reviews
    removeReview(user_id, game_id) {
      const path = `http://localhost:5000/api/review/modify/${user_id}/${game_id}`
      axios
        .delete(path)
        .then(() => {
          this.getReviews()
          this.message = 'Genre Removed!'
          this.resetDelete()
          this.showMessage = true
          this.game_id = 0
          this.user_id = 0
        })
        .catch((err) => {
          console.log(err)
          this.getReviews()
        })
    },

    deleteReview(user_id, game_id) {
      this.showDeleteBox = true
      this.user_id = user_id
      this.game_id = game_id
    },
    resetDelete() {
      this.showDeleteBox = false
    },
  },
  created() {
    this.getReviews()
    setTimeout(() => {
      this.showMessage = false
    }, 3000)
  },
}
</script>

<style>
/* CSS */
</style>
