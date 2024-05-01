<template>
  <v-container>
    <v-card>
      <v-card-title>Аугментация изображений</v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="12">
            <p>
              Для начала аугментации загрузите изображения. Вы также можете загрузить их в виде
              zip-архива.
            </p>
          </v-col>
          <v-col cols="12">
            <p>Загружено изображений: {{ images.length }}</p>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <v-file-input color="primary" label="Выберите изображения или zip архив" multiple accept="image/*,.zip"
              @change="handleFileInputChange"></v-file-input>
          </v-col>
        </v-row>
        <v-row v-if="images.length > 0">
          <v-col v-for="(image, index) in displayedImages" :key="index" cols="12" sm="6" md="4">
            <v-img :src="image.url" style="transform: scale(0.7);" contain></v-img>
          </v-col>
        </v-row>
        <v-row v-if="images.length > 3">
          <v-col cols="12">
            <v-btn color="primary" @click="toggleImages">
              <v-icon left>mdi-image</v-icon>
              {{ showAll ? 'Скрыть' : 'Показать все' }}
            </v-btn>
          </v-col>
        </v-row>
        <v-row v-if="images.length > 0">
          <v-col cols="12">
            <p>Отправьте загруженные изображения для аугментации</p>
          </v-col>
          <v-btn v-if="!uploadSuccess" color="primary" @click="uploadImages">
            <v-icon left>mdi-upload</v-icon>
            Отправить изображения
          </v-btn>
          <v-row v-if="uploadSuccess">
            <v-col cols="12">
              <v-alert type="success" dense text> Изображения успешно загружены </v-alert>
            </v-col>
          </v-row>
        </v-row>
        <v-row v-if="images.length > 0 && uploadSuccess">
          <v-col cols="12">
            <p>Настройте параметры аугментации</p>
          </v-col>
          <v-col cols="12">
            <v-row>
              <v-col cols="8">
                <v-slider label="Процент аугментации" v-model.number="augmentationPercentage" min="5" max="50"
                  step="1"></v-slider>
              </v-col>
              <v-col cols="4">
                <v-text-field v-model.number="augmentationPercentage" readonly></v-text-field>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="8">
                <v-slider label="Угол поворота" v-model.number="rotationAngle" min="0" max="45" step="1"></v-slider>
              </v-col>
              <v-col cols="4">
                <v-text-field v-model.number="rotationAngle" readonly></v-text-field>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="8">
                <v-slider label="Шум" v-model.number="noise" min="0" max="50" step="1"></v-slider>
              </v-col>
              <v-col cols="4">
                <v-text-field v-model.number="noise" readonly></v-text-field>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="8">
                <v-slider label="Контраст" v-model.number="contrast" min="0.5" max="1.5" step="0.1"></v-slider>
              </v-col>
              <v-col cols="4">
                <v-text-field v-model.number="contrast" readonly></v-text-field>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="8">
                <v-slider label="Яркость" v-model.number="brightness" min="-255" max="255" step="1"></v-slider>
              </v-col>
              <v-col cols="4">
                <v-text-field v-model.number="brightness" readonly></v-text-field>
              </v-col>
            </v-row>
          </v-col>

          <v-btn color="primary" @click="startAugmentation">
            <v-icon left>mdi-play</v-icon>
            Начать аугментацию
          </v-btn>
        </v-row>
        <!-- Индикатор загрузки -->
        <v-dialog v-model="loading" persistent max-width="300">
          <v-card color="primary" flat>
            <v-card-text class="text-center">
              <div>Ожидайте...</div>
              <v-progress-circular
                :size="60"
                :width="7"
                indeterminate
                color="white" 
              ></v-progress-circular>
            </v-card-text>
          </v-card>
        </v-dialog>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import JSZip from 'jszip'

