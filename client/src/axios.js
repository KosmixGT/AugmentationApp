import axios from 'axios'

const baseURL = 'http://localhost:8000' // Замените на ваш URL сервера

const instance = axios.create({
  baseURL,
  timeout: 5000 // Настройка тайм-аута запросов
})

export default instance
