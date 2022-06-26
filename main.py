import streamlit as st
import pyrebase
import datetime as datetime

firebaseConfig = {
  "apiKey": "AIzaSyANvY1WusKuNfpCW3WYagFSd9mPIBtUN_0",
  "authDomain": "stay-safe-c7497.firebaseapp.com",
  "databaseURL": "https://stay-safe-c7497-default-rtdb.firebaseio.com",
  "projectId": "stay-safe-c7497",
  "storageBucket": "stay-safe-c7497.appspot.com",
  "messagingSenderId": "510281232102",
  "appId": "1:510281232102:web:82d6246255cbca22f0d527",
  "measurementId": "G-1FQC62M1V7"
};

#Firebase authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
#Database
db = firebase.database()
storage = firebase.storage()

# Authentication
st.sidebar.title("Welcome to Stay Safe")