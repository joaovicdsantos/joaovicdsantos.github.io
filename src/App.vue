<template>
  <div id="app">
    <Main />
    <About />
    <Projects />
    <Contact />
  </div>
</template>

<script>
import Main from "./layouts/Main";
import About from "./layouts/About";
import Projects from "./layouts/Projects";
import Contact from "./layouts/Contact";

export default {
  name: "App",
  components: {
    Main,
    About,
    Projects,
    Contact
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Lato:wght@400;500;600;900&display=swap");

* {
  font-family: "Lato", sans-serif;
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  list-style-type: none;
}

html {
  scroll-behavior: smooth;
}

a {
  color: #000;
  text-decoration: none;
}

div.divider {
  width: 100%;
  border-top: 1px dashed rgba(255, 255, 255, 0.1);
  margin: 2% 0;
}
/* scrollbars */
::-webkit-scrollbar {
  width: 2px;
  height: 2px;
}
::-webkit-scrollbar-button {
  width: 0px;
  height: 0px;
}
::-webkit-scrollbar-thumb {
  background: #0d0d0d;
  border: 0px none #ffffff;
  border-radius: 50px;
}
::-webkit-scrollbar-thumb:hover {
  background: #ffffff;
}
::-webkit-scrollbar-thumb:active {
  background: #000000;
}
::-webkit-scrollbar-track {
  background: #666666;
  border: 0px none #ffffff;
  border-radius: 50px;
}
::-webkit-scrollbar-track:hover {
  background: #666666;
}
::-webkit-scrollbar-track:active {
  background: #333333;
}
::-webkit-scrollbar-corner {
  background: transparent;
}
</style>
