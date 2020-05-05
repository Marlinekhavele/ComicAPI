<template>
  <div class="creator-card">
    <details>
      <summary>{{creator.name}}</summary>
      <p>{{ creator.description }}</p>
    </details>
  </div>
</template>

<script>
export default {
  props: {
    creator: Object
  }
};
</script>

<style>
</style>