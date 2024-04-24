import { createApp } from 'vue'
import App from './App.vue'
import index from './router'
import axiosInstance from './axios'
import { loadFonts } from './plugins/webfontloader'

loadFonts()

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'

import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives
})

const app = createApp(App)

app.use(vuetify)
app.use(index)
app.config.globalProperties.$axios = axiosInstance

app.mount('#app')
