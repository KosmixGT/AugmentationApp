<template>
  <v-container>
    <v-row justify="center" class="mt-15">
      <v-col cols="12" sm="8" md="6" lg="4">
        <v-card class="pa-5">
          <h2 class="text-center mb-4">Вход</h2>
          <v-form>
            <v-text-field v-model="login" label="Логин" outlined></v-text-field>
            <v-text-field v-model="password" label="Пароль" type="password" outlined></v-text-field>
            <v-btn @click="loginClick" color="primary" class="mt-4" block>Вход</v-btn>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  methods: {
    async getUser(user_login) {
      try {
        const response = await this.$axios.get('/users/' + user_login)
        // Обработка успешной загрузки
        console.log('Пользователь найден:', response.data)
        return response.data.password
      } catch (error) {
        console.error('Пользователь не обнаружен:', error.response)
        return -1
      }
    },
    async loginClick() {
      var passwd = await this.getUser(this.login)
      if (passwd == -1) {
        alert('Пользователь не найден')
      } else if (passwd == this.password) {
        this.$router.push({ name: 'image-upload', params: { login: this.login } })
      } else {
        alert('Неверный пароль')
      }
    }
  },
  data() {
    return {
      login: '',
      password: ''
    }
  }
}
</script>

<style>
.centered {
  display: flex;
  justify-content: center;
  align-items: center;
}
.mt-15 {
    margin-top: 15%;
  }
</style>
