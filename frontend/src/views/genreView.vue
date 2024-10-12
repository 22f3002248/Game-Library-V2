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
            v-on:click="showModal"
          >
            Add Genre
          </button>

          <!-- Show Data Button -->
          <button
            type="button"
            class="btn btn-outline btn-info"
            v-on:click="showDataAll"
          >
            Show data
          </button>

          <!-- Close Data Button -->
          <button
            type="button"
            class="btn btn-outline btn-error"
            v-on:click="closeDataAll"
          >
            Close data
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
                <td>{{ genre.desc }}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Filter Button -->
        <button type="button" class="btn btn-outline btn-primary">
          Filter
        </button>

        <!-- Filter Table -->
        <div>
          <table class="table w-full mt-4">
            <thead>
              <tr>
                <th>Game Name</th>
                <th>Genre</th>
                <th>Played</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(game, index) in filterGenre.games" :key="index">
                <td>{{ filterGenre.title }}</td>
                <td>{{ game.title }}</td>
                <td>
                  <span v-if="game.played">Yes</span>
                  <span v-else>No</span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Filter Modal -->
        <div>
          <b-modal
            ref="filterGamesByGenre"
            id="genre-modal"
            title="Filter Games by Genre"
            hide-backdrop
            hide-footer
          >
            <form @submit.prevent="onSubmitFilter" class="w-full">
              <div class="form-control">
                <label class="label" for="form-genre-input">Genre</label>
                <select
                  id="form-genre-input"
                  v-model="addGameForm.genre_id"
                  class="select select-accent w-full max-w-xs"
                  required
                >
                  <option
                    v-for="genre in genres"
                    :key="genre.id"
                    :value="genre.id"
                  >
                    {{ genre.text }}
                  </option>
                </select>

                <!-- Submit Button -->
                <button class="btn btn-outline btn-primary w-20 mt-4" type="submit">
                  Ok
                </button>
              </div>
            </form>
          </b-modal>
        </div>

        <!-- Add Genre Modal -->
        <div v-if="showModalForm">
          <b-modal
            ref="addGameModal"
            id="game-modal"
            title="Add a New Genre"
            hide-backdrop
            hide-footer
          >
            <form @submit.prevent="onSubmit" class="w-full">
              <div class="form-control">
                <label class="label" for="form-name-input">Genre</label>
                <input
                  id="form-name-input"
                  type="text"
                  v-model="addGameForm.title"
                  class="input input-bordered"
                  required
                  placeholder="Enter Genre"
                />
              </div>

              <div class="form-control mt-4">
                <label class="label" for="form-genre-input">Description</label>
                <input
                  id="form-genre-input"
                  type="text"
                  v-model="addGameForm.desc"
                  class="input input-bordered"
                  required
                  placeholder="Enter Description"
                />
              </div>

              <!-- Submit Button -->
              <button class="btn btn-outline mt-4" type="submit">Add</button>
            </form>
          </b-modal>
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

export default {
  name: 'genreView',
  data() {
    return {
      genre: [],
      filterGenre: {
        games: [],
      },
      addGameForm: {
        title: '',
        desc: '',
        genre_id: '',
      },
      message: '',
      showMessage: false,
      showData: false,
      showModalForm: false,
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
    }
  },
  methods: {
    getGames() {
      const path = 'http://localhost:5000/api/Genre'
      axios
        .get(path)
        .then((res) => {
          this.genre = res.data
        })
        .catch((err) => {
          console.error(err)
        })
    },
    getGenre(genre_id) {
      const path = `http://localhost:5000/api/Genres/${genre_id}`
      axios
        .get(path)
        .then((res) => {
          this.filterGenre = res.data
          // if (this.filterGenre) {
          //   this.message = "Games are found";
          //   this.showMessage = true;
          // } else {
          //   this.message = "games not found";
          //   this.showMessage = true;
          // }
        })
        .catch((err) => {
          console.error(err)
        })
    },
    // POST function
    addGame(payload) {
      const path = 'http://localhost:5000/api/Genre'
      axios.post(path, payload).then(() => {
        this.getGames()
        // Game alert
        this.message = 'Game Added!'
        // Show actual message
        this.showMessage = true
      })
    },
    initForm() {
      this.addGameForm.title = ''
      this.addGameForm.desc = ''
      this.addGameForm.genre_id = ''
    },
    // This is for modal 1 - to submit new game
    onSubmit(e) {
      e.preventDefault()
      this.hideModal()
      const payload = {
        title: this.addGameForm.title,
        desc: this.addGameForm.desc,
      }
      this.addGame(payload)
      this.initForm()
    },
    onSubmitFilter(e) {
      e.preventDefault()
      this.$refs.filterGamesByGenre.hide()
      const genre_id = Number(this.addGameForm.genre_id)
      this.initForm()
      this.getGenre(genre_id)
    },
    showDataAll() {
      this.showData = true
    },
    closeDataAll() {
      this.showData = false
    },
    showModal() {
      this.showModalForm = true
    },
    hideModal() {
      this.showModalForm = false
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
