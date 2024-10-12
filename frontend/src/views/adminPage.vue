<template>
  <div class="flex h-screen bg-gray-100">
    <div class="w-64 h-full bg-base-200 shadow-md flex flex-col">
      <h1 class="text-2xl font-bold text-center py-4">Navigation</h1>
      <ul class="menu p-2 flex-1">
        <li>
          <a
            href="#"
            class="menu-item flex items-center p-3 hover:bg-base-300 transition duration-200 rounded"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="w-6 h-6 mr-2"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M3 3h18M3 12h18m-7 9h7"
              />
            </svg>
            Dashboard
          </a>
        </li>
        <li>
          <a
            href="#"
            class="menu-item flex items-center p-3 hover:bg-base-300 transition duration-200 rounded"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="w-6 h-6 mr-2"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M3 6h18M3 12h18m-7 6h7"
              />
            </svg>
            Profile
          </a>
        </li>
        <li>
          <a
            href="#"
            class="menu-item flex items-center p-3 hover:bg-base-300 transition duration-200 rounded"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="w-6 h-6 mr-2"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M5 13h14l-7 7m0 0l-7-7m7 7V6"
              />
            </svg>
            Settings
          </a>
        </li>
        <li>
          <a
            href="#"
            class="menu-item flex items-center p-3 hover:bg-base-300 transition duration-200 rounded"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="w-6 h-6 mr-2"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M15 12h3m-3 4h3m-3-8h3m-8 12h5m-5-8h3m-3 4h3"
              />
            </svg>
            Messages
          </a>
        </li>
        <li>
          <a
            href="#"
            class="menu-item flex items-center p-3 hover:bg-base-300 transition duration-200 rounded"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="w-6 h-6 mr-2"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M10 14l2 2 4-4m-6-6h4M4 4h16v16H4z"
              />
            </svg>
            Logout
          </a>
        </li>
      </ul>
    </div>
    <div class="flex-1 p-5">
      <h1 class="text-3xl">Main Content Area</h1>
      <p>This is where your main content will go.</p>
    </div>
  </div>
</template>

<script>
// JS
export default {
  name: 'adminPage',
  data() {
    return {}
  },
  methods: {},
}
</script>

<style>
/* CSS */
</style>
