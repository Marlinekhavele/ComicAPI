import axios from "axios";

export default {
  state: {
    characters: [],
  },
  getters: {
    characters: (state) => state.characters,
  },
  mutations: {
    SET_CHARACTERS: (state, characters) => {
      state.characters = characters;
    },
  },
  actions: {
    fetchCharacters({ commit }) {
      commit("SET_LOADING_STATUS", true, { root: true });
      axios
        .get("http://52.49.227.229/api/character/?format=json")
        .then((res) => {
          commit("SET_LOADING_STATUS", false, { root: true });
          commit("SET_CHARACTERS", res.data);
        })
        .catch((err) => console.log(err));
    },
    fetchCharacterById({ commit }, characterId) {
      commit("SET_LOADING_STATUS", true, { root: true });
      axios
        .get(`http://52.49.227.229/api/character/${characterId}/?format=json`)
        .then((res) => {
          commit("SET_LOADING_STATUS", false, { root: true });
          commit("SET_CHARACTERS", res.data);
        })
        .catch((err) => console.log(err));
    },
  },
};
