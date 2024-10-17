<template>
  <div class="min-h-screen flex items-center justify-center">
    <div class="w-full max-w-3xl p-4">
      <div class="bg-neutral text-white p-6 rounded-lg shadow-lg">
        <h1
          class="text-3xl text-center bg-primary-content text-accent p-4 rounded-lg"
        >
          Genre
        </h1>
        <hr class="my-4" />

        <!-- Alert Message -->
        <div v-if="showMessage" class="alert alert-success">
          {{ message }}
        </div>

        <div class="flex space-x-2">
          <!-- Add Genre Button -->
          <button
            type="button"
            class="btn btn-outline btn-accent"
            @click="showAddGenre = true"
          >
            Add Genre
          </button>

          <!-- Show Data Button -->
          <button
            type="button"
            class="btn btn-outline btn-info"
            @click="showDataAll"
          >
            Show Data
          </button>

          <!-- Close Data Button -->
          <button
            type="button"
            class="btn btn-outline btn-error"
            @click="closeDataAll"
          >
            Close Data
          </button>
        </div>

        <br />

        <!-- Genre Table -->
        <div v-if="showData">
          <table class="table w-full">
            <thead>
              <tr>
                <th>Title</th>
                <th>Description</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(genre, id) in genre" :key="id">
                <td>{{ genre.title }}</td>
                <td>{{ genre.description }}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Add Genre Dialog -->
        <TransitionRoot
          as="template"
          :show="showAddGenre"
          @close="showAddGenre = false"
        >
          <Dialog as="div" class="fixed z-10 inset-0 overflow-y-auto">
            <div class="flex items-center justify-center min-h-screen">
              <DialogPanel class="bg-neutral p-6 rounded-lg shadow-lg">
                <DialogTitle class="text-lg font-bold"
                  >Add a New Genre</DialogTitle
                >
                <form @submit.prevent="onSubmitGenre" class="dialog-form">
                  <div class="form-control mt-4">
                    <label for="form-name-input">Genre</label>
                    <input
                      id="form-name-input"
                      type="text"
                      v-model="addGenreForm.title"
                      required
                      placeholder="Enter Genre"
                      class="input input-bordered"
                    />
                  </div>

                  <div class="form-control mt-4">
                    <label for="form-genre-input">Description</label>
                    <input
                      id="form-genre-input"
                      type="text"
                      v-model="addGenreForm.description"
                      required
                      placeholder="Enter Description"
                      class="input input-bordered"
                    />
                  </div>

                  <div class="mt-4">
                    <button class="btn btn-outline" type="submit">Add</button>
                    <button
                      type="button"
                      class="btn btn-outline"
                      @click="showAddGenre = false"
                    >
                      Cancel
                    </button>
                  </div>
                </form>
              </DialogPanel>
            </div>
          </Dialog>
        </TransitionRoot>

        <!-- Footer -->
        <footer
          class="bg-primary-content text-accent p-4 text-center mt-6 rounded-lg"
        >
          Copyright &copy;, All Rights Reserved 2024.
        </footer>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  TransitionRoot,
} from '@headlessui/vue'

export default {
  name: 'genreView',
  components: {
    Dialog,
    DialogPanel,
    DialogTitle,
    TransitionRoot,
  },

  data() {
    return {
      genre: [],
      // filterGenre: {
      //   games: [],
      // },
      addGenreForm: {
        title: '',
        description: '',
      },
      message: '',
      showMessage: false,
      showData: false,
      showAddGenre: false,
      genres: [],
    }
  },
  methods: {
    getGenre() {
      const path = 'http://localhost:5000/genre'
      axios
        .get(path)
        .then((res) => {
          this.genre = res.data
        })
        .catch((err) => {
          console.error(err)
        })
    },
    // POST function
    addGenre(payload) {
      const path = 'http://localhost:5000/genre'
      axios.post(path, payload).then(() => {
        this.getGames()
        // Game alert
        this.message = 'Genre Added!'
        // Show actual message
        this.showMessage = true
      })
    },
    initForm() {
      this.addGenreForm.title = '';
      this.addGenreForm.description = '';
    },
    // This is for modal 1 - to submit new game
    onSubmitGenre(e) {
      e.preventDefault()
      this.showAddGenre = false;
      const payload = {
        title: this.addGenreForm.title,
        desc: this.addGenreForm.description,
      }
      this.addGenre(payload)
      this.initForm()
    },
    onSubmitFilter(e) {
      e.preventDefault()
      // const genre_id = Number(this.addGenreForm.genre_id)
      this.initForm()
      // this.getGenre(genre_id)
    },
    showDataAll() {
      this.showData = true
    },
    closeDataAll() {
      this.showData = false
    },
  },
  created() {
    this.getGenre()
  },
}
</script>

<style>
/* CSS */
</style>
