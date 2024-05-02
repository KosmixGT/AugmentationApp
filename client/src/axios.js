import axios from 'axios'

//const baseURL = 'http://backend:5000' // Замените на ваш URL сервера
const baseURL = 'http://gardunov.duckdns.org:7505'
//const baseURL = 'http://localhost:7505'

const instance = axios.create({
  baseURL,
  timeout: 500000 // Настройка тайм-аута запросов
})

export default instance
