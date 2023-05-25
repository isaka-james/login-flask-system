from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
  return '''
  <!DOCTYPE html>
  <html>
  <head>
       <title> Home </title>
       <meta name="viewport" content="width=device-width,initial-scale=1"/>
  </head>
  <body>
    <h1 style="text-align: center;font-size: 30px; font-weight:500"> Homepage </h1>
    <div style="padding-left: 12px;padding-right:12px;background-color:whitesmoke;text-align: center; padding-top: 10px; border-radius: 10px;">
         <button style="padding: 12px 20px; border-radius: 8px; float: center; background-color: blue;color: white"> Login </button>
         <br/>
         <button style="padding: 12px 20px; border-radius: 8px; float: center; background-color: lightblue;color:white"> Login </button>
    </div>
  </body>
  </html>
  '''

