import axios from "axios";

export default {
  state: {
    stories: [],
  },
  getters: {
    stories: (state) => state.stories,
  },
  mutations: {
    SET_STORIES: (state, stories) => {
      state.stories = stories;
    },
  },
  actions: {
    fetchStories({ commit }, comcicId) {
      commit("SET_LOADING_STATUS", true, { root: true });
      axios
        .get(
          `http://18.203.102.108/api/stories-in-comic/${comcicId}/?format=json`
        )
        .then((res) => {
          commit("SET_STORIES", res.data);
          commit("SET_LOADING_STATUS", false, { root: true });
        })
        .catch((err) => console.log(err));
    },
  },
};
