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
            <comic-card :comic="comic" />
          </div>
        </div>
      </div>
    </div>
    <footr />
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import ComicCard from "@/components/ComicCard.vue";

export default {
  components: {
    ComicCard
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