export default {
  data() {
    return {
      files: [],
      images: [],
      showAll: false,
      uploadSuccess: false,
      augmentationPercentage: 5,
      rotationAngle: 0,
      noise: 0,
      contrast: 1,
      brightness: 0,
      loading: false
    }
  },
  async created() {
    console.log(this.$route.params.login)
  },
  computed: {
    displayedImages() {
      if (this.showAll) {
        return this.images.slice(0, 20)
      } else {
        return this.images.slice(0, 3)
      }
    }
  },
  methods: {
    toggleImages() {
      this.showAll = !this.showAll
    },
    handleFileInputChange(event) {
      this.files = event.target.files
      this.images = []
      for (let i = 0; i < 20; i++) {
        const file = this.files[i]
        const reader = new FileReader()
        reader.onload = (e) => {
          if (file.type === 'image/jpeg' || file.type === 'image/png') {
            this.images.push({ url: e.target.result })
          } else if (
            file.type === 'application/zip' ||
            file.type === 'application/x-zip-compressed'
          ) {
            this.extractImagesFromZip(file)
          }
        }
        reader.readAsDataURL(file)
      }
    },
    async extractImagesFromZip(file) {
      const zip = new JSZip()
      await zip.loadAsync(file)
      const files = Object.values(zip.files)
      for (const zipFile of files) {
        if (zipFile.dir === false && zipFile.name.match(/\.(jpg|jpeg|png)$/i)) {
          const imageData = await zipFile.async('blob')
          const reader = new FileReader()
          reader.onload = (e) => {
            this.images.push({ url: e.target.result })
          }
          reader.readAsDataURL(imageData)
        }
      }
    },
    async uploadImages() {
      try {
        this.loading = true;
        const zip = new JSZip()

        for (let i = 0; i < this.files.length; i++) {
          const file = this.files[i]
          if (file.type === 'image/jpeg' || file.type === 'image/png') {
            // Если это изображение, добавляем его в zip-архив
            const fileData = await this.getFileData(file)
            zip.file(file.name, fileData, { binary: true })
          } else if (
            file.type === 'application/zip' ||
            file.type === 'application/x-zip-compressed'
          ) {
            // Если это zip-архив, добавляем его содержимое в zip-архив
            await this.addImagesFromZip(file, zip)
          }
        }

        // Генерируем zip-архив
        const zipBlob = await zip.generateAsync({ type: 'blob' })

        // Отправляем zip-архив на сервер
        const formData = new FormData()
        formData.append('zip_file', zipBlob, 'images.zip')

        const response = await this.$axios.post('/upload_images/', formData, {
          headers: {
            'Content-Type': 'application/zip'
          }
        })

        // Обработка успешной загрузки
        console.log('Изображения успешно загружены:', response.data)
        this.uploadSuccess = true
        this.loading = false;
      } catch (error) {
        console.error('Ошибка загрузки изображений:', error)
        this.loading = false;
      }
    },

    async startAugmentation() {
      try {
        this.loading = true;
        const params = {
          rotation_angle: this.rotationAngle,
          noise_sigma: this.noise,
          contrast_alpha: this.contrast,
          brightness_beta: this.brightness,
          aug_percentage: this.augmentationPercentage
        }

        const response = await this.$axios.post('/augment_images/', null, {
          params,
          responseType: 'blob'
        })

        // Создаем ссылку на скачивание файла
        const url = window.URL.createObjectURL(new Blob([response.data]))

        // Создаем ссылку на элемент <a>, чтобы начать скачивание
        const link = document.createElement('a')
        link.href = url
        link.setAttribute('download', 'augmented_images.zip') // Устанавливаем имя файла для скачивания
        document.body.appendChild(link)
        link.click()

        // Освобождаем ресурсы
        window.URL.revokeObjectURL(url)
        this.loading = false;
      } catch (error) {
        // Обрабатываем ошибку
        console.error('Произошла ошибка:', error)
        this.loading = false;
      }
    },

    getFileData(file) {
      return new Promise((resolve, reject) => {
        const reader = new FileReader()
        reader.onload = () => resolve(reader.result)
        reader.onerror = reject
        reader.readAsArrayBuffer(file)
      })
    },
    async addImagesFromZip(zipFile, zip) {
      const zipData = await JSZip.loadAsync(zipFile)
      await Promise.all(
        Object.keys(zipData.files).map(async (fileName) => {
          const file = zipData.files[fileName]
          if (
            file.dir === false &&
            (file.name.endsWith('.jpg') ||
              file.name.endsWith('.jpeg') ||
              file.name.endsWith('.png'))
          ) {
            const imageData = await file.async('blob')
            zip.file(file.name, imageData, { binary: true })
          }
        })
      )
    }
  }
}
</script>

<style scoped>
.v-dialog {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* добавьте тень */
  border-radius: 8px; /* закругленные углы */
}

.v-dialog {
  animation: pulse 1s infinite alternate; /* добавьте анимацию */
}
.v-card-text {
  overflow-y: hidden !important;
}


@keyframes pulse {
  from {
    transform: scale(1);
  }
  to {
    transform: scale(1.1);
  }
}
</style>
