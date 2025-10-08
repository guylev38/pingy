import { createApp } from 'vue'
import { Quasar } from 'quasar'
import { Notify, Dialog } from 'quasar'

// Import icon libraries
import '@quasar/extras/material-icons/material-icons.css'

// Import Quasar css
import 'quasar/src/css/index.sass'

import App from './App.vue'

const myApp = createApp(App)

myApp.use(Quasar, {
  plugins: { Notify, Dialog }, 
})

myApp.mount('#app')
