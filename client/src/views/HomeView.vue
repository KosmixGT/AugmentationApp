<template>
  <v-container>
    <h1 class="centered">Добро пожаловать на сайт аугментации изображений!</h1>
    <div class="centered">
      <div>
        <p style="font-size: 27px">Здесь вы можете провести агументацию по:</p>
        <div style="font-size: 20px">
          <p>1. Параметр 1</p>
          <p>2. Параметр 2</p>
          <p>3. Параметр 3</p>
          <p>4. Параметр 4</p>
        </div>
      </div>
    </div>

    <h2 class="centered" style="margin-top: 10%">Как выглядит аугментация</h2>
    <img class="centered" style="width: 100%" src="../assets/HomeAug1.jpg" />

    <p><RouterLink to="/login">Вход</RouterLink></p>
    <p><RouterLink to="/register">Регистрация</RouterLink></p>
  </v-container>
</template>

<style>
.centered {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>

<script>
import { defineComponent } from 'vue'

// Components
import HelloWorld from '../components/HelloWorld.vue'

export default defineComponent({
  name: 'HomeView',

  components: {
    HelloWorld
  }
})
</script>
