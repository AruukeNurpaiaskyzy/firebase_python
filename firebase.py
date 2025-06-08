import pyrebase
config = {
  "apiKey": "AIzaSyC0gRvOJqMBMPLGpNx-H2AT_3zcvNnyoWI",
  "authDomain": "connectionfireba.firebaseapp.com",
  "projectId": "connectionfireba",
  "databaseURL": "https://connectionfireba-default-rtdb.firebaseio.com/",
  "storageBucket": "connectionfireba.firebasestorage.app",
  "messagingSenderId": "319406906810",
  "appId": "1:319406906810:web:6f683a8f8f0b455c065183",
  "measurementId": "G-FM8L17DDKL"
}
firebase = pyrebase.initialize_app(config)
database = firebase.database()

date = {'Age': 21, }