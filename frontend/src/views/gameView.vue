<template>
  <div class="min-h-screen flex items-center justify-center">
    <div class="w-full max-w-5xl p-4">
      <div class="bg-accent-content text-white p-6 rounded-lg shadow-lg">
        <h1
          class="text-3xl text-center bg-primary-content text-accent p-4 rounded-lg"
        >
          Games Library
        </h1>
        <hr class="my-4" />

        <!-- Alert Message -->
        <div v-if="showMessage" class="alert alert-success">
          {{ message }}
        </div>

        <div class="my-4">
          <!-- Add Game Button -->
          <button
            type="button"
            @click="openAddModel = true"
            class="btn btn-success btn-sm mr-2"
          >
            Add Game
          </button>

          <button
            type="button"
            @click="showData = true"
            class="btn btn-primary btn-sm"
          >
            Show Data
          </button>
        </div>

        <!-- Games Table -->
<<<<<<< HEAD

        <div v-if="showData">
          <button
=======
          
      <div v-if="showData">
        <button
>>>>>>> 9eb1938f1a260f19787e6287efad27b639075c44
            type="button"
            @click="showData = false"
            class="btn btn-error btn-sm"
          >
            Close
          </button>
<<<<<<< HEAD
          <table class="table w-full table-zebra">
            <thead>
              <tr class="text-accent">
                <th>Id</th>
                <th>Name</th>
                <th>Genre</th>
                <th>Played</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(game, id) in games" :key="id">
                <td>{{ game.id }}</td>
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
                <td>
                  <div class="btn-group">
                    <button
                      @click="
                        () => {
                          editGame(game)
                          openEditModal = true
                        }
                      "
                      class="btn btn-info btn-sm"
                    >
                      Update
                    </button>
                    <button
                      @click="deleteGames(game)"
                      class="btn btn-danger btn-sm"
                    >
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
=======
        <table class="table w-full table-zebra">
          <thead>
            <tr class="text-accent">
              <th>Id</th>
              <th>Name</th>
              <th>Genre</th>
              <th>Played</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(game, id) in games" :key="id">
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
              <td>
                <div class="btn-group">
                  <button
                    @click="
                      () => {
                        editGame(game)
                        openEditModal = true
                      }
                    "
                    class="btn btn-info btn-sm"
                  >
                    Update
                  </button>
                  <button
                    @click="deleteGames(game)"
                    class="btn btn-danger btn-sm"
                  >
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
>>>>>>> 9eb1938f1a260f19787e6287efad27b639075c44

        <!-- Footer -->
        <footer
          class="bg-primary-content text-accent p-4 text-center mt-6 rounded-lg"
        >
          Copyright &copy;, All Rights Reserved 2024.
        </footer>
      </div>
    </div>

    <!-- Add Game Modal -->
    <TransitionRoot :show="openAddModel" @close="openAddModel = false">
      <Dialog as="div" class="fixed z-10 inset-0 overflow-y-auto">
        <div class="flex items-center justify-center min-h-screen">
          <div class="fixed inset-0 bg-black bg-opacity-30"></div>

          <DialogPanel
            class="bg-accent-content p-6 rounded-lg shadow-lg w-full max-w-md z-50"
          >
            <DialogTitle class="text-accent text-center font-bold"
              >Add a New Game</DialogTitle
            >

            <form @submit="onSubmit" class="dialog-form">
              <div class="form-control mt-4">
                <label
                  for="game-name"
                  class="block text-sm font-medium text-accent"
                  >Game Name</label
                >
                <input
                  v-model="addGameForm.name"
                  id="game-name"
                  class="mt-1 block w-full rounded-md border-gray-300 shadow-sm input input-bordered"
                  type="text"
                  placeholder="Enter Game Name"
                  required
                />
              </div>

              <div class="form-control mt-4">
                <label
                  for="genres"
                  class="block text-sm font-medium text-accent mb-1"
                  >Genre(s)</label
                >
                <select
                  id="genres"
                  v-model="addGameForm.genre_ids"
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
                <p class="mt-1 text-xs text-gray-500">
                  Hold down the Ctrl (Windows) or Command (Mac) button to select
                  multiple options.
                </p>
              </div>

              <div class="form-control mt-4">
                <label
                  for="played"
                  class="block text-sm font-medium text-accent"
                  >Played?</label
                >
                <input
                  type="checkbox"
                  v-model="addGameForm.played"
                  id="played"
                />
              </div>

              <div class="mt-4 flex justify-end">
                <button type="submit" class="btn btn-outline btn-accent">
                  Submit
                </button>
                <button
                  type="button"
                  @click="openAddModel = false"
                  class="btn btn-outline btn-error ml-4"
                >
                  Cancel
                </button>
              </div>
            </form>
          </DialogPanel>
        </div>
      </Dialog>
    </TransitionRoot>
