<template>
  <div id="contact">
    <div id="contact__container">
      <SocialMedia name="joaovicdsantos" imageName="linkedin.png"  link="https://www.linkedin.com/in/joaovicdsantos"/>
      <SocialMedia name="joao_budinha" imageName="twitter.png" link="https://www.twitter.com/joao_budinha"/>
      <SocialMedia name="joaovicdsantos" imageName="github.png" link="https://github.com/joaovicdsantos" />
      <SocialMedia name="joaovicdsantos@" imageName="mail.png" link="mailto:joaovicdsantos@gmail.com" />
    </div>
  </div>
</template>

<script>
import SocialMedia from '../components/Contact/SocialMedia';

export default {
  components: {
    SocialMedia
  }    
}
</script>

<style scoped>
#contact {
  width: 100vw;
  max-width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #ff3838;
}
#contact__container {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  width: 80%;
  padding: 2% 0;
  flex-wrap: wrap;
}
.socialmedia {
  margin: 10px;
}
</style>
