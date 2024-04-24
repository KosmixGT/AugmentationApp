<template>
  <v-container>
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
        <v-file-input
          label="Выберите изображения или zip архив"
          multiple
          accept="image/*,.zip"
          @change="handleFileInputChange"
        ></v-file-input>
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
      <v-btn color="primary" @click="uploadImages">Отправить изображения</v-btn>
    </v-row>
  </v-container>
</template>

<script>
import JSZip from 'jszip';

export default {
  data() {
    return {
      files: [],
      images: [],
      showAll: false
    }
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
      } catch (error) {
        console.error('Ошибка загрузки изображений:', error)
      }
    }
  }
}
</script>