

import { createApp } from 'vue'
import App from './App.vue'


const app = createApp(App)

//不需.use(store) 那是一頁式cdn在用的

app.mount('#app')
