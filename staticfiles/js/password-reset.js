// static/js/firebase-config.js

// Import Firebase SDK
import firebase from "https://www.gstatic.com/firebasejs/9.10.0/firebase-app.js";
import "https://www.gstatic.com/firebasejs/9.10.0/firebase-auth.js";

// Firebase configuration (replace these with your Firebase project's config)
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_STORAGE_BUCKET",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID",
  measurementId: "YOUR_MEASUREMENT_ID"
};

// Initialize Firebase
const app = firebase.initializeApp(firebaseConfig);

// Export the Firebase Auth instance
export const auth = firebase.auth();
