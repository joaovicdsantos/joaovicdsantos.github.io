<template>
  <div class="card">
    <div class="card__title">{{ title }}</div>
    <div class="card__content">
      <slot />
    </div>
  </div>
</template>

<script>
export default {
  props: ["title"],
};
</script>

<style scoped>
.card {
  flex: 1;
  text-align: center;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
  margin: 10px;
  background-color: #e74c3c;
  border-radius: 10px;
}

.card .card__title {
  padding: 15px 10px;
  color: #fff;
  font-weight: bold;
  border-bottom: 1px solid rgba(255, 255, 255, 0.5);
}

.card .card__content {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}
@media (max-width: 576px) {
  .card {
    flex: 0;
    width: 100%;
    margin: 10px 0;
  }
}
</style>
