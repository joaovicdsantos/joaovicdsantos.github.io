<template>
  <header>
    <div id="container">
      <div id="container__logo">
        <a href="."><h1 id="logo">Budinha</h1></a>
      </div>
      <nav id="links">
        <ul>
          <li><a href="#about">{{ $t('header.about') }}</a></li>
          <li><a href="#projects">{{ $t('header.project') }}</a></li>
          <li><a href="#contact">{{ $t('header.contact') }}</a></li>
        </ul>
      </nav>
    </div>
    <Sidenav />
  </header>
</template>

<script>
import Sidenav from "./Sidenav";

export default {
  components: {
    Sidenav,
  },
};
</script>

<style scoped>
@font-face {
  font-family: Logo;
  src: url("../../assets/fonts/Playlist Script.otf");
}

header {
  display: flex;
  justify-content: center;
  /* box-shadow: 1px 1px 10px rgba(0, 0, 0, .2); */
  width: 100%;
}

#container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  width: 80%;
  padding: 2% 0;
}

#container__logo {
  width: 100%;
}

#logo {
  font-family: Logo;
  font-size: 2.5rem;
  text-shadow: 2px 2px rgba(0, 0, 0, 0.3);
  color: #ddd;
}

header ul {
  list-style: none;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  width: 300px;
}

header ul li a {
  font-weight: bold;
  text-transform: uppercase;
  font-size: 0.9rem;
  text-shadow: 2px 2px rgba(0, 0, 0, 0.2);
  color: #ddd;
  padding-bottom: 2px;
  border-bottom: 2px solid rgba(255, 0, 0, 0.3);
}

@media (max-width: 576px) {
  img#gopher {
    display: none;
  }
  nav#links {
    display: none;
  }
  header #container {
    padding: 4% 0;
  }
  #container__logo {
    text-align: center;
  }
}
</style>
