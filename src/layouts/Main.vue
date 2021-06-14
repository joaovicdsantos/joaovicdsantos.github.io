<template>
  <div id="main">
    <Header />
    <MainContent />
    <Arrow link="#about" />
    <LangSelect />
  </div>
</template>

<script>
import Header from "../components/Main/Header";
import MainContent from "../components/Main/MainContent";
import Arrow from "../components/Arrow";
import LangSelect from "../components/LangSelect";

export default {
  components: {
    Header,
    MainContent,
    Arrow,
    LangSelect
  },
};
</script>

<style scoped>
div#main {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  background: url("../assets/banner.jpg") no-repeat center top;
  background-attachment: fixed;
  background-size: cover;
  height: 100vh;
  width: 100vw;
  max-width: 100%;
}
</style>
