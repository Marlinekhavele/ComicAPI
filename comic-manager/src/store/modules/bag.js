export default {
  state: {
    items: [],
  },
  getters: {
    items: (state) => state.items,
  },
  mutations: {
    SET_ITEMS: (state, items) => (state.items = items),
  },
  actions: {
    fetchStories({ commit }, item) {
      commit("SET_ITEMS", item);
    },
  },
};
