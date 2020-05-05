 
<template>
  <div class="creator-registration">
    <navbar />
    <div class="container">
      <h1>Welcome to ComicHub</h1>
      <div v-show="fb">
        <div class="fb-box">
          <p>{{ fb }}</p>
        </div>
      </div>
      <form id="registerCreator" @submit.prevent="register" autocomplete="off">
        <div class="form-group">
          <label for="name" class="label">Name</label>
          <input type="text" v-model="creator.name" id="name" class="input" placeholder="Name" />
        </div>
        <div class="form-group mx-auto">
          <label for="description" class="label">Description</label>
          <textarea
            v-model="creator.description"
            id="description"
            cols="30"
            rows="10"
            class="input"
            placeholder="Description"
          ></textarea>
        </div>
        <button type="submit" class="btn btn-secondary btn-half-block">Register</button>
      </form>
    </div>
    <footr />
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      creator: {
        name: null,
        description: null
      },
      fb: null
    };
  },
  methods: {
    register() {
      if (!this.creator.name) {
        this.fb = "Please fill out the name";
        return false;
      } else if (!this.creator.description) {
        this.fb = "Please fill out the description";
        return false;
      } else {
        this.fb = null;
        axios
          .post("http://52.49.227.229/api/creator/", this.creator)
          .then(() => {
            this.creator.name = null;
            this.creator.description = null;
            this.fb = "Successfully registered creator";
            return true;
          })
          .catch(err => console.log(err));
      }
    }
  }
};
</script>

<style>
</style>