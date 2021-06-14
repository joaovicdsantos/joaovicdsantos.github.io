<template>
  <div class="technology">
    <a v-if="link" :href="link" target="_blank"
      >{{ name }}&nbsp;<img
        src="../../assets/arrow_link.png"
        style="vertical-align: baseline; height: 0.6rem"
    /></a>
    <a v-else>{{ name }}</a>
    <!--
    <div id="stars">
      <img v-bind:src="starsImg[0]" />
      <img v-bind:src="starsImg[1]" />
      <img v-bind:src="starsImg[2]" />
      <img v-bind:src="starsImg[3]" />
      <img v-bind:src="starsImg[4]" />
    </div>
-->
  </div>
</template>

<script>
export default {
  props: ["name", "stars", "link"],
  data: function () {
    var starsImg = Array();
    var half = this.stars % 1;
    var stars = this.stars - half;
    for (var i = 0; i < stars; i++) {
      starsImg[i] = require("@/assets/star.png");
    }
    if (half == 0.5) {
      starsImg[i++] = require("@/assets/star_half.png");
    }
    for (let j = i; j <= 5; j++) {
      starsImg[j] = require("@/assets/star_outline.png");
    }
    return {
      starsImg,
    };
  },
};
</script>

<style scoped>
.technology {
  width: 100%;
  display: flex;
  justify-content: space-between;
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  padding: 8px;
}

.technology:last-child {
  border-bottom: none !important;
}

.technology a {
  font-size: 0.9rem;
  color: #fff;
}

.technology img {
  height: 0.9rem;
}
</style>
