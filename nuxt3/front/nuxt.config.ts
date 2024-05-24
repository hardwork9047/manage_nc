// nuxt.config.js
export default {
  buildModules: [
    '@vuetify/nuxt'
  ],
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    treeShake: true
  },
  css: [
    'vuetify/lib/styles/main.sass',
    '@/assets/variables.scss',
  ],
  build: {
    transpile: ['vuetify'],
  },
  plugins: ['~/plugins/vuetify.js'],
  typescript: {
    strict: true
  },
}
