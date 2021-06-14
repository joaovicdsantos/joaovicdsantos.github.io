<template>
  <div id="about">
    <div id="about__container">

      <Topic
        :title="$t('about_content.title')"
        :description="$t('about_content.description')"
      />

      <div class="cards">
        <Card :title="$t('about_content.back_tech')">
          <Technology name="Golang" stars="3" link="https://github.com/joaovicdsantos?tab=repositories&q=&type=&language=go" />
          <Technology name="Javascript" stars="4" link="https://github.com/joaovicdsantos?tab=repositories&q=&type=&language=javascript" />
          <Technology name="PHP" stars="4" link="https://github.com/joaovicdsantos?tab=repositories&q=&type=&language=php" />
          <Technology name="Python" stars="3" />
          <Technology name="Ruby" stars="3" />
        </Card>
        <Card :title="$t('about_content.front_tech')">
          <Technology name="HTML" stars="5" />
          <Technology name="CSS" stars="5" />
          <Technology name="Vue" stars="4" />
          <Technology name="React" stars="4" />
          <Technology name="SASS" stars="4" />
          <Technology name="Webpack" stars="4" />
        </Card>
        <Card :title="$t('about_content.extra')">
          <Technology name="Linux" stars="4" />
          <Technology name="Scrum" stars="4" />
          <Technology name="Heroku" stars="4" />
        </Card>
      </div>

      <Arrow link="#projects" />
    </div>
  </div>
</template>

<script>
import Topic from "../components/Topic";
import Card from "../components/About/Card";
import Technology from "../components/About/Technology";
import Arrow from "../components/Arrow";

export default {
  components: {
    Arrow,
    Topic,
    Card,
    Technology
  }
};
</script>

<style scoped>
#about {
  width: 100vw;
  min-height: 100vh;
  max-width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

#about__container {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  width: 80%;
  padding: 2% 0;
}

.cards {
  display: flex;
  flex-wrap: wrap;
  width: 100%;
  margin: 30px 0;
  align-items: stretch;
}

@media (max-width: 576px) {
  .cards {
    display: initial;
  }
}
</style>
