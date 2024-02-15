import App from "./App.vue";
import {createApp} from "vue";
import router from "./router";
import "./assets/style.css";
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap';

let app = createApp(App);

app.use(router);
app.mount("#app")
