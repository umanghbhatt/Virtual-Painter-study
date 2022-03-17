from flask import Flask,render_template,request,redirect,Response
from Virtual import main
from Virtual import FingerCounting
import cv2


app = Flask(__name__)
obj = main.GetVirtualScreen()
obj2 =  FingerCounting.FingerCounting()
# obj.drawObject()
@app.route("/home")
def main_func():
    return render_template("home.html")
@app.route("/")
def mainfunc():
    return render_template("info.html")
@app.route("/info")
def mainfunc1():
    return render_template("info.html")
    #return "<p>This page for products page </p>"



@app.route("/count")
def videoCount():
    print("Started")
    return Response(obj2.countFingers(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/video")
def video():
    print("Started")
    return Response(obj.drawObject(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/live")
def live():
    return render_template('video.html')

@app.route("/live-count")
def liveCount():
    return render_template('countFinger.html')
if __name__ == "__main__":
    app.run(debug = False ,port = 5000)
