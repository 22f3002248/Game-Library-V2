<template>
  <div class="min-w-screen flex">
    <navbarCompVertical></navbarCompVertical>
    <div class="flex-1">
      <div
        class="bg-accent-content text-white p-6 rounded-lg shadow-lg w-full h-full"
      >
        <h1 class="text-3xl text-center bg-grey text-accent p-4">ADD GAME</h1>
        <hr class="my-4" />

        <!-- Alert Message -->
        <div v-if="showMessage" class="alert alert-success h-10 mb-3">
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
        </div>

        <!-- Games Table -->
        <table class="table w-full table-zebra">
          <thead>
            <tr class="text-accent">
              <th>Id</th>
              <th>Name</th>
              <th>Genre</th>
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
                {{ game.no_of_downloads.toLocaleString('en-IN') }}
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
                    class="btn btn-info btn-sm mr-2"
                  >
                    Update
                  </button>
                  <button
                    @click="deleteGames(game)"
                    class="btn btn-error btn-sm mr-2"
                  >
                    Delete
                  </button>
                  <button
                    @click="openGameModal(game.id)"
                    class="btn btn-primary btn-sm"
                  >
                    Open
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>

        <!-- Footer
        <footer>
          
        </footer> -->
      </div>
    </div>
    <TransitionRoot :show="showGameModal" @close="showGameModal = false">
      <Dialog as="div" class="fixed z-10 inset-0 overflow-y-auto">
        <div class="flex items-center justify-center min-h-full">
          <div class="fixed inset-0 bg-black bg-opacity-30"></div>
          <!-- Background overlay -->

          <DialogPanel
            class="bg-accent-content p-6 rounded-lg shadow-lg max-w-200 z-50"
          >
            <DialogTitle
              class="text-accent font-medium leading-6 bg-grey text-center"
            >
            </DialogTitle>

            <!-- Modal content -->
            <div class="w-full max-w-5xl">
              <div class="flex justify-between items-center ml-20">
                <h3 class="text-2xl font-bold">{{ modal_title }}</h3>
                <div class="mt-4 flex justify-end mr-10">
                  <button
                    @click="showGameModal = false"
                    class="btn btn-sm btn-error ml-10"
                  >
                    X
                  </button>
                </div>
              </div>
              <br />
              <br />
              <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
                <div class="flex flex-col items-center mr-20">
                  <img
                    :src="modal_poster"
                    alt="Image"
                    height="400px"
                    width="300px"
                    style="
                      box-shadow: 2px 2px 30px rgb(205, 204, 204);
                      border-radius: 10px;
                    "
                  />
                  <br />
                </div>
                <div class="flex flex-col">
                  <div class="mb-2">
                    <strong>Genre:</strong> {{ modal_genre }}
                  </div>
                  <div class="mb-2">
                    <strong>Release Date:</strong> {{ modal_release_date }}
                  </div>
                  <div class="mb-2">
                    <strong>Developer:</strong> {{ modal_developer }}
                  </div>
                  <div class="mb-2">
                    <strong>Publisher:</strong> {{ modal_publisher }}
                  </div>
                  <div class="mb-2">
                    <strong>Platform:</strong> {{ modal_platform }}
                  </div>
                  <div class="mb-2">
                    <strong>Rating:</strong> {{ modal_rating }}
                  </div>
                  <div class="mb-2">
                    <strong>Description:</strong>
                    <p class="text-justify">{{ modal_description }}</p>
                  </div>
                  <div class="mb-2">
                    <strong>Price:</strong> ${{ modal_price.toFixed(2) }}
                  </div>
                  <div class="mb-2">
                    <strong>Multiplayer:</strong>
                    {{ modal_multiplayer ? 'Yes' : 'No' }}
                  </div>
                  <div class="mb-2">
                    <strong>No. of Downloads:</strong>
                    {{ modal_no_of_downloads }}
                  </div>
                </div>
              </div>
            </div>
            <!-- Add more fields as needed -->
          </DialogPanel>
        </div>
      </Dialog>
    </TransitionRoot>

    <!-- Add Game Modal -->
    <TransitionRoot :show="openAddModel" @close="openAddModel = false">
      <Dialog as="div" class="fixed z-10 inset-0 overflow-y-auto">
        <div class="flex items-center justify-center min-h-screen">
          <div class="fixed inset-0 bg-black bg-opacity-30"></div>
          <!-- Background overlay -->

          <DialogPanel
            class="bg-accent-content p-6 rounded-lg shadow-lg w-full max-w-5xl z-50"
          >
            <DialogTitle
              class="text-accent font-medium leading-6 bg-grey text-center text-2xl mb-5"
            >
              Add New Game
            </DialogTitle>

            <!-- Modal content -->
            <form @submit="onSubmit" class="w-full max-w-5xl">
              <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
                <!-- Left Column: Image Input, Preview, Genres, Multiplayer -->
                <div class="flex flex-col items-center">
                  <div class="form-control mt-4 w-full">
                    <label
                      for="game-poster"
                      class="block text-sm font-medium text-accent"
                      >Upload Image</label
                    >
                    <input
                      id="game-poster"
                      class="mt-1 block w-full rounded-md border-gray-300 shadow-sm input input-bordered"
                      type="file"
                      placeholder="Ex(.jpg)"
                      required
                      @change="handleFileChange"
                    />
                  </div>

                  <div v-if="imagePreview" class="mt-3">
                    <img
                      :src="imagePreview"
                      alt="Game Picture Preview"
                      style="
                        max-width: 300px;
                        height: auto;
                        border-radius: 10px;
                        box-shadow: 2px 2px 30px rgb(205, 204, 204);
                      "
                    />
                  </div>

                  <!-- Genre Checkboxes -->
                  <div class="form-control mt-4 w-full">
                    <label class="block text-sm font-medium text-accent mb-2"
                      >Select Genres</label
                    >
                    <div class="grid grid-cols-1 gap-2">
                      <label
                        v-for="genre in genres"
                        :key="genre.id"
                        class="flex items-center space-x-2"
                      >
                        <input
                          type="checkbox"
                          v-model="addGameForm.genre_ids"
                          :value="genre.id"
                          class="checkbox checkbox-accent"
                        />
                        <span class="text-grey-700">{{ genre.title }}</span>
                      </label>
                    </div>
                  </div>

                  <!-- Multiplayer Checkbox -->
                  <div class="form-control mt-4 w-full">
                    <label
                      for="game-multiplayer"
                      class="block text-sm font-medium text-accent"
                      >Multiplayer?</label
                    >
                    <input
                      type="checkbox"
                      v-model="addGameForm.multiplayer"
                      id="game-multiplayer"
                      class="checkbox checkbox-accent mt-1"
                    />
                  </div>
                </div>

                <!-- Right Column: Other Inputs -->
                <div class="grid grid-cols-1 gap-5">
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
                      for="game-release_date"
                      class="block text-sm font-medium text-accent"
                      >Select Release Date</label
                    >
                    <input
                      v-model="addGameForm.release_date"
                      id="game-release_date"
                      class="mt-1 block w-full rounded-md border-gray-300 shadow-sm input input-bordered"
                      type="date"
                      required
                    />
                  </div>

                  <div class="form-control mt-4">
                    <label
                      for="game-developer"
                      class="block text-sm font-medium text-accent"
                      >Developer Name</label
                    >
                    <input
                      v-model="addGameForm.developer"
                      id="game-developer"
                      class="mt-1 block w-full rounded-md border-gray-300 shadow-sm input input-bordered"
                      type="text"
                      placeholder="Enter Developer Name"
                      required
                    />
                  </div>

                  <div class="form-control mt-4">
                    <label
                      for="game-publisher"
                      class="block text-sm font-medium text-accent"
                      >Publisher Name</label
                    >
                    <input
                      v-model="addGameForm.publisher"
                      id="game-publisher"
                      class="mt-1 block w-full rounded-md border-gray-300 shadow-sm input input-bordered"
                      type="text"
                      placeholder="Enter Publisher Name"
                      required
                    />
                  </div>

                  <div class="form-control mt-4">
                    <label
                      for="game-platform"
                      class="block text-sm font-medium text-accent"
                      >Platform Name</label
                    >
                    <input
                      v-model="addGameForm.platform"
                      id="game-platform"
                      class="mt-1 block w-full rounded-md border-gray-300 shadow-sm input input-bordered"
                      type="text"
                      placeholder="Enter Platform Name"
                      required
                    />
                  </div>

                  <div class="form-control mt-4">
                    <label
                      for="game-description"
                      class="block text-sm font-medium text-accent"
                      >Description</label
                    >
                    <textarea
                      v-model="addGameForm.description"
                      id="game-description"
                      class="mt-1 block w-full h-full rounded-md border-gray-300 shadow-sm input input-bordered"
                      placeholder="Enter Description"
                      required
                      rows="5"
                      cols="5"
                    ></textarea>
                  </div>

                  <div class="form-control mt-4">
                    <label
                      for="game-price"
                      class="block text-sm font-medium text-accent"
                      >Enter Price</label
                    >
                    <input
                      v-model="addGameForm.price"
                      id="game-price"
                      class="mt-1 block w-full rounded-md border-gray-300 shadow-sm input input-bordered"
                      type="number"
                      step="0.01"
                      placeholder="Ex(0.01,3.22).."
                      required
                    />
                  </div>
                </div>
              </div>

              <div class="mt-4 flex justify-end">
                <button type="submit" class="btn btn-accent btn-sm">
                  Submit
                </button>
                <button
                  type="button"
                  @click="openAddModel = false"
                  class="btn btn-sm btn-error ml-4"
                >
                  Cancel
                </button>
              </div>
            </form>
          </DialogPanel>
        </div>
      </Dialog>
    </TransitionRoot>

    <!-- Edit Game Modal -->
    <div v-if="openEditModal">
      <TransitionRoot :show="openEditModal" @close="openEditModal = false">
        <Dialog class="relative z-10" @close="openEditModal = false">
          <div class="fixed inset-0 bg-black bg-opacity-30"></div>

          <div class="fixed inset-0 z-10 overflow-y-auto">
            <div class="flex min-h-full items-center justify-center p-4">
              <DialogPanel
                class="w-full max-w-4xl transform overflow-hidden rounded-lg bg-accent-content p-6 shadow-xl transition-all z-50"
              >
                <DialogTitle
                  class="text-accent font-medium leading-6 bg-grey text-center"
                >
                  Update Game
                </DialogTitle>

                <form
                  @submit.prevent="onSubmitUpdate"
                  class="grid grid-cols-2 gap-4"
                >
                  <!-- Left Column -->
                  <div class="space-y-4">
                    <div class="form-control">
                      <label
                        for="game-name"
                        class="block text-sm font-medium text-accent"
                        >Game Name</label
                      >
                      <input
                        v-model="editForm.title"
                        id="game-name"
                        class="mt-1 block w-full rounded-md border-gray-300 shadow-sm input input-bordered"
                        type="text"
                        placeholder="Enter Game Name"
                        required
                      />
                    </div>

                    <div class="form-control">
                      <label class="block text-sm font-medium text-accent mb-2"
                        >Select Genres</label
                      >
                      <div class="grid grid-cols-1 gap-2">
                        <label
                          v-for="genre in genres"
                          :key="genre.id"
                          class="flex items-center space-x-2"
                        >
                          <input
                            type="checkbox"
                            v-model="editForm.genre_ids"
                            :value="genre.id"
                            class="checkbox checkbox-accent"
                          />
                          <span class="text-grey-700">{{ genre.title }}</span>
                        </label>
                      </div>
                    </div>

                    <div class="form-control">
                      <label
                        for="game-multiplayer"
                        class="block text-sm font-medium text-accent"
                        >Multiplayer?</label
                      >
                      <input
                        type="checkbox"
                        v-model="editForm.multiplayer"
                        id="game-multiplayer"
                        class="checkbox checkbox-accent"
                      />
                    </div>
                  </div>

                  <!-- Right Column -->
                  <div class="space-y-4">
                    <div class="form-control">
                      <label
                        for="game-release_date"
                        class="block text-sm font-medium text-accent"
                        >Select Release Date</label
                      >
                      <input
                        v-model="editForm.release_date"
                        id="game-release_date"
                        class="mt-1 block w-full rounded-md border-gray-300 shadow-sm input input-bordered"
                        type="date"
                        required
                      />
                    </div>

                    <div class="form-control">
                      <label
                        for="game-developer"
                        class="block text-sm font-medium text-accent"
                        >Developer Name</label
                      >
                      <input
                        v-model="editForm.developer"
                        id="game-developer"
                        class="mt-1 block w-full rounded-md border-gray-300 shadow-sm input input-bordered"
                        type="text"
                        placeholder="Enter Developer Name"
                        required
                      />
                    </div>

                    <div class="form-control">
                      <label
                        for="game-publisher"
                        class="block text-sm font-medium text-accent"
                        >Publisher Name</label
                      >
                      <input
                        v-model="editForm.publisher"
                        id="game-publisher"
                        class="mt-1 block w-full rounded-md border-gray-300 shadow-sm input input-bordered"
                        type="text"
                        placeholder="Enter Publisher Name"
                        required
                      />
                    </div>

                    <div class="form-control">
                      <label
                        for="game-platform"
                        class="block text-sm font-medium text-accent"
                        >Platform Name</label
                      >
                      <input
                        v-model="editForm.platform"
                        id="game-platform"
                        class="mt-1 block w-full rounded-md border-gray-300 shadow-sm input input-bordered"
                        type="text"
                        placeholder="Enter Platform Name"
                        required
                      />
                    </div>

                    <div class="form-control">
                      <label
                        for="game-description"
                        class="block text-sm font-medium text-accent"
                        >Description</label
                      >
                      <textarea
                        v-model="editForm.description"
                        id="game-description"
                        class="mt-1 w-full h-full rounded-md border-gray-300 shadow-sm input input-bordered"
                        placeholder="Enter Description"
                        required
                        rows="5"
                        cols="5"
                      ></textarea>
                    </div>

                    <div class="form-control">
                      <label
                        for="game-price"
                        class="block text-sm font-medium text-accent"
                        >Enter Price</label
                      >
                      <input
                        v-model="editForm.price"
                        id="game-price"
                        class="mt-1 block w-full rounded-md border-gray-300 shadow-sm input input-bordered"
                        type="number"
                        step="0.01"
                        placeholder="Ex(0.01,3.22).."
                        required
                      />
                    </div>
                  </div>

                  <!-- Submit and Cancel Buttons -->
                  <div class="mt-4 flex justify-end col-span-2 space-x-4">
                    <button type="submit" class="btn btn-accent">Update</button>
                    <button
                      type="button"
                      @click="openEditModal = false"
                      class="btn btn-error"
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
import navbarCompVertical from '../components/navbarCompVertical.vue'
export default {
  name: 'gameView',
  components: {
    Dialog,
    DialogPanel,
    DialogTitle,
    TransitionRoot,
    navbarCompVertical,
  },
  data() {
    return {
      games: [],
      genres: [],
      topGames: [],
      addGameForm: {
        name: '',
        genre_ids: [],
        release_date: '',
        developer: '',
        publisher: '',
        platform: '',
        description: '',
        price: 0.0, //float
        multiplayer: [], //boolean
      },
      editForm: {
        id: 0,
        name: '',
        genre_ids: [],
        release_date: '',
        developer: '',
        publisher: '',
        platform: '',
        description: '',
        price: 0.0, //float
        multiplayer: [], //boolean
      },
      message: '',
      modal_title: '',
      modal_genre: '',
      modal_poster: '',
      modal_release_date: '',
      modal_developer: '',
      modal_publisher: '',
      modal_platform: '',
      modal_rating: 0.0,
      modal_description: '',
      modal_price: 0.0,
      modal_multiplayer: false,
      modal_no_of_downloads: 0,
      showMessage: false, //show hide
      openAddModel: false,
      openEditModal: false,
      showData: false,
      showGameModal: false,
      selectedFile: null, //for file
      imagePreview: null,
    }
  },
  methods: {
    // GET function
    getGames() {
      const path = 'http://localhost:5000/admin/games'
      axios
        .get(path)
        .then((res) => {
          this.games = res.data.games
          this.genres = res.data.genres
          this.topGames = res.data.games
        })
        .catch((err) => {
          console.error(err)
        })
    },
    // POST function
    addGame(payload) {
      const path = 'http://localhost:5000/admin/games'
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
      this.addGameForm.release_date = ''
      this.addGameForm.developer = ''
      this.addGameForm.publisher = ''
      this.addGameForm.platform = ''
      this.addGameForm.description = ''
      this.addGameForm.price = 0.0 //float
      this.addGameForm.multiplayer = [] //boolean

      this.editForm.id = ''
      this.editForm.name = ''
      this.editForm.genre_ids = []
      this.editForm.release_date = ''
      this.editForm.developer = ''
      this.editForm.publisher = ''
      this.editForm.platform = ''
      this.editForm.description = ''
      this.editForm.price = 0.0 //float
      this.editForm.multiplayer = [] //boolean
    },
    handleFileChange(event) {
      // Get the selected file from the input
      this.selectedFile = event.target.files[0]
      if (this.selectedFile) {
        const reader = new FileReader()
        reader.onload = (e) => {
          this.imagePreview = e.target.result
        }
        reader.readAsDataURL(this.selectedFile)
      } else {
        this.imagePreview = null
      }
    },
    // This is for modal 1 - to submit new game
    onSubmit(e) {
      e.preventDefault()
      this.openAddModel = false
      // Ensure a file has been selected
      if (!this.selectedFile) {
        alert('Please select a file')
        return
      }
      let multiplayer = false
      const genre_ids = this.addGameForm.genre_ids.map((id) => parseInt(id))
      if (this.addGameForm.multiplayer[0]) multiplayer = true
      const payload = {
        title: this.addGameForm.name,
        genre_ids,
        release_date: this.addGameForm.release_date,
        developer: this.addGameForm.developer,
        publisher: this.addGameForm.publisher,
        platform: this.addGameForm.platform,
        description: this.addGameForm.description,
        price: this.addGameForm.price,
        poster: this.selectedFile,
        multiplayer: this.addGameForm.multiplayer,
      }
      console.log(payload)
      this.addGame(payload)
      this.initForm()
    },
    // onReset(e) {
    //   e.preventDefault()
    //   this.openAddModel = false
    //   this.initForm()
    // },
    // This is for modal 2 - to update new game
    onSubmitUpdate(e) {
      e.preventDefault()
      this.openEditModal = false
      let multiplayer = false
      let genre_ids = []
      genre_ids = this.editForm.genre_ids.map((id) => parseInt(id))
      if (this.editForm.multiplayer[0]) multiplayer = true
      const payload = {
        title: this.editForm.name,
        genre_ids,
        release_date: this.editForm.release_date,
        developer: this.editForm.developer,
        publisher: this.editForm.publisher,
        platform: this.editForm.platform,
        description: this.editForm.description,
        price: this.editForm.price,
        multiplayer: this.editForm.multiplayer,
        // poster: this.editForm.poster
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
      const path = `http://localhost:5000/admin/games/${gameID}`
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
      const path = `http://localhost:5000/admin/games/${gameID}`
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
      if (confirm(`Are you sure you want to delete the game: ${game.title}?`)) {
        this.removeGame(game.id)
      }
    },
    openGameModal(num) {
      let n = num - 1 ///change
      if (Array.isArray(this.topGames) && this.topGames[n]) {
        this.modal_title = this.topGames[n].title
        let gs = this.topGames[n].genres
        let grs = ''
        for (let i = 0; i < gs.length; i++) {
          grs = grs.concat(gs[i])
          if (i < gs.length - 1) {
            grs = grs.concat(', ') // Add comma between genres
          }
        }
        this.modal_genre = grs
        this.modal_poster = this.topGames[n].poster
        this.modal_release_date = this.topGames[n].release_date
        this.modal_developer = this.topGames[n].developer
        this.modal_publisher = this.topGames[n].publisher
        this.modal_platform = this.topGames[n].platform
        this.modal_rating = this.topGames[n].rating
        this.modal_description = this.topGames[n].description
        this.modal_price = this.topGames[n].price
        this.modal_multiplayer = this.topGames[n].multiplayer
        this.modal_no_of_downloads = this.topGames[n].no_of_downloads
        try {
          this.showGameModal = true
        } catch (error) {
          console.error('Error opening modal:', error)
        }
      } else {
        console.error('Game not found at index:', n)
      }
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
