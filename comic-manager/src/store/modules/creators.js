import axios from "axios";

export default {
  state: {
    creators: [],
  },
  getters: {
    creators: (state) => state.creators,
  },
  mutations: {
    SET_CREATORS: (state, creators) => {
      state.creators = creators;
    },
  },
  actions: {
    fetchCreators({ commit }) {
      commit("SET_LOADING_STATUS", true, { root: true });
      axios
        .get("http://52.49.227.229/api/creator/?format=json")
        .then((res) => {
          commit("SET_LOADING_STATUS", false, { root: true });
          commit("SET_CREATORS", res.data);
        })
        .catch((err) => console.log(err));
    },
    fetchCreatorById({ commit }, creatorId) {
      commit("SET_LOADING_STATUS", true, { root: true });
      axios
        .get(`http://52.49.227.229/api/creator/${creatorId}/?format=json`)
        .then((res) => {
          commit("SET_LOADING_STATUS", false, { root: true });
          commit("SET_CREATOR", res.data);
        })
        .catch((err) => console.log(err));
    },
  },
};
