// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getDatabase } from "firebase/database";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAHmLswg1gsgVUgLOJN3ojTS5A9Q59-fUM",
  authDomain: "bbpeg-9da33.firebaseapp.com",
  databaseURL: "https://bbpeg-9da33-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "bbpeg-9da33",
  storageBucket: "bbpeg-9da33.appspot.com",
  messagingSenderId: "630640057706",
  appId: "1:630640057706:web:625f522efa4b18797d1913",
  measurementId: "G-69TWE44M23",
  databaseURL:"https://bbpeg-9da33-default-rtdb.asia-southeast1.firebasedatabase.app/"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const database = getDatabase();

export default database