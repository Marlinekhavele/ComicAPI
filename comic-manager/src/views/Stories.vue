<template>
  <div>
    <navbar />
    <div class="container">
      <div v-show="loading">
        <loader />
      </div>
      <div class="container-flex">
        <div v-for="story in stories" :key="story.id">
          <div class="flex-item">
            <story-card :story="story" />
          </div>
        </div>
      </div>
    </div>
    <footr />
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import StoryCard from "@/components/StoryCard.vue";

export default {
  components: {
    StoryCard
  },
  methods: {
    ...mapActions(["fetchStories"])
  },
  computed: {
    ...mapGetters(["loading", "stories"])
  },
  created() {
    this.fetchStories();
  }
};
</script>

<style>
</style>