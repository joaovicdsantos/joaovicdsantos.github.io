import Vue from 'vue';
import i18n from './lang';
import App from './App.vue';

Vue.config.productionTip = false;

new Vue({
  i18n,
  render: h => h(App),
}).$mount('#app');
