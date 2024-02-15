// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import{getDatabase,ref,get,set,onValue,push} from "firebase/database"
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDH5uSRQl60eETjWWGFCv8S9uDYDtTJYaA",
  authDomain: "vuefirebasechat-39fbf.firebaseapp.com",
  projectId: "vuefirebasechat-39fbf",
  storageBucket: "vuefirebasechat-39fbf.appspot.com",
  messagingSenderId: "592088930343",
  appId: "1:592088930343:web:c3cf2117f594300c2b5602",
  measurementId: "G-538EHVERE6",
  databaseURL:"https://vuefirebasechat-39fbf-default-rtdb.asia-southeast1.firebasedatabase.app"
};

// Initialize Firebase
const fbapp = initializeApp(firebaseConfig);
const dataBase = getDatabase(fbapp);
const chatRoomRef = ref(dataBase,"chatRoom")

export {chatRoomRef,get,set,onValue,push}