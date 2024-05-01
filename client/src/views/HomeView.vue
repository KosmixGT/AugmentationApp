<template>
  <v-container>
    <!-- Заголовок и описание -->
    <v-row justify="center">
      <v-col cols="12">
        <h1 class="text-center">Добро пожаловать на сайт аугментации изображений!</h1>
        <div class="text-center">
          <p class="headline">Улучшите ваши изображения с помощью наших инструментов аугментации:</p>
          <!-- Список параметров аугментации -->
          <v-list dense>
            <v-list-item>
              <v-list-item-title style="font-size: 25px;">Процент аугментации</v-list-item-title>
              <v-list-item-title style="font-size: 25px;">Угол поворота</v-list-item-title>
              <v-list-item-title style="font-size: 25px;">Шум</v-list-item-title>
              <v-list-item-title style="font-size: 25px;">Контраст</v-list-item-title>
              <v-list-item-title style="font-size: 25px;">Яркость</v-list-item-title>
            </v-list-item>
            <!-- Другие параметры -->
          </v-list>
        </div>
      </v-col>
    </v-row>
    
    <!-- Пример аугментации -->
    <h2 class="text-center mt-8">Пример аугментации</h2>
    <img class="centered" style="width: 100%; transform: scale(0.8);" src="../assets/HomeAug1.jpg" />

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
