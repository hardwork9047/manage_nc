<!-- app.vue -->
<template>
  <v-app>
    <v-app-bar app color="emerald" dark>
      <v-toolbar-title class="white--text">Nurse Call Management System</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-img
        src="/img/logo.png"
        alt="Company Logo"
        contain
        class="logo-img"
      ></v-img>
    </v-app-bar>
    <v-main>
      <NuxtPage />
    </v-main>
  </v-app>
</template>

<script>

export default {
  setup() {
    // Vuetifyの設定はプラグインで行うため、ここには追加しません
  }
}
</script>

<style scoped>
.v-app-bar {
  background-color: #2ecc71; /* エメラルド色 */
}



.v-toolbar-title {
  color: white;
  word-break: break-word; /* 長い単語が折り返されるようにする */
}

.v-img {
  max-height: 40px; /* 画像の高さを適切に調整 */
  max-width: 120px;
}

.logo-img {
  margin-right: 16px; /* 右側のマージンを調整 */
}
</style>