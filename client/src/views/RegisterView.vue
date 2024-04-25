<template>
  <v-container>
    <div class="centered" style="margin-top: 15%">
      <div style="font-size: 24px">
        <h2 style="margin-bottom: 15px">Регистрация</h2>
        <strong><p>Логин:</p></strong>
        <input
          style="margin-top: 5px; border: 1px solid; text-indent: 7px"
          v-model="login"
          placeholder="Введите логин"
        />
        <p style="margin-top: 10px"></p>
        <strong><p>Пароль:</p></strong>
        <input
          type="password"
          style="margin-top: 5px; border: 1px solid; text-indent: 7px"
          v-model="password"
          placeholder="Введите пароль"
        />
        <p style="margin-top: 10px"></p>
        <strong><p>Повторите пароль:</p></strong>
        <input
          type="password"
          style="margin-top: 5px; border: 1px solid; text-indent: 7px"
          v-model="repeatPassword"
          placeholder="Повторите пароль"
        />
        <p style="margin-top: 15px"></p>
        <button
          v-on:click="addClick"
          style="margin-top: 15px; border: 1px solid; background-color: aqua; width: 80%"
        >
          Регистрация
        </button>
        <br />
      </div>
    </div>
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
        const response = await this.$axios.post('/users/register/', null, { formData })
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
