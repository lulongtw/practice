// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import {getDatabase} from "firebase/database";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDew1h9zPmt2TttnaMAlotRH9JmY5FNfa0",
  authDomain: "testingla-52bb1.firebaseapp.com",
  databaseURL: "https://testingla-52bb1-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "testingla-52bb1",
  storageBucket: "testingla-52bb1.appspot.com",
  messagingSenderId: "157924080759",
  appId: "1:157924080759:web:080cb690224d8346155a72",
  measurementId: "G-H632BP6H9X"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);


const database = getDatabase(app)
export default database