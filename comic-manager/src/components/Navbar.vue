<template>
  <nav class="navbar">
    <div class="nav-wrapper">
      <button class="nav-toggle" @click="toggleNav">
        <font-awesome-icon :icon="['fas', 'bars']" />
      </button>
      <div class="logo">
        <router-link to="/">ComicHub</router-link>
      </div>
      <ul class="nav-items">
        <div class="nav-ctrls">
          <div class="logo">
            <router-link to="/">ComicHub</router-link>
          </div>
          <button class="btn-rounded btn-neutral" @click="toggleNav">
            <font-awesome-icon :icon="['fas', 'times']" />
          </button>
        </div>
        <li class="nav-item">
          <router-link to="/stories">Stories</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/creators">Creators</router-link>
        </li>
      </ul>
      <div class="nav-controlls">
        <router-link to="#!">
          <font-awesome-icon :icon="['fas', 'search']" />
        </router-link>
        <router-link to="#!">
          <font-awesome-icon :icon="['fas', 'shopping-bag']" />
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  methods: {
    toggleNav() {
      const navItems = document.querySelector(".nav-items");

      if (navItems.classList.contains("show")) {
        navItems.classList.remove("show");
        document.body.classList.remove("overlay");
        document.body.classList.remove("overflow-hidden");
      } else {
        navItems.classList.add("show");
        document.body.classList.add("overlay");
        document.body.classList.add("overflow-hidden");
      }

      window.onmouseup = (event) => {
        if (event.target.closest(".nav-items")) return;
        navItems.classList.remove("show");
        document.body.classList.remove("overlay");
        document.body.classList.remove("overflow-hidden");
      };
    },
  },
};
</script>

<style></style>
