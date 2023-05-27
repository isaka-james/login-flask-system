from flask import Flask,session,url_for,render_template,redirect,request
import random
import string

app=Flask(__name__)

# getting the secret key for the sessions
letters = string.ascii_lowercase
app.secret_key = ''.join(random.choice(letters) for i in range(32)) # 32 random characters



@app.route('/')
def dash(): 
  if 'username' in session:
    return redirect(f'/dash/{session["username"]}')
  else:
    return render_template('login.html',title='Login to Your Account')


@app.route('/login')
def login():
  if 'username' in session:
    return redirect(f'/dash/{session["username"]}')
  else:
    return render_template('login.html',title='Login to Your Account')
    
@app.route('/dash/<name>')
def home(home):
  if not 'username' in session:
    return redirect('/login')
  title1 = 'Home Page'
  session_usr = session['username']
  return render_template('/dashboard.html',title=title1,name = session_usr)

@app.route('/action',methods=['GET','POST'])
def action():
  if 'username' in session:
    return redirect(f'/dash/{session["username"]}')

  # we deal with the post request
  if request.method == 'POST':
    try: # for security issue 
      username = request.form['username']
      password = request.form['password']
    except:
      return render_template('login.html',message='Invalid Request',title='Try login again!')
  else: # when the user send the get request
    return render_template('login.html',message='Invalid Request',title='Try login again!')

  # implement logarithm here to check the real password from the server(database)
  real_pwd = 'master123'
  real_username = 'masterplan@gmail.com'

  if (password == real_pwd) and (username == real_username):
    # hoorey -> already sign in

    # assigning the userful informations
    # next time fetch this from the database
    session['username'] = 'masterplan'

    return redirect(f'/dash/{session["username"]}')
  else:
    return render_template('login.html',message="Wrong password or Username",title='Login Failed Try agian!')

@app.route('/Logout')
def logout():
  if 'username' in session:
    session.pop('username')
  return redirect('/login')

if __name__=='__main__':
  app.run(debug=True)
