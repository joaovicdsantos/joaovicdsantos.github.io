<template>
    <a v-bind:href="link"><img src="../assets/seta.png" id="arrow"></a>
</template>

<script>
export default {
    props: ['link']
}
</script>

<style scoped>

img#arrow {
    width: 30px;
}

</style>