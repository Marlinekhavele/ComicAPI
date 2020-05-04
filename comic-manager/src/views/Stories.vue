<template>
  <div>
    <navbar />
    <div class="content">
      <div v-if="loading">
        <loader />
      </div>
      <div v-show="!loading">
        <header class="story-header">
          <div class="story-burner">
            <img :src="comic.image" :alt="comic.title" height="100%" />
          </div>
          <div class="story-info">
            <h1 class="title">{{ comic.title }}</h1>
            <p class="author">{{ comicIssue }} - {{ comic.pages }}pages</p>
            <p class="price">Ksh. {{ comic.price }}</p>
            <p class="p-date">Published: {{ commicPublishDate }}</p>
          </div>
        </header>
        <div class="story-details">
          <button class="btn btn-secondary btn-block btn-flex my-2">
            <font-awesome-icon :icon="['fas','shopping-bag']" />
            <span>Add to bag</span>
          </button>
        </div>
      </div>
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