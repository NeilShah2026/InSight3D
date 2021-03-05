#Imports
from flask import Flask
from threading import Thread

# Making HTTP Server
app = Flask('')

# Checking For Activity
@app.route('/')
def home():
    return "Hello. I am alive!"

# Collecting Server Data
def run():
  app.run(host='0.0.0.0',port=8080)

# Starting HTTP Server
def keep_alive():
    t = Thread(target=run)
    t.start()