<template>
  <v-container>
    <v-row justify="center" class="mt-15">
      <v-col cols="12" sm="8" md="6" lg="4">
        <v-card class="pa-5">
          <h2 class="text-center mb-4">Регистрация</h2>
          <v-form>
            <v-text-field v-model="login" label="Логин" outlined></v-text-field>
            <v-text-field v-model="password" label="Пароль" type="password" outlined></v-text-field>
            <v-text-field v-model="repeatPassword" label="Повторите пароль" type="password" outlined></v-text-field>
            <v-btn @click="addClick" color="primary" class="mt-4" block>Регистрация</v-btn>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { formToJSON } from 'axios'

export default {
  methods: {
    async getUser(user_login) {
      try {
        const response = await this.$axios.get('/users/' + user_login)
        // Обработка успешной загрузки
        console.log('Пользователь найден:', response.data)
        return response.data.password
      } catch (error) {
        console.error('Пользователь не обнаружен:', error)
        return -1
      }
    },
    async addUser(user_login, user_password) {
      const formData = {
        login: user_login,
        password: user_password
      }

      try {
        const response = await this.$axios.post('/users/register/',formData)
        // Обработка успешной загрузки
        console.log('Пользователь добавлен')
        return true
      } catch (error) {
        console.error('Пользователь не добавлен:', error)
        return false
      }
    },
    async addClick() {
      if (this.password != this.repeatPassword) {
        alert('Пароли не совпадают')
        return
      }

      var passwd = await this.getUser(this.login)
      if (passwd == -1) {
        if (this.login.length < 3) {
          alert('Логин должен содержать не меньше 3 символов')
        } else if (this.password.length < 3) {
          alert('Пароль должен содержать не меньше 3 символов')
        } else if (await this.addUser(this.login, this.password)) {
          alert('Регистрация успешна')
          this.$router.push({ name: 'image-upload', params: { login: this.login } })
        } else {
          alert('Не удалось зарегистрировать пользователя')
        }
      } else {
        alert('Пользователь с таким логином уже существует')
      }
    }
  },
  data() {
    return {
      login: '',
      password: '',
      repeatPassword: ''
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
</style>
