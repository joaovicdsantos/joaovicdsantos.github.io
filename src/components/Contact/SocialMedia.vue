<template>
  <a v-bind:href="link" target="blank" class="socialmedia">
    <img v-bind:src="imageLink" />
    <span>/{{ name }}</span>
  </a>
</template>

<script>
export default {
  props: [
    'name',
    'imageName',
    'link'
  ],
  data: function() {
    var imageLink = require('@/assets/socialmedias/' + this.imageName);
    return { imageLink }
  }
}
</script>

<style scoped>
.socialmedia {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.socialmedia span {
  color: #fff;
  font-size: 1.1rem;
}
.socialmedia img {
  width: 1.1rem;
}
</style>