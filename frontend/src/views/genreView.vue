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
        </div>

        <br />

        <!-- Genre Table -->
        <div v-if="showData">
          <button
            type="button"
            class="btn btn-outline btn-error"
            @click="closeDataAll"
          >
            Close Data
          </button>
          <table class="table w-full">
            <thead>
              <tr>
                <th>Id</th>
                <th>Title</th>
                <th>Description</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(genre, id) in genres" :key="id" class="text-accent">
                <td>{{ genre.id }}</td>
                <td>{{ genre.title }}</td>
                <td>{{ genre.description || 'No Description' }}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="flex justify-start">
          <form @submit="onFilter">
            <div>
              <label
                for="genres"
                class="block text-sm font-medium text-accent mb-1"
                >Genre(s)</label
              >
              <select
                id="genres"
                v-model="addGameForm.select"
                class="mt-1 select select-accent w-full max-w-xs"
                required
                multiple
              >
                <option disabled value="" class="text-grey-700">
                  Select Genre(s)
                </option>
                <option
                  v-for="genre in genres"
                  :key="genre.id"
                  :value="genre.id"
                  class="text-grey-700 hover:bg-accent"
                >
                  {{ genre.title }}
                </option>
              </select>
            </div>
            <div>
              <button
                type="submit"
                class="btn btn-outline btn-accent ml-3 mb-3"
              >
                Filter
              </button>
            </div>
            <p class="mt-1 text-xs text-gray-500">
              Hold down the Ctrl (Windows) or Command (Mac) button to select
              multiple options.
            </p>
          </form>
        </div>

        <table class="table w-full">
            <thead>
              <tr>
                <th>Id</th>
                <th>Title</th>
                <th>Genre</th>
                <th>Played</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(game, id) in filterGames" :key="id" class="text-accent">
                <td> {{ game.id }} </td>
              <td>{{ game.title }}</td>
              <td>
              <span v-if="game.genres && game.genres.length">
                {{ game.genres.join(', ') }}
                <!-- Joining genre titles with a comma -->
              </span>
              </td>
              <td>
                <span v-if="game.played">Yes</span>
                <span v-else>No</span>
              </td>
              </tr>
            </tbody>
          </table>

        <!-- Add Genre Dialog -->
        <div>
          <TransitionRoot
            as="template"
            :show="showAddGenre"
            @close="showAddGenre = false"
          >
            <Dialog as="div" class="fixed z-10 inset-0 overflow-y-auto">
              <div class="flex items-center justify-center min-h-screen">
                <DialogPanel class="bg-neutral p-6 rounded-lg shadow-lg">
                  <DialogTitle class="text-accent font-bold"
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
                        class="input input-bordered mt-2"
                      />
                    </div>

                    <div class="form-control mt-4 text-accent">
                      <label for="form-genre-input">Description</label>
                      <input
                        id="form-genre-input"
                        type="text"
                        v-model="addGenreForm.description"
                        required
                        placeholder="Enter Description"
                        class="input input-bordered mt-2"
                      />
                    </div>

                    <div class="mt-4">
                      <button
                        class="btn btn-outline btn-accent mr-2"
                        type="submit"
                      >
                        Add
                      </button>
                      <button
                        type="button"
                        class="btn btn-outline btn-error ml-2"
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
        </div>

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
      genres: [],
      filterGames: [],
      addGenreForm: {
        title: '',
        description: '',
     
      },
      addGameForm: {
        select:[],
      },
      message: '',
      showMessage: false,
      showData: false,
      showAddGenre: false,
    }
  },
  methods: {
    getGenre() {
      const path = 'http://localhost:5000/api/genre'
      axios
        .get(path)
        .then((res) => {
          this.genres = res.data.genres  //marshal problem wrapping
          // console.log(this.genres)
        })
        .catch((err) => {
          console.error(err)
        })
    },
    // POST function
    addGenre(payload) {
      const path = 'http://localhost:5000/api/genre'
      axios.post(path, payload).then(() => {
        this.getGenre()
        // Game alert
        this.message = 'Genre Added!'
        // Show actual message
        this.showMessage = true
      })
    },
    initForm() {
      this.addGenreForm.title = '';
      this.addGenreForm.description = '';
      this.addGameForm.select = [];
    },
    // This is for modal 1 - to submit new game
    onSubmitGenre(e) {
      e.preventDefault();
      this.showAddGenre = false;
      const payload = {
        title: this.addGenreForm.title,
        description: this.addGenreForm.description,
      }
      this.addGenre(payload);
      this.initForm();
    },
    getGames(genre_ids) {
      const path = `http://localhost:5000/api/genre/${genre_ids}`
      axios
        .get(path)
        .then((res) => {
          this.filterGames = res.data.games;
        })
        .catch((err) => {
          console.error(err)
        })
    },
    onFilter(e) {
      e.preventDefault();
      const genre_ids = this.addGameForm.select.map((id) => parseInt(id)).join(',');
      this.initForm();
      this.getGames(genre_ids);
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
