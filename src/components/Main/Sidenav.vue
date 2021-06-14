<template>
  <div>
    <nav id="sidenav">
      <ul id="sidenav__links">
        <li><a href="#">{{ $t('header.home') }}</a></li>
        <li><a href="#about">{{ $t('header.about') }}</a></li>
        <li><a href="#project">{{ $t('header.project') }}</a></li>
        <li><a href="#contact">{{ $t('header.contact') }}</a></li>
      </ul>
    </nav>
    <div class="containerButtonOpen">
      <a href="#!" class="menuButton"
        ><img src="../../assets/bars.png" alt="" width="35" id="buttonImg"
      /></a>
    </div>
    <div class="containerButtonClose">
      <a href="#!" class="menuButton"
        ><img src="../../assets/close.png" alt="" width="35" id="buttonImg"
      /></a>
    </div>
  </div>
</template>

<script>
export default {
  mounted: function() {
    const menuButton = document.querySelectorAll(".menuButton");
    const sideNav = document.querySelector("#sidenav");
    const botaoAbrido = document.querySelector(".containerButtonOpen");
    const botaoFechado = document.querySelector(".containerButtonClose");

    menuButton.forEach((botao) => {
      botao.addEventListener("click", function() {
        if (sideNav.style.width != "80vw") {
          sideNav.style.width = "80vw";
          botaoAbrido.style.display = "none";
          botaoFechado.style.display = "block";
        } else {
          sideNav.style.width = "0";
          botaoAbrido.style.display = "block";
          botaoFechado.style.display = "none";
        }
      });
    });
  },
};
</script>

<style scoped>
nav#sidenav {
  position: fixed;
  right: 0;
  top: 0;
  width: 0; /* 80vw */
  height: 100vh;
  transition: width 0.5s;
  background-color: rgba(0, 0, 0, 0.9);
}

ul#sidenav__links li {
  margin: 40px 25px;
}

ul#sidenav__links li a {
  color: #ddd;
  text-transform: uppercase;
  font-weight: bold;
  border-bottom: 2px solid rgba(255, 0, 0, 0.3);
}

.containerButtonOpen,
.containerButtonClose {
  position: fixed;
  top: 3.5vh;
  right: 5vw;
  display: none;
}

@media (max-width: 576px) {
  div.containerButtonOpen {
    display: block;
  }
  div.containerButtonClose {
    display: none;
  }
}

@media (min-width: 576px) {
  div.containerButtonOpen, div.containerButtonClose {
    display: none;
  }
}

</style>
