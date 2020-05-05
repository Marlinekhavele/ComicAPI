import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import Comic from "@/views/Comic.vue";
import Stories from "@/views/Stories.vue";
import Creators from "@/views/creators/Index.vue";
import CreateCreators from "@/views/creators/Register.vue";

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
  {
    path: "/stories",
    name: "Stories",
    component: Stories,
  },
  {
    path: "/creators",
    name: "Creators",
    component: Creators,
  },
  {
    path: "/creators/create",
    name: "CreateCreators",
    component: CreateCreators,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
