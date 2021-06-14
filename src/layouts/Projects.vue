<template>
  <div id="projects">
    <div id="projects__container">
      <Topic
        :title="$t('projects_content.title')"
        title_color="#fff"
        class="title"
      />
      <div id="projects__group">
        <Project :title="$t('projects_content.projects.budajuda.title')" :description="$t('projects_content.projects.budajuda.description')"  imgName="budajuda.budaportfolio.epizy.com.png" link="http://budajuda.budaportfolio.epizy.com"/>
        <Project :title="$t('projects_content.projects.trasle.title')" :description="$t('projects_content.projects.trasle.description')"  imgName="trasle.png" link="https://trasle-cloud.gq"/>
        <Project :title="$t('projects_content.projects.trasle_cloud.title')" :description="$t('projects_content.projects.trasle_cloud.description')"  imgName="trasle-cloud.png" link="https://trasle-cloud.gq"/>
      </div>
    </div>
  </div>
</template>

<script>
import Topic from "../components/Topic";
import Project from "../components/Projects/Project";

export default {
  components: {
    Topic,
    Project
  },
};
</script>

<style scoped>
#projects {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  min-height: 100vh;
  width: 100vw;
  max-width: 100%;
  background-color: #111;
}
#projects__container {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  width: 80%;
  padding: 2% 0;
}
#projects__container .title {
  flex: 3;
  display: flex;
  align-items: center;
}
#projects__group {
  display: flex;
  flex: 4;
  width: 100%;
  flex-wrap: wrap;
  justify-content: space-between;
}
</style>
