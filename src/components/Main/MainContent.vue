<template>
  <div id="container">
    <div>
      <h1>
        {{ $t('main_content.main1') }} <span class="highlight">João Victor</span>. {{ $t('main_content.main2') }}
        <span class="highlight">{{ $t('main_content.main3') }}</span>.
      </h1>
      <h6>{{ $t('main_content.main4') }} <span class="highlight">golang</span> {{ $t('main_content.main5') }}.</h6>
    </div>
    <img src="../../assets/gopher.png" style="width: 300px" id="gopher" />
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
#container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  width: 80%;
  padding: 2% 0;
  color: #ddd;
}

#container h1 {
  font-size: 3rem;
}

span.highlight {
  color: #ff3838;
}

@media (max-width: 576px) {
  #container h1, #container h6 {
    text-align: center;
  }
  #container h1 {
    font-size: 2.9rem;
  }
}

@media (max-width: 768px) {
  img#gopher {
    display: none;
  }
}
</style>
