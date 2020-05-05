import Vue from "vue";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";

Vue.component("font-awesome-icon", FontAwesomeIcon);

import {
  faSearch,
  faShoppingBag,
  faBars,
  faTimes,
} from "@fortawesome/free-solid-svg-icons";

import {
  faTwitter,
  faFacebook,
  faInstagram,
} from "@fortawesome/free-brands-svg-icons";

library.add(
  faSearch,
  faShoppingBag,
  faBars,
  faTimes,
  faTwitter,
  faFacebook,
  faInstagram
);
