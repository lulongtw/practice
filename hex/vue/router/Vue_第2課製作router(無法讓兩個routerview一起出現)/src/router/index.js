import {createRouter,createWebHistory} from "vue-router";
import mainView from "../views/mainView.vue";
import footView from "../views/footView.vue";
import aView from "../views/aView.vue";
import bView from "../views/bView.vue";
import cView from "../views/cView.vue"

const routes = [
  {
    path: '/component1',
    name: 'component1',
    components: {
      view1: mainView,
    },
  },
  {
    path: '/component2',
    name: 'component2',
    components: {
      view1: footView,
    },
  },
  {
    path: '/component3',
    name: 'component3',
    components: {
      view2: aView,
    },
  },
  {
    path: '/component4',
    name: 'component4',
    components: {
      view2: bView,
    },
  },
  {
    path: '/component5',
    name: 'component5',
    components: {
      view2: cView,
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
