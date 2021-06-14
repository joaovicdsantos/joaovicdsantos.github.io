<template>
    <div>
      <h1 class="title">{{ title }}</h1>
      <p class="description">
        {{ description }}
      </p>
    </div>
</template>

<script>
export default {
    props: [
        'title', 'description'
    ]
}
</script>

<style scoped>

.title {
  color: #ff3838;
  font-size: 2.5rem;
  text-shadow: 2px 2px rgba(0, 0, 0, 0.3);
  margin-bottom: 20px;
}

.description {
  font-size: 1.1rem;
  font-weight: 100;
}
</style>