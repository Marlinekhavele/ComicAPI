import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import Stories from "@/views/Stories.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/stories/:id",
    name: "Stories",
    component: Stories,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
