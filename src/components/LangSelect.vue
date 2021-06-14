<template>
  <div class="locale-changer">
    <select v-model="$i18n.locale">
      <option v-for="(lang, i) in langs" :key="`Lang${i}`" :value="lang[0]">
        {{ lang[1] }}
      </option>
    </select>
  </div>
</template>

<script>
export default {
  name: 'locale-changer',
  data () {
    return { langs: [['pt', 'pt-BR'], ['en', 'en-US']] }
  }
}
</script>

<style scoped>
.locale-changer {
  position: fixed;
  z-index: 10;
  bottom: 20px;
  right: 20px;
}
.locale-changer select {
  border: 1px solid #ffffff10;
  border-radius: 5px;
  background-color: #ff383890;
  /* font-weight: bolder; */
  font-size: 16px;
  color: #ffffff90;
  padding: 3px 10px;
}
.locale-changer select:focus {
  outline: 0;
}
.locale-changer select option {
  border: none;
  background-color: #ff3838;
  color: #fff;
}

</style>