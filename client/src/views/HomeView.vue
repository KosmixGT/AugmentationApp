<template>
  <v-container>
    <!-- Заголовок и описание -->
    <v-row justify="center">
      <v-col cols="12">
        <h1 class="text-center">Добро пожаловать на сайт аугментации изображений!</h1>
        <div class="text-center">
          <p class="headline">Здесь вы можете провести агументацию по различным параметрам:</p>
          <!-- Список параметров аугментации -->
          <div class="text-left centered">
            <v-list dense>
              <v-list-item>
                <v-list-item-title style="font-size: 25px;">1. Процент аугментации</v-list-item-title>
                <v-list-item-title style="font-size: 25px;">2. Угол поворота</v-list-item-title>
                <v-list-item-title style="font-size: 25px;">3. Шум</v-list-item-title>
                <v-list-item-title style="font-size: 25px;">4. Контраст</v-list-item-title>
                <v-list-item-title style="font-size: 25px;">5. Яркость</v-list-item-title>
              </v-list-item>
              <!-- Другие параметры -->
            </v-list>
          </div>
        </div>
      </v-col>
    </v-row>

    <!-- Пример аугментации -->
    <h2 class="text-center mt-12"  style="font-size: 26px;">Пример аугментации</h2>
    <p class="text-center"><img style="width: 90%;" src="../assets/HomeAug1.jpg" /></p>

    <!-- Кнопки для входа и регистрации -->
    <v-row justify="center" class="mt-8">
      <v-col cols="12" class="text-center">
        <router-link to="/login" class="text-decoration-none">
          <v-btn color="primary" class="mr-4">Вход</v-btn>
        </router-link>
        <router-link to="/register" class="text-decoration-none">
          <v-btn color="primary">Регистрация</v-btn>
        </router-link>
      </v-col>
    </v-row>
  </v-container>
</template>


<style>
.centered {
  display: flex;
  justify-content: center;
  align-items: center;
}

.headline {
  font-size: 27px;
}

</style>

<script>
export default {
  name: 'HomeView'
}
</script>
