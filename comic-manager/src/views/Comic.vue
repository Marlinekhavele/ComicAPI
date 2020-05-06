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
          <p class="price">$. {{ comic.price }}</p>
          <p class="p-date my-1">Published: {{ commicPublishDate }}</p>
          <button class="btn btn-secondary btn-block btn-flex btn-lg my-2">
            <font-awesome-icon :icon="['fas','shopping-bag']" />
            <span>Add to bag</span>
          </button>
        </div>
      </header>
      <div class="comic-details">
        <h1>Stories</h1>
        <hr />
        <div v-for="story in comicStories" :key="story.id">
          <div class="story btn btn-info btn-lg">{{ story.title }}</div>
        </div>
      </div>
    </div>
    <footr />
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  data() {
    return {
      comicId: this.$route.params.id
    };
  },
  methods: {
    ...mapActions(["fetchComicById", "fetchStoriesByComic"]),
    getComic() {
      this.fetchComicById(this.comicId);
    },
    getStories() {
      this.fetchStoriesByComic(this.comicId);
    }
  },
  computed: {
    ...mapGetters(["loading", "comics", "stories"]),
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
    },
    comicStories() {
      return this.stories;
    }
  },
  created() {
    this.getComic();
    this.getStories();
  }
};
</script>

<style>
</style>