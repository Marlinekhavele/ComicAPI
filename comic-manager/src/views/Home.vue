<template>
  <div>
    <navbar />
    <div class="container">
      <div v-show="loading">
        <loader />
      </div>
      <div class="container-flex">
        <div v-for="comic in comics" :key="comic.id">
          <div class="flex-item">
            <card :comic="comic" />
          </div>
        </div>
      </div>
    </div>
    <footr />
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

import Navbar from "@/components/Navbar.vue";
import Card from "@/components/Card.vue";
import Footr from "@/components/Footr.vue";

export default {
  components: {
    Navbar,
    Card,
    Footr
  },
  methods: {
    ...mapActions(["fetchComics"])
  },
  computed: {
    ...mapGetters(["loading", "comics"])
  },
  created() {
    this.fetchComics();
  }
};
</script>

<style>
</style>