import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import Comic from "@/views/Comic.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/comic/:id",
    name: "Comic",
    component: Comic,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
