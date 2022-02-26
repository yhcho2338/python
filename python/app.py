#from flask import Flask
#from urllib import request
#from bs4 import BeautifulSoup
#
#app = Flask(__name__)
#@app.route("/")
#def hello():
#    target = request.urlopen("https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=131")
#    soup = BeautifulSoup(target, "html.parser")
#    output=""
#    
#    for location in soup.select("location"):
#        output += "<h2> {} </h2>".format(location.select_one("city").string)
#        output += "날씨: {}, ".format(location.select_one("wf").string)
#        output += "최저/최고 기온: {} / {}".format(location.select_one("tmn").string, location.select_one("tmx").string)
#        output += "<hr/>"
#    return output
#
#====================================================================


#from flask import Flask
#
#FlaskApp = Flask(__name__)
#
#@FlaskApp.route("/") # url의 경로? 127.0.0.1:5000 로컬호스트
#def HekkoFlask():
#    return "Hello Flask!"
#
#@FlaskApp.route("/login/<ID>")
#def login_id(ID):
#    return "Login ID: %s" % ID

#@FlaskApp.route("/pass/<int:PASS>")
#def pass_num(PASS):
#    return "password: %s" % PASS  # %s 스트링으로 형변환
 
# 아랫 구문이 파이썬의 시작구문 
#if __name__ == "__main__":
#    FlaskApp.debug = True 
#    FlaskApp.run()    
#
#=================================================================
#
#from HelloFlask import FlaskApp
#from flask import Flask, render_template
#
#FlaskApp = Flask(__name__)
#
#@FlaskApp.route("/main.do")
#def naver():
#    return render_template("naver.html")
#
#
#if __name__ == "__main__":
#    FlaskApp.run()
#
#
# 
#===============================================================
#
#from flask import Flask, url_for
#
#FlaskApp = Flask(__name__)
#
#@FlaskApp.route("/") # url의 경로? 127.0.0.1:5000 로컬호스트
#def HelloFlask():
#    return "<h1> Hello Flask! </h1>"
#
#@FlaskApp.route("/login/<ID>")
#def login_id(ID):
#    return "Login ID: <h3> %s </h3>" % ID
#
#@FlaskApp.route("/pass/<int:PASS>")
#def pass_num(PASS):
#    return "password: <h6> %s </h6> " % PASS  # %s 스트링으로 형변환
# 
# 아랫 구문이 파이썬의 시작구문 
#if __name__ == "__main__":
#    FlaskApp.debug = True 
#    #FlaskApp.run()    
#    with FlaskApp.test_request_context():
#        print(url_for("login_id", ID="dragon"))
#        print(url_for("pass_num", PASS=1111))
#
#
#===============================================================

from flask import Flask, url_for
from flask.templating import render_template

FlaskApp = Flask(__name__)

@FlaskApp.route("/") # url의 경로? 127.0.0.1:5000 로컬호스트
def Hello():
    return "<h1> Klasse </h1>"

@FlaskApp.route("/userinfo1/<username>")
def user(username):
    return render_template("Userinfo1.html", name=username)

@FlaskApp.route("/userinfo2/<username>/<location>/<age_num>")
def user2(username, location, age_num):
    return render_template("Userinfo2.html", name=username, country=location, age=age_num)
 
# 아랫 구문이 파이썬의 시작구문 
if __name__ == "__main__":
    #FlaskApp.debug = True 
    FlaskApp.run()    
    