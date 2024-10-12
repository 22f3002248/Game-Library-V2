<template>
  <div class="flex h-screen bg-gray-100">
    <navbarCompVertical />
    <div class="flex-1 p-5">
      <h1 class="text-3xl">Main Content Area</h1>
      <p>This is where your main content will go.</p>
    </div>
  </div>
</template>

<script>
// JS
import navbarCompVertical from '../components/navbarCompVertical.vue'
export default {
  name: 'adminDash',
  components: {
    navbarCompVertical,
  },
  data() {
    return {}
  },
  methods: {},
}
</script>

<style>
/* CSS */
</style>