<<<<<<< HEAD

    <!-- Edit Game Modal -->
    <div v-if="openEditModal">
      <TransitionRoot :show="openEditModal" @close="openEditModal = false">
        <Dialog class="relative z-10" @close="openEditModal = false">
          <div class="fixed inset-0 bg-black bg-opacity-30"></div>

          <div class="fixed inset-0 z-10 overflow-y-auto">
            <div class="flex min-h-full items-center justify-center p-4">
              <DialogPanel
                class="w-full max-w-md transform overflow-hidden rounded-lg bg-accent-content p-6 shadow-xl transition-all z-50"
              >
                <DialogTitle
                  class="text-accent font-medium leading-6 bg-grey text-center"
                >
                  Update Game
                </DialogTitle>

                <form @submit.prevent="onSubmitUpdate">
                  <div class="mt-4">
                    <label
                      for="game-name-edit"
                      class="block font-medium text-accent"
                      >Game Name</label
                    >
                    <input
                      v-model="editForm.name"
                      id="game-name-edit"
                      class="mt-1 block w-full rounded-md border-gray-200 shadow-sm"
                      type="text"
                      placeholder="Enter name"
                      required
                    />
                  </div>

=======

    <!-- Edit Game Modal -->
    <div v-if="openEditModal">
      <TransitionRoot :show="openEditModal" @close="openEditModal = false">
        <Dialog class="relative z-10" @close="openEditModal = false">
          <div class="fixed inset-0 bg-black bg-opacity-30"></div>

          <div class="fixed inset-0 z-10 overflow-y-auto">
            <div
              class="flex min-h-full items-center justify-center p-4"
            >
              <DialogPanel
                class="w-full max-w-md transform overflow-hidden rounded-lg bg-accent-content p-6 shadow-xl transition-all z-50"
              >
                <DialogTitle
                  class="text-accent font-medium leading-6 bg-grey text-center"
                >
                  Update Game
                </DialogTitle>

                <form @submit.prevent="onSubmitUpdate">
                  <div class="mt-4">
                    <label
                      for="game-name-edit"
                      class="block font-medium text-accent"
                      >Game Name</label
                    >
                    <input
                      v-model="editForm.name"
                      id="game-name-edit"
                      class="mt-1 block w-full rounded-md border-gray-200 shadow-sm"
                      type="text"
                      placeholder="Enter name"
                      required
                    />
                  </div>

>>>>>>> 9eb1938f1a260f19787e6287efad27b639075c44
                  <div class="mt-4">
                    <label
                      for="genres-edit"
                      class="block font-medium text-accent"
                      >Genre</label
                    >
                    <select
                      id="genres-edit"
                      v-model="editForm.genre_ids"
<<<<<<< HEAD
                      class="mt-1 block w-full rounded-md border-gray-300 shadow-sm"
                      required
                      multiple
                    >
                      <option selected disabled value="">Select options</option>
=======
                      class="mt-1 block w-full rounded-md border-gray-300 shadow-sm "
                      required
                      multiple
                    >
                    <option selected disabled value="">Select options</option>
>>>>>>> 9eb1938f1a260f19787e6287efad27b639075c44
                      <option
                        class="text-grey-700 hover:bg-accent"
                        v-for="genre in genres"
                        :key="genre.id"
                        :value="genre.id"
                      >
                        {{ genre.title }}
                      </option>
                    </select>
                  </div>

                  <div class="mt-4">
<<<<<<< HEAD
                    <label for="played-edit" class="font-bold text-accent mr-4"
=======
                    <label
                      for="played-edit"
                      class=" font-bold text-accent mr-4"
