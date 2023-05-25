from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
  return '''<p style='color:red;font-size:45px;font-weight:500;'> masterplan </p>'''

