import "./assets/style.css";
import App from "./App.vue";
import router from "./router";
import {createApp} from "vue";
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap';

let app = createApp(App);
app.use(router);

app.mount("#app");