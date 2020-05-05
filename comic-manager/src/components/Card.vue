<template>
  <div>
    <div class="card">
      <div class="card-burner">
        <router-link :to="`/comic/${comic.id}`">
          <img :src="comic.image" :alt="comic.title" height="100%" />
        </router-link>
      </div>
      <div class="card-info">
        <router-link :to="`/comic/${comic.id}`">
          <h1 class="title">{{ comic.title }}</h1>
        </router-link>
        <p
          class="author"
        >{{ comic.issue.charAt(0).toUpperCase() + comic.issue.slice(1) }} - {{ comic.pages }}pages</p>
        <p class="price">Ksh. {{ comic.price }}</p>
      </div>
    </div>
    <hr class="my-1" />
  </div>
</template>

<script>
export default {
  props: {
    comic: Object
  }
};
</script>

<style></style>
