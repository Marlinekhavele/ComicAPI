<template>
  <div>
    <navbar />
    <div class="container">
      <subnav />
      <div v-show="loading">
        <loader />
      </div>
      <div class="container-flex">
        <div v-for="creator in creators" :key="creator.id">
          <div class="flex-item">
            <creator-card :creator="creator" />
          </div>
        </div>
      </div>
    </div>
    <footr />
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import Subnav from "@/components/Subnav.vue";
import CreatorCard from "@/components/CreatorCard.vue";

export default {
  components: {
    Subnav,
    CreatorCard
  },
  methods: {
    ...mapActions(["fetchCreators"])
  },
  computed: {
    ...mapGetters(["loading", "creators"])
  },
  created() {
    this.fetchCreators();
  }
};
</script>

<style>
</style>