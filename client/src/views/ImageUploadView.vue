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
            <p>
              Загружено изображений: {{ images.length }}
            </p>
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
            <v-img :src="image.url" contain></v-img>
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
            <p>
              Отправьте загруженные изображения для аугментации
            </p>
          </v-col>
          <v-btn color="primary" @click="uploadImages">
            <v-icon left>mdi-upload</v-icon>
            Отправить изображения
          </v-btn>
          <v-row v-if="uploadSuccess">
            <v-col cols="12">
              <v-alert type="success" dense text>
                Изображения успешно загружены
              </v-alert>
            </v-col>
          </v-row>
        </v-row>
        <v-row v-if="images.length > 0 && uploadSuccess">
          <v-col cols="12">
            <p>
              Настройте параметры аугментации
            </p>
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
      </v-card-text>
    </v-card>
  </v-container>
</template>


<script>
import JSZip from 'jszip';

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
      brightness: 0
    }
  },
  async created() {
    console.log(this.$route.params.login)
  },
  computed: {
    displayedImages() {
      if (this.showAll) {
        return this.images.slice(0, 20);
      } else {
        return this.images.slice(0, 3);
      }
    }
  },
  methods: {
    toggleImages() {
      this.showAll = !this.showAll;
    },
    handleFileInputChange(event) {
      this.files = event.target.files
      this.images = []
      for (let i = 0; i < this.files.length; i++) {
        const file = this.files[i]
        const reader = new FileReader()
        reader.onload = (e) => {
          if (file.type === 'image/jpeg' || file.type === 'image/png') {
            this.images.push({ url: e.target.result })
          } else if (file.type === 'application/zip' || file.type === 'application/x-zip-compressed') {
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
      const formData = new FormData()
      for (let i = 0; i < this.files.length; i++) {
        formData.append('files', this.files[i])
      }
      try {
        const response = await this.$axios.post('/upload_images/', formData)
        // Обработка успешной загрузки
        console.log('Изображения успешно загружены:', response.data)
        this.uploadSuccess = true
      } catch (error) {
        console.error('Ошибка загрузки изображений:', error)
      }
    }
  }
}
</script>