<template>
  <div class="frontDIV min-h-screen">
    <nav class="bg-grey text-white w-full min-h-screen p-5 shadow-lg">
      <h2 class="text-2xl font-bold mb-6 text-center bg-primary-content text-accent p-2 rounded-lg">
        ADMIN
      </h2>
      <ul class="space-y-4">
        <li>
          <a href="#" class="block text-white hover:bg-accent p-3 rounded-lg">
            Home
          </a>
        </li>
        <li>
          <a href="http://localhost:5173/admin/allgames" class="block text-white hover:bg-accent p-3 rounded-lg">
            Game Library
          </a>
        </li>
        <li>
          <a href="http://localhost:5173/admin/games" class="block text-white hover:bg-accent p-3 rounded-lg">
            Add Game
          </a>
        </li>
        <li>
          <a href="http://localhost:5173/admin/genre" class="block text-white hover:bg-accent p-3 rounded-lg">
            Add Genre
          </a>
        </li>
        <li>
          <a href="#" class="block text-white hover:bg-accent p-3 rounded-lg">
            Manage Users
          </a>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
// JS
export default {
  name: 'navbarCompVertical',
  data() {
    return {}
  },
  props: {},
  methods: {},
}
</script>

<style>
/* CSS */
.frontDIV{
  width: 20%;
}

</style>
