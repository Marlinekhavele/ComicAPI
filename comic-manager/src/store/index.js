import Vue from "vue";
import Vuex from "vuex";
import stories from "./modules/stories";
import comics from "./modules/comics";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    loading: false,
  },
  getters: {
    loading: (state) => state.loading,
  },
  mutations: {
    SET_LOADING_STATUS(state, loading) {
      state.loading = loading;
    },
  },
  modules: {
    stories,
    comics,
  },
});
