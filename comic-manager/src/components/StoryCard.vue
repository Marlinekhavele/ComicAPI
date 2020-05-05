<template>
  <div class="story-card">
    <div class="card">
      <div class="card-info">
        <h1 class="title">{{ story.title }}</h1>
        <p class="source">
          From
          <router-link :to="`/comic/${story.comic}`">this comic</router-link>
        </p>
      </div>
    </div>
    <hr class="my-1" />
  </div>
</template>

<script>
export default {
  props: {
    story: Object
  }
};
</script>

<style></style>