>>>>>>> 9eb1938f1a260f19787e6287efad27b639075c44
                      >Played?</label
                    >
                    <input
                      type="checkbox"
                      v-model="editForm.played"
                      id="played-edit"
                    />
                  </div>

                  <div class="mt-4 flex justify-end">
                    <button type="submit" class="btn btn-outline btn-accent">
                      Update
                    </button>
                    <button
                      type="button"
                      @click="openEditModal = false"
                      class="btn btn-outline btn-error ml-4"
                    >
                      Cancel
                    </button>
                  </div>
                </form>
              </DialogPanel>
            </div>
          </div>
        </Dialog>
      </TransitionRoot>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import { ref } from 'vue'
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  TransitionRoot,
} from '@headlessui/vue'
export default {
  name: 'gameView',
  components: {
    Dialog,
    DialogPanel,
    DialogTitle,
    TransitionRoot,
  },
  data() {
    return {
      games: [],
      genres: [],
      addGameForm: {
        name: '',
        genre_ids: [],
        played: [],
      },
      editForm: {
        name: '',
        genre_ids: [],
        played: [],
      },
      message: '',
      showMessage: false,
      openAddModel: false,
      openEditModal: false,
      showData: false,
    }
  },
  methods: {
    // GET function
    getGames() {
      const path = 'http://localhost:5000/api/games'
      axios
        .get(path)
        .then((res) => {
          this.games = res.data.games
          this.genres = res.data.genres
          console.log(this.games)
        })
        .catch((err) => {
          console.error(err)
        })
    },
    // POST function
    addGame(payload) {
      const path = 'http://localhost:5000/api/games'
      axios.post(path, payload).then(() => {
        this.getGames()
        // Game alert
        this.message = 'Game Added!'
        // Show actual message
        this.showMessage = true
      })
    },
    initForm() {
      this.addGameForm.name = ''
      this.addGameForm.genre_ids = []
      this.addGameForm.played = []
      this.editForm.name = ''
      this.editForm.genre_ids = []
      this.editForm.played = []
    },
    // This is for modal 1 - to submit new game
    onSubmit(e) {
      e.preventDefault()
      this.openAddModel = false
      let played = false
      const genre_ids = this.addGameForm.genre_ids.map((id) => parseInt(id))
      console.log(genre_ids)
      if (this.addGameForm.played[0]) played = true
      const payload = {
        title: this.addGameForm.name,
        genre_ids,
        played,
      }
      this.addGame(payload)
      this.initForm()
    },
    onReset(e) {
      e.preventDefault()
      this.openAddModel = false
      this.initForm()
    },
    // This is for modal 2 - to update new game
    onSubmitUpdate(e) {
      e.preventDefault()
      this.openEditModal = false
      let played = false
      const genre_ids = this.editForm.genre_ids.map((id) => parseInt(id))
      if (this.editForm.played[0]) played = true
      const payload = {
        title: this.editForm.name,
        genre_ids,
        played,
      }
      this.updateGame(payload, this.editForm.id)
    },
    // Handle cancel button click
    onResetUpdate(e) {
      e.preventDefault()
      this.openEditModal = false
      this.initForm()
      this.getGames()
    },
    // Update Individual game
    updateGame(payload, gameID) {
      const path = `http://localhost:5000/api/games/${gameID}`
      axios
        .put(path, payload)
        .then(() => {
          this.getGames()
          this.message = 'Game Updated!'
          this.showMessage = true
        })
        .catch((err) => {
          console.error(err)
          this.getGames()
        })
    },
    // Delete Individual game
    removeGame(gameID) {
      const path = `http://localhost:5000/api/games/${gameID}`
      axios
        .delete(path)
        .then(() => {
          this.getGames()
          this.message = 'Game Removed!'
          this.showMessage = true
        })
        .catch((err) => {
          console.log(err)
          this.getGames()
        })
    },
    // Handle update button
    editGame(game) {
      this.editForm = { ...game } // Ensure the form is filled with the game data
    },
    // Handle delete button
    deleteGames(game) {
      this.removeGame(game.id)
    },
  },
  created() {
    this.getGames()
  },
}
</script>

<style>
/* CSS */
</style>
