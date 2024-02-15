// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";

import {getDatabase,ref} from "firebase/database";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyA1t_qz1ooLW77S0sKxsEYGBoAg5ukXE30",
  authDomain: "onlytest-79bdd.firebaseapp.com",
  databaseURL: "https://onlytest-79bdd-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "onlytest-79bdd",
  storageBucket: "onlytest-79bdd.appspot.com",
  messagingSenderId: "214070070086",
  appId: "1:214070070086:web:690225d4ed9ea0f20d3347",
  measurementId: "G-DREB96MDDJ"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);


const database = getDatabase(app);
const testRef = ref(database,"test");
const countRef = ref(database,"count")

export {testRef,countRef}

