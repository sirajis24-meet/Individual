from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

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

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here

@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
           error = "login failed"
    return render_template("signin.html", error = error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            UID = login_session['user']['localId']
            user = {'username' : username}
            db.child("Users").child(UID).set(user)
            return redirect(url_for('signin'))
        except:
            error = "auth failed"
    return render_template("signup.html", error = error)

@app.route('/home', methods = ['GET', 'POST'])
def home():
    game_data = db.child("Games").get().val()
    return render_template("home.html", game_data=game_data)

@app.route('/home/<string:name>')
def games(name):
    game_data = db.get().val()
    return render_template("comments.html", n = name, game_data=game_data)

@app.route('/add_games', methods = ['GET','POST'])
def add_game():
    error = ""
    if request.method == 'POST':
        img_url = request.form['img_url']
        game_title = request.form['game_title']
        #comments = request.form['comments']
        try: 
           
            game_data = {
                'img_url': img_url,
                'game_title': game_title,
                'comments': []
            }
          
            db.child("Games").push(game_data)

            return redirect(url_for('home'))
        except:
            error = "couldnt add game"
    game_data = db.child("Games").get().val()
    return render_template('add_games.html', error = error, game_data = game_data )







#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)