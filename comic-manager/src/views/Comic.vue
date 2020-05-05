<template>
  <div>
    <navbar />
    <div class="container">
      <div v-show="loading">
        <loader />
      </div>
      <header class="comic-header">
        <div class="comic-burner">
          <img :src="comic.image" :alt="comic.title" height="100%" />
        </div>
        <div class="comic-info">
          <h1 class="title">{{ comic.title }}</h1>
          <p class="author">{{ comicIssue }} - {{ comic.pages }}pages</p>
          <p class="price">Ksh. {{ comic.price }}</p>
          <p class="p-date my-1">Published: {{ commicPublishDate }}</p>
          <button class="btn btn-secondary btn-block btn-flex my-2">
            <font-awesome-icon :icon="['fas','shopping-bag']" />
            <span>Add to bag</span>
          </button>
        </div>
      </header>
    </div>
    <footr />
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

import Navbar from "@/components/Navbar.vue";
import Footr from "@/components/Footr.vue";

export default {
  components: {
    Navbar,
    Footr
  },
  data() {
    return {
      comicId: this.$route.params.id
    };
  },
  methods: {
    ...mapActions(["fetchComicById"]),
    getComic() {
      this.fetchComicById(this.comicId);
    }
  },
  computed: {
    ...mapGetters(["loading", "comics"]),
    comic() {
      return this.comics;
    },
    comicIssue() {
      return (
        this.comics.issue.charAt(0).toUpperCase() + this.comics.issue.slice(1)
      );
    },
    commicPublishDate() {
      const publishDate = new Date(this.comic.date_published);
      return publishDate.toString();
    }
  },
  created() {
    this.getComic();
  }
};
</script>

<style>
</style>