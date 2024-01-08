
from flask import Flask,request
from threading import Thread
from test import sender
app=Flask("")
@app.route("/")
def home():
    return "hello"
@app.post("/post_deal")
def post_deal():
    deal=request.get_json()
    print(deal)
    sender(deal)
    return {"hello":"world"}
def run():
    app.run(host="0.0.0.0",port=8080)
def keep_alive():
    t=  Thread(target=run)
    t.start()

keep_alive()