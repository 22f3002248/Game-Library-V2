<script setup></script>

<template>
  <div>
    <router-view></router-view>
    <div style="margin-bottom: 50px"></div>
    <hr />
    <div class="container mx-auto">
      <br />
      <div
        class="text-center italic mx-auto w-[400px] text-2xl text-grey-300 font-bold border border-white-400 p-2 rounded-lg"
      >
        Contact US:
      </div>
      <br />
      <footer
        class="mt-auto p-5 bg-neutral text-neutral-content"
        style="margin-bottom: -29px"
      >
        <div class="flex justify-between">
          <div>
            <p>Email: support@gamevault.com</p>
          </div>
          <div>
            <h3 class="text-lg font-bold">Newsletter</h3>
            <p>Sign up for the latest news and updates.</p>
            <br />
            <button class="btn btn-sm btn-accent">Subscribe</button>
          </div>
        </div>
      </footer>
      <div class="text-center mt-8">
        <p>&copy; 2025 GameVault. All rights reserved.</p>
        <p>Privacy Policy | Terms of Service</p>
      </div>
      <div style="margin-bottom: -300px"></div>
    </div>
  </div>
</template>

<style>
.container {
  max-width: 1200px;
}
</style>
