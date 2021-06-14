<template>
  <div>
    <h1 class="title" :style="title_color_css">{{ title }}</h1>
    <p class="description" :style="description_color_css">
      {{ description }}
    </p>
  </div>
</template>

<script>
export default {
  props: ["title", "description", "title_color", "description_color"],
  computed: {
    title_color_css() {
      return {
        "--title-color": this.title_color ? this.title_color : "#ff3838",
      };
    },
    description_color_css() {
      return {
        "--description-color": this.title_color ? this.title_color : "#000",
      };
    },
  },
};
</script>

<style scoped>
.title {
  color: var(--title-color);
  font-size: 2.5rem;
  text-shadow: 2px 2px rgba(0, 0, 0, 0.3);
  margin-bottom: 20px;
}

.description {
  color: var(--description-color);
  font-size: 1.1rem;
  font-weight: 100;
}
</style>
