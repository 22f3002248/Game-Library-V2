<template>
  <div class="min-h-screen flex items-center justify-center">
    <div class="w-full max-w-5xl p-4">
      <div class="bg-primary text-white p-6 rounded-lg shadow-lg">
        <h1
          class="text-3xl text-center bg-primary-content text-primary p-4 rounded-lg"
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
            class="btn btn-success btn-sm"
            v-b-modal.game-modal
          >
            Add Game
          </button>
        </div>

        <!-- Games Table -->
        <table class="table w-full table-zebra">
          <thead>
            <tr>
              <th>Name</th>
              <th>Genre</th>
              <th>Played</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(game, id) in games" :key="id">
              <td>{{ game.title }}</td>
              <td>{{ game.genre_id }}</td>
              <td>
                <span v-if="game.played">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group">
                  <button
                    type="button"
                    class="btn btn-info btn-sm"
                    v-b-modal.game-update-modal
                    @click="editGame(game)"
                  >
                    Update
                  </button>
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="deleteGames(game)"
                  >
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>

        <!-- Footer -->
        <footer
          class="bg-primary-content text-primary p-4 text-center mt-6 rounded-lg"
        >
          Copyright &copy;, All Rights Reserved 2024.
        </footer>
      </div>
    </div>

    <!-- Start Add Game Modal -->
    <div>
      <b-modal
        ref="addGameModal"
        id="game-modal"
        title="Add a new game"
        hide-backdrop
        hide-footer
      >
        <form @submit.prevent="onSubmit" @reset="onReset" class="w-full">
          <div class="form-control">
            <label class="label" for="form-name-input">Name</label>
            <input
              id="form-name-input"
              type="text"
              v-model="addGameForm.name"
              class="input input-bordered"
              required
              placeholder="Enter Game"
            />
          </div>

          <div class="form-control mt-4">
            <label class="label" for="form-genre-input">Genre</label>
            <select
              id="form-genre-input"
              v-model="addGameForm.genre_id"
              class="select select-bordered"
              required
            >
              <option v-for="genre in genres" :key="genre.id" :value="genre.id">
                {{ genre.title }}
              </option>
            </select>
          </div>

          <div class="form-control mt-4">
            <label class="cursor-pointer">
              <input
                type="checkbox"
                class="checkbox"
                v-model="addGameForm.played"
              />
              <span class="label-text">Played?</span>
            </label>
          </div>

          <!-- Submit and Reset Buttons -->
          <div class="mt-4">
            <button class="btn btn-outline btn-info" type="submit">
              Submit
            </button>
            <button class="btn btn-outline btn-error" type="reset">
              Reset
            </button>
          </div>
        </form>
      </b-modal>
    </div>

    <!-- Start Edit Game Modal -->
    <div>
      <b-modal
        ref="editGameModal"
        id="game-update-modal"
        title="Update"
        hide-backdrop
        hide-footer
      >
        <form
          @submit.prevent="onSubmitUpdate"
          @reset="onResetUpdate"
          class="w-full"
        >
          <div class="form-control">
            <label class="label" for="form-name-edit-input">Name</label>
            <input
              id="form-name-edit-input"
              type="text"
              v-model="editForm.name"
              class="input input-bordered"
              required
              placeholder="Enter name"
            />
          </div>

          <div class="form-control mt-4">
            <label class="label" for="form-genre-edit-input">Genre</label>
            <select
              id="form-genre-edit-input"
              v-model="addGameForm.genre_id"
              class="select select-bordered"
              required
            >
              <option v-for="genre in genres" :key="genre.id" :value="genre.id">
                {{ genre.title }}
              </option>
            </select>
          </div>

          <div class="form-control mt-4">
            <label class="cursor-pointer">
              <input
                type="checkbox"
                class="checkbox"
                v-model="editForm.played"
              />
              <span class="label-text">Played?</span>
            </label>
          </div>

          <!-- Update and Cancel Buttons -->
          <div class="mt-4">
            <button class="btn btn-outline btn-info" type="submit">
              Update
            </button>
            <button class="btn btn-outline btn-error" type="reset">
              Cancel
            </button>
          </div>
        </form>
      </b-modal>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'gameView',
  data() {
    return {
      games: [],
      addGameForm: {
        name: '',
        genre_id: '',
        played: [],
      },
      editForm: {
        name: '',
        genre_id: '',
        played: [],
      },
      message: '',
      genres: [
        { text: 'Select One', value: '' },
        { text: 'RPG', value: '1' },
        { text: 'Adventure', value: '2' },
        { text: 'Action', value: '3' },
        { text: 'Retro', value: '4' },
        { text: 'Sports', value: '5' },
        { text: 'Racing', value: '6' },
        { text: 'Puzzle', value: '7' },
        { text: 'Strategy', value: '8' },
        { text: 'Battle Royal', value: '9' },
        { text: 'Horror', value: '10' },
      ],
      showMessage: false,
    }
  },
  methods: {
    // GET function
    getGames() {
      const path = 'http://localhost:5000/api/Games'
      axios
        .get(path)
        .then((res) => {
          this.games = res.data
        })
        .catch((err) => {
          console.error(err)
        })
    },
    // POST function
    addGame(payload) {
      const path = 'http://localhost:5000/api/Games'
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
      this.addGameForm.genre_id = ''
      this.addGameForm.played = []
      this.editForm.name = ''
      this.editForm.genre_id = ''
      this.editForm.played = []
    },
    // This is for modal 1 - to submit new game
    onSubmit(e) {
      e.preventDefault()
      this.$refs.addGameModal.hide()
      let played = false
      if (this.addGameForm.played[0]) played = true
      const payload = {
        title: this.addGameForm.name,
        genre_id: Number(this.addGameForm.genre_id),
        played,
      }
      this.addGame(payload)
      this.initForm()
    },
    onReset(e) {
      e.preventDefault()
      this.$refs.addGameModal.hide()
      this.initForm()
    },
    // This is for modal 2 - to update new game
    onSubmitUpdate(e) {
      e.preventDefault()
      this.$refs.editGameModal.hide()
      let played = false
      if (this.editForm.played[0]) played = true
      const payload = {
        title: this.editForm.name,
        genre_id: Number(this.editForm.genre_id),
        played,
      }
      this.updateGame(payload, this.editForm.id)
    },
    // Handle cancel button click
    onResetUpdate(e) {
      e.preventDefault()
      this.$refs.editGameModal.hide()
      this.initForm()
      this.getGames()
    },
    // Update Individual game
    updateGame(payload, gameID) {
      const path = `http://localhost:5000/api/Games/${gameID}`
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
      const path = `http://localhost:5000/api/Games/${gameID}`
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
