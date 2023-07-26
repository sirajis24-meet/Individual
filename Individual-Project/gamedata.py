config = {

  "apiKey": "AIzaSyDBkLecQZCF7_Qo0wCfxcdNIjqTwl3tvn0",
  "authDomain": "individual-project-e3baf.firebaseapp.com",
  "databaseURL": "https://individual-project-e3baf-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "individual-project-e3baf",
  "storageBucket": "individual-project-e3baf.appspot.com",
  "messagingSenderId": "456164884614",
  "appId": "1:456164884614:web:a11924727200904ea01107"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


db.child("Games").child("UGID").