<template>
  <div>
    <navbarComp></navbarComp>
    <div class="p-6 max-w-4xl mx-auto">
      <!-- Profile Card -->
      <div class="relative bg-white rounded-2xl shadow-xl overflow-hidden">
        <!-- Edit Button -->
        <button
          @click="openModal"
          class="absolute top-4 right-4 bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-lg transition"
        >
          Edit Profile
        </button>

        <div
          class="flex flex-col md:flex-row items-center md:items-start p-8 space-y-6 md:space-y-0 md:space-x-8"
        >
          <!-- Avatar -->
          <div class="flex-shrink-0">
            <img
              :src="profile.profile_picture"
              alt="Avatar"
              class="w-32 h-32 md:w-40 md:h-40 rounded-full object-cover border-4 border-indigo-100 shadow-md"
            />
          </div>
          <!-- Details -->
          <div
            class="flex-1 grid grid-cols-1 md:grid-cols-2 gap-4 text-gray-700"
          >
            <div class="space-y-2">
              <p>
                <span class="font-semibold">Name:</span>
                {{ profile.first_name }}
                {{ profile.last_name }}
              </p>
              <p>
                <span class="font-semibold">Username:</span>
                {{ profile.username }}
              </p>
              <p>
                <span class="font-semibold">Email:</span> {{ profile.email }}
              </p>
              <p>
                <span class="font-semibold">Gender:</span> {{ profile.gender }}
              </p>
              <p>
                <span class="font-semibold">DOB:</span>
                {{ profile.date_of_birth }}
              </p>
            </div>
            <div class="space-y-2">
              <p>
                <span class="font-semibold">Phone:</span>
                {{ profile.phone_number }}
              </p>
              <p>
                <span class="font-semibold">Address:</span>
                {{ profile.address }},
                {{ profile.city }}
              </p>
              <p>
                <span class="font-semibold">State:</span> {{ profile.state }}
              </p>
              <p>
                <span class="font-semibold">Postal Code:</span>
                {{ profile.postal_code }}
              </p>
              <p>
                <span class="font-semibold">Country:</span>
                {{ profile.country }}
              </p>
            </div>
            <div class="md:col-span-2">
              <p class="font-semibold">Bio:</p>
              <p class="text-gray-600">{{ profile.bio }}</p>
            </div>
            <div class="md:col-span-2 grid grid-cols-2 gap-4 mt-4">
              <a
                :href="profile.github_url"
                target="_blank"
                class="flex items-center space-x-2 hover:text-indigo-600 transition"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 text-gray-500"
                  viewBox="0 0 24 24"
                  fill="currentColor"
                >
                  <path
                    d="M12 0C5.37 0 0 5.37 0 12c0 5.3 3.438 9.8 8.205 11.387.6.113.82-.263.82-.583 0-.288-.012-1.244-.017-2.257-3.338.726-4.042-1.61-4.042-1.61-.546-1.387-1.333-1.757-1.333-1.757-1.089-.745.082-.73.082-.73 1.205.085 1.84 1.238 1.84 1.238 1.07 1.834 2.807 1.304 3.492.997.108-.775.42-1.305.763-1.605-2.665-.304-5.467-1.333-5.467-5.933 0-1.31.468-2.382 1.235-3.222-.123-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.98-.399 3-.405 1.02.006 2.043.139 3 .405 2.292-1.552 3.298-1.23 3.298-1.23.653 1.653.241 2.873.118 3.176.77.84 1.233 1.912 1.233 3.222 0 4.61-2.807 5.625-5.48 5.922.431.372.815 1.102.815 2.222 0 1.606-.015 2.898-.015 3.293 0 .322.218.699.825.581C20.565 21.796 24 17.297 24 12c0-6.63-5.37-12-12-12z"
                  />
                </svg>
                <span>GitHub</span>
              </a>
              <a
                :href="profile.linkedin_url"
                target="_blank"
                class="flex items-center space-x-2 hover:text-indigo-600 transition"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 text-gray-500"
                  viewBox="0 0 24 24"
                  fill="currentColor"
                >
                  <path
                    d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.761 0 5-2.239 5-5v-14c0-2.761-2.239-5-5-5zm-11 19h-3v-10h3v10zm-1.5-11.268c-.966 0-1.75-.784-1.75-1.75s.784-1.75 1.75-1.75 1.75.784 1.75 1.75-.784 1.75-1.75 1.75zm13.5 11.268h-3v-5.5c0-1.379-1.121-2.5-2.5-2.5s-2.5 1.121-2.5 2.5v5.5h-3v-10h3v1.5c.829-1.299 2.449-1.5 3.5-1.5 2.481 0 4.5 2.019 4.5 4.5v5.5z"
                  />
                </svg>
                <span>LinkedIn</span>
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- Edit Modal -->
      <div
        v-if="showModal"
        class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
      >
        <div class="bg-white rounded-xl shadow-2xl w-full max-w-2xl p-6">
          <div class="flex justify-between items-center mb-4">
            <h3 class="text-xl font-semibold text-gray-800">Edit Profile</h3>
            <button
              @click="closeModal"
              class="text-gray-500 hover:text-gray-700"
            >
              &times;
            </button>
          </div>
          <form @submit.prevent="updateProfile" class="space-y-4">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <input
                v-model="form.first_name"
                type="text"
                placeholder="First Name"
                class="border rounded-lg p-2 focus:ring-2 focus:ring-indigo-300"
              />
              <input
                v-model="form.last_name"
                type="text"
                placeholder="Last Name"
                class="border rounded-lg p-2 focus:ring-2 focus:ring-indigo-300"
              />
              <input
                v-model="form.gender"
                type="text"
                placeholder="Gender"
                class="border rounded-lg p-2 focus:ring-2 focus:ring-indigo-300"
              />
              <input
                v-model="form.date_of_birth"
                type="date"
                class="border rounded-lg p-2 focus:ring-2 focus:ring-indigo-300"
              />
              <input
                v-model="form.phone_number"
                type="text"
                placeholder="Phone"
                class="border rounded-lg p-2 focus:ring-2 focus:ring-indigo-300"
              />
              <input
                v-model="form.address"
                type="text"
                placeholder="Address"
                class="border rounded-lg p-2 focus:ring-2 focus:ring-indigo-300"
              />
              <input
                v-model="form.city"
                type="text"
                placeholder="City"
                class="border rounded-lg p-2 focus:ring-2 focus:ring-indigo-300"
              />
              <input
                v-model="form.state"
                type="text"
                placeholder="State"
                class="border rounded-lg p-2 focus:ring-2 focus:ring-indigo-300"
              />
              <input
                v-model="form.postal_code"
                type="text"
                placeholder="Postal Code"
                class="border rounded-lg p-2 focus:ring-2 focus:ring-indigo-300"
              />
              <input
                v-model="form.country"
                type="text"
                placeholder="Country"
                class="border rounded-lg p-2 focus:ring-2 focus:ring-indigo-300"
              />
              <input
                v-model="form.github_url"
                type="url"
                placeholder="GitHub URL"
                class="border rounded-lg p-2 focus:ring-2 focus:ring-indigo-300"
              />
              <input
                v-model="form.twitter_url"
                type="url"
                placeholder="Twitter URL"
                class="border rounded-lg p-2 focus:ring-2 focus:ring-indigo-300"
              />
              <input
                v-model="form.linkedin_url"
                type="url"
                placeholder="LinkedIn URL"
                class="border rounded-lg p-2 focus:ring-2 focus:ring-indigo-300"
              />
              <input
                v-model="form.website_url"
                type="url"
                placeholder="Website URL"
                class="border rounded-lg p-2 focus:ring-2 focus:ring-indigo-300"
              />
            </div>
            <div>
              <textarea
                v-model="form.bio"
                rows="4"
                placeholder="Bio"
                class="w-full border rounded-lg p-2 focus:ring-2 focus:ring-indigo-300"
              ></textarea>
            </div>
            <div class="flex justify-end space-x-4">
              <button
                type="button"
                @click="closeModal"
                class="px-4 py-2 bg-gray-300 text-gray-700 rounded-lg hover:bg-gray-400"
              >
                Cancel
              </button>
              <button
                type="submit"
                class="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700"
              >
                Save
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import navbarComp from '../components/navbarComp.vue'

export default {
  name: 'userProfile',
  data() {
    return {
      showModal: false,
      profile: {},
      form: {},
    }
  },
  components: {
    navbarComp,
  },
  methods: {
    async fetchProfile() {
      try {
        const res = await axios.get(
          `http://127.0.0.1:5000/api/user/${this.$store.getters.get_userid}/profile`
        )
        this.profile = res.data.profile
        this.form = { ...res.data.profile }
      } catch (err) {
        console.error('Failed to fetch profile', err)
      }
    },
    openModal() {
      this.showModal = true
    },
    closeModal() {
      this.showModal = false
    },
    async updateProfile() {
      try {
        const res = await axios.put(
          `http://127.0.0.1:5000/api/user/${this.$store.getters.get_userid}/profile`,
          this.form
        )
        this.profile = { ...res.data.profile }
        this.closeModal()
      } catch (err) {
        console.error('Failed to update profile', err)
      }
    },
  },
  created() {
    this.fetchProfile()
  },
}
</script>

<style scoped>
/* Add any additional custom styles here */
</style>
