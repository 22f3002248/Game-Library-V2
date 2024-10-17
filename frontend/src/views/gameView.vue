<template>
  <div class="min-h-screen flex items-center justify-center">
    <div class="w-full max-w-5xl p-4">
      <div class="bg-primary text-white p-6 rounded-lg shadow-lg">
        <h1 class="text-3xl text-center bg-primary-content text-primary p-4 rounded-lg">
          Games Library
        </h1>
        <hr class="my-4" />

        <!-- Alert Message -->
        <div v-if="showMessage" class="alert alert-success">
          {{ message }}
        </div>

        <div class="my-4">
          <!-- Add Game Button -->
          <button type="button" @click="openAddModal = true" class="btn btn-success btn-sm">
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
              <td>{{ game.genre.title }}</td>
              <td>
                <span v-if="game.played">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group">
                  <button @click="editGame(game); openEditModal = true" class="btn btn-info btn-sm">
                    Update
                  </button>
                  <button @click="deleteGames(game)" class="btn btn-danger btn-sm">
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>

        <!-- Footer -->
        <footer class="bg-primary-content text-primary p-4 text-center mt-6 rounded-lg">
          Copyright &copy;, All Rights Reserved 2024.
        </footer>
      </div>
    </div>

    <!-- Add Game Modal using Headless UI -->
    <TransitionRoot as="template" :show="openAddModal" @close="openAddModal = false">
      <Dialog class="relative z-10" @close="openAddModal = false">
        <div class="fixed inset-0 bg-black bg-opacity-30"></div>

        <div class="fixed inset-0 z-10 overflow-y-auto">
          <div class="flex min-h-full items-center justify-center p-4 text-center">
            <DialogPanel class="w-full max-w-md transform overflow-hidden rounded-lg bg-white p-6 shadow-xl transition-all">
              <DialogTitle class="text-lg font-medium leading-6 text-gray-900">
                Add a New Game
              </DialogTitle>

              <form @submit.prevent="onSubmit" @reset="onReset">
                <div class="mt-4">
                  <label for="game-name" class="block text-sm font-medium text-gray-700">Game Name</label>
                  <input
                    v-model="addGameForm.name"
                    id="game-name"
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                    type="text"
                    placeholder="Enter Game Name"
                    required
                  />
                </div>

                <div class="mt-4">
                  <label for="genres" class="block text-sm font-medium text-gray-700">Genre(s)</label>
                  <select
                    id="genres"
                    v-model="addGameForm.genre_ids"
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                    required
                    multiple
                  >
                    <option v-for="genre in games.genres" :key="genre.id" :value="genre.id">
                      {{ genre.title }}
                    </option>
                  </select>
                </div>

                <div class="mt-4">
                  <label for="played" class="block text-sm font-medium text-gray-700">Played?</label>
                  <input type="checkbox" v-model="addGameForm.played" id="played" />
                </div>

                <div class="mt-4 flex justify-end">
                  <button type="submit" class="btn btn-primary">Submit</button>
                  <button type="button" @click="openAddModal = false" class="btn btn-secondary ml-4">
                    Cancel
                  </button>
                </div>
              </form>
            </DialogPanel>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>

    <!-- Edit Game Modal -->
    <TransitionRoot as="template" :show="openEditModal" @close="openEditModal = false">
      <Dialog class="relative z-10" @close="openEditModal = false">
        <div class="fixed inset-0 bg-black bg-opacity-30"></div>

        <div class="fixed inset-0 z-10 overflow-y-auto">
          <div class="flex min-h-full items-center justify-center p-4 text-center">
            <DialogPanel class="w-full max-w-md transform overflow-hidden rounded-lg bg-white p-6 shadow-xl transition-all">
              <DialogTitle class="text-lg font-medium leading-6 text-gray-900">
                Update Game
              </DialogTitle>

              <form @submit.prevent="onSubmitUpdate" @reset="onResetUpdate">
                <div class="mt-4">
                  <label for="game-name-edit" class="block text-sm font-medium text-gray-700">Game Name</label>
                  <input
                    v-model="editForm.name"
                    id="game-name-edit"
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                    type="text"
                    placeholder="Enter name"
                    required
                  />
                </div>

                <div class="mt-4">
                  <label for="genres-edit" class="block text-sm font-medium text-gray-700">Genre</label>
                  <select
                    id="genres-edit"
                    v-model="editForm.genre_ids"
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                    required
                    multiple
                  >
                    <option v-for="genre in games.genres" :key="genre.id" :value="genre.id">
                      {{ genre.title }}
                    </option>
                  </select>
                </div>

                <div class="mt-4">
                  <label for="played-edit" class="block text-sm font-medium text-gray-700">Played?</label>
                  <input type="checkbox" v-model="editForm.played" id="played-edit" />
                </div>

                <div class="mt-4 flex justify-end">
                  <button type="submit" class="btn btn-primary">Update</button>
                  <button type="button" @click="openEditModal = false" class="btn btn-secondary ml-4">
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
</template>

