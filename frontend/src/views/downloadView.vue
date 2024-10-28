<template>
  <div>
    <navbar-comp />
    <!-- html code -->
    <button @click="downloadInstaller()">Download</button>
    <div v-if="isWaiting">
      <span class="loading loading-dots loading-lg"></span>
      <span class="loading loading-dots loading-lg"></span>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import navbarComp from '../components/navbarComp.vue'
// JS

export default {
  name: 'downloadView',
  data() {
    return {
      isWaiting: false,
    }
  },
  components: {
    navbarComp: navbarComp,
  },
  methods: {
    async downloadInstaller() {
      this.isWaiting = true
      const res = await fetch('http://127.0.0.1:5000/download-installer')
      const data = await res.json()
      if (res.ok) {
        const taskId = data['task_id']
        const intvl = setInterval(async () => {
          const installer_res = await fetch(
            `http://127.0.0.1:5000/result-download-installer/${taskId}`
          )
          if (installer_res.ok) {
            this.isWaiting = false
            clearInterval(intvl)
            window.location.href = `http://127.0.0.1:5000/result-download-installer/${taskId}`
          }
        }, 1000)
      }
    },
  },
}
</script>

<style>
/* CSS */
</style>
