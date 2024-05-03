// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import {getDatabase} from "firebase/database";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBGKFlZcgiuKJMCAmSU1F2L8-mpRtWyGCk",
  authDomain: "bbpag-e60d8.firebaseapp.com",
  projectId: "bbpag-e60d8",
  storageBucket: "bbpag-e60d8.appspot.com",
  messagingSenderId: "685339319716",
  appId: "1:685339319716:web:5e0c10926798b5f5e47531",
  measurementId: "G-XVKYW0BGTL",
  databaseURL:"https://bbpag-e60d8-default-rtdb.asia-southeast1.firebasedatabase.app/"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
let database = getDatabase(app);

export default database;