<script>
import axios from "axios";
// import { ref } from 'vue';
import { Dialog, DialogPanel, DialogTitle, TransitionRoot } from '@headlessui/vue';
export default {
  name: "gameView",
  components: {
    Dialog,
    DialogPanel,
    DialogTitle,
    TransitionRoot,
  },
  data() {
    return {
      games: [],
      // genres: [],
      addGameForm: {
        name: "",
        genre_ids: [],
        played: [],
      },
      editForm: {
        name: "",
        genre_ids: [],
        played: [],
      },
      message: "",
      showMessage: false,
      openAddModal: false,
      openEditModal: false
    };
  },
  methods: {
    // GET function
    getGames() {
      const path = "http://localhost:5000/games";
      axios
        .get(path)
        .then((res) => {
          this.games = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    // POST function
    addGame(payload) {
      const path = "http://localhost:5000/games";
      axios.post(path, payload).then(() => {
        this.getGames();
        // Game alert
        this.message = "Game Added!";
        // Show actual message
        this.showMessage = true;
      });
    },
    initForm() {
      this.addGameForm.name = "";
      this.addGameForm.genre_ids = [];
      this.addGameForm.played = [];
      this.editForm.name = "";
      this.editForm.genre_ids = [];
      this.editForm.played = [];
    },
    // This is for modal 1 - to submit new game
    onSubmit(e) {
      e.preventDefault();
      this.openAddModal = false;
      let played = false;
      if (this.addGameForm.played[0]) played = true;
      const payload = {
        title: this.addGameForm.name,
        genre_ids: this.addGameForm.genre_ids,
        played,
      };
      this.addGame(payload);
      this.initForm();
    },
    onReset(e) {
      e.preventDefault();
      this.openAddModal=false;
      this.initForm();
    },
    // This is for modal 2 - to update new game
    onSubmitUpdate(e) {
      e.preventDefault();
      this.editGameModal=false;
      let played = false;
      if (this.editForm.played[0]) played = true;
      const payload = {
        title: this.editForm.name,
        genre_id: this.editForm.genre_ids,
        played,
      };
      this.updateGame(payload, this.editForm.id);
    },
    // Handle cancel button click
    onResetUpdate(e) {
      e.preventDefault();
      this.editGameModal=false;
      this.initForm();
      this.getGames();
    },
    // Update Individual game
    updateGame(payload, gameID) {
      const path = `http://localhost:5000/games/${gameID}`;
      axios
        .put(path, payload)
        .then(() => {
          this.getGames();
          this.message = "Game Updated!";
          this.showMessage = true;
        })
        .catch((err) => {
          console.error(err);
          this.getGames();
        });
    },
    // Delete Individual game
    removeGame(gameID) {
      const path = `http://localhost:5000/games/${gameID}`;
      axios
        .delete(path)
        .then(() => {
          this.getGames();
          this.message = "Game Removed!";
          this.showMessage = true;
        })
        .catch((err) => {
          console.log(err);
          this.getGames();
        });
    },
    // Handle update button
    editGame(game) {
      this.editForm = { ...game }; // Ensure the form is filled with the game data
    },
    // Handle delete button
    deleteGames(game) {
      this.removeGame(game.id);
    },
  },
  created() {
    this.getGames();
  },
};
</script>

<style>
/* CSS */
</style>
