<template>
  <div class="min-w-screen flex">
  <navbarCompVertical></navbarCompVertical>
    <div class="flex-1">
      <div class="bg-accent-content text-white p-6 rounded-lg shadow-lg w-full h-full">
        <h1
          class="text-3xl text-center bg-primary-content text-accent p-4 rounded-lg"
        >
         Add Genre
        </h1>
        <hr class="my-4" />

        <!-- Alert Message -->
        <div v-if="showMessage" class="alert alert-success h-10 mb-3">
          {{ message }}
        </div>

        <div class="flex space-x-2">
          <!-- Add Genre Button -->
          <button
            type="button"
            class="btn btn-sm btn-accent"
            @click="showAddGenre = true"
          >
            Add Genre
          </button>

          <!-- Show Data Button -->
          <div v-if="showBtn">
          <button
            type="button"
            class="btn btn-sm btn-info"
            @click="showData=true,showBtn=false,showFilterForm=false,showFilterData=false"
          >
            Show Data
          </button>
          </div> 

          <div>
            <button
                type="button"
                class="btn btn-sm btn-secondary"
                @click="showFilterForm=true,showData=false,showBtn=true"
            >
               Filter
            </button>
          </div>
        </div>

        <br />

        <!-- Genre Table -->
        <div v-if="showData" class="flex">
          <table class="table w-full">
            <thead class="text-accent">
              <tr>
                <th>Id</th>
                <th>Title</th>
                <th>Description</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(genre, id) in genres" :key="id" class="text-grey">
                <td>{{ genre.id }}</td>
                <td>{{ genre.title }}</td>
                <td>{{ genre.description || 'No Description' }}</td>
                <td>
                  <button
                      @click="deleteGenre(genre)"
                      class="btn btn-error btn-sm mr-2"
                    >
                      Delete
                    </button>
                </td>
              </tr>
            </tbody>
          </table>
          <button
            type="button"
            class="btn btn-error mr-5 ml-0"
            @click="showData=false,showBtn=true"
          >
            X
          </button>
        </div>

        <div v-if="showFilterForm" class="flex justify-start">
          <form @submit="onFilter">
            <div>
              <label
                for="genres"
                class="block text-sm font-medium text-accent mb-1"
                >Genre(s)</label
              >
              <div id="genres">
                <label v-for="genre in genres" :key="genre.id" class="flex items-center space-x-2">
                  <input
                    type="checkbox"
                    v-model="addGameForm.select"
                    :value="genre.id"
                    class="checkbox checkbox-accent"
                  />
                  <span class="text-grey-700">{{ genre.title }}</span>
                </label>
              </div>
            </div>
            <div>
              <button
                type="submit"
                class="btn btn-sm btn-accent ml-3 mt-3"
              >
                OK
              </button>
            </div>
          </form>
        </div>

    <div v-if="showFilterData">
      <div v-if="greenFlag" class="mt-5 text-center text-bold text-error">Games not found</div>
      <div v-else>
        <table class="table w-full">
        
          <thead class="text-accent">
            <tr>
              <th>Id</th>
              <th>Title</th>
              <th>Genre</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(game, id) in filterGames" :key="id">
              <td>{{ game.id }}</td>
              <td>{{ game.title }}</td>
              <td>
                <span v-if="game.genres && game.genres.length">
                  {{ game.genres.join(', ') }}
                  <!-- Joining genre titles with a comma -->
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      
    </div>

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

                    <div class="form-control mt-4 text-grey">
                      <label for="form-genre-textarea">Description</label>
                        <textarea
                          id="form-genre-textarea"
                          v-model="addGenreForm.description"
                          required
                          placeholder="Enter Description"
                          class="input input-bordered mt-2"
                          rows="5"
                          cols="5"
                        ></textarea>
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
        <!-- <footer
          class="bg-primary-content text-accent p-4 text-center mt-6 rounded-lg"
        >
          Copyright &copy;, All Rights Reserved 2024.
        </footer> -->
      </div>
    </div>  
  </div>
</template>

<script>
import axios from 'axios'
import navbarCompVertical from '../components/navbarCompVertical.vue';
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
    navbarCompVertical
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
        select: [],
      },
      message: '',
      showMessage: false,
      showData: true,
      showAddGenre: false,
      showBtn:false,
      showFilterForm:false,
      showFilterData:false,
      greenFlag:false,
    }
  },
  methods: {
    getGenre() {
      const path = 'http://localhost:5000/admin/genre'
      axios
        .get(path)
        .then((res) => {
          this.genres = res.data.genres //marshal problem wrapping
          console.log(this.genres)
        })
        .catch((err) => {
          console.error(err)
        })
    },
    // POST function
    addGenre(payload) {
      const path = 'http://localhost:5000/admin/genre'
      axios.post(path, payload).then(() => {
        this.getGenre()
        // Game alert
        this.message = 'Genre Added!'
        // Show actual message
        this.showMessage = true
      })
    },
    initForm() {
      this.addGenreForm.title = ''
      this.addGenreForm.description = ''
      this.addGameForm.select = []
    },
    // This is for modal 1 - to submit new game
    onSubmitGenre(e) {
      e.preventDefault()
      this.showAddGenre = false
      const payload = {
        title: this.addGenreForm.title,
        description: this.addGenreForm.description,
      }
      this.addGenre(payload)
      this.initForm()
    },
    getGames(genre_ids) {
      const path = `http://localhost:5000/admin/genre/${genre_ids}`
      axios
        .get(path)
        .then((res) => {
          this.greenFlag=false
          this.filterGames = res.data.games;
          if(this.filterGames===undefined){
            this.greenFlag=true;
          }
          })
        .catch((err) => {
          console.error(err)
        })
    },
    onFilter(e) {
      e.preventDefault()
      const genre_ids = this.addGameForm.select
        .map((id) => parseInt(id))
        .join(',')
      this.showFilterData=true;  
      this.initForm();
      this.getGames(genre_ids);
    },
    removeGenre(genre_id){
      const path = `http://localhost:5000/admin/genre/${genre_id}`
      axios
        .delete(path)
        .then(() => {
          this.getGenre()
          this.message = 'Genre Removed!'
          this.showMessage = true
        })
        .catch((err) => {
          console.log(err)
          this.getGenre()
        })
    },
    deleteGenre(genre) {
    // Confirmation prompt before deletion
      if (confirm(`Are you sure you want to delete the genre: ${genre.title}?`)) {
      this.removeGenre(genre.id);
      }
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
