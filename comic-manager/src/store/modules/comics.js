import axios from "axios";

export default {
  state: {
    comics: [],
  },
  getters: {
    comics: (state) => state.comics,
  },
  mutations: {
    SET_COMICS: (state, comics) => {
      state.comics = comics;
    },
  },
  actions: {
    fetchComics({ commit }) {
      commit("SET_LOADING_STATUS", true, { root: true });
      axios
        .get("http://52.49.227.229/api/comic/?format=json")
        .then((res) => {
          commit("SET_LOADING_STATUS", false, { root: true });
          commit("SET_COMICS", res.data);
        })
        .catch((err) => console.log(err));
    },
    fetchComicById({ commit }, comicId) {
      commit("SET_LOADING_STATUS", true, { root: true });
      axios
        .get(`http://52.49.227.229/api/comic/${comicId}/?format=json`)
        .then((res) => {
          commit("SET_LOADING_STATUS", false, { root: true });
          commit("SET_COMICS", res.data);
        })
        .catch((err) => console.log(err));
    },
  },
};
