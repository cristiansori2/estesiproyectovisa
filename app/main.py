from turtle import home
import flask
import requests
import requests, ssl
import time
import smtplib
app = flask.Flask(__name__)
app.config["DEBUG"] = False
starttime = time.time()

@app.route('/', methods=['GET'])
def home():
    while True:
     url = 'https://infovisa.ibz.be/ResultFr.aspx?place=HAV&visumnr=17125'
     response = requests.get(url)
     if response.text.__contains__("ACCORD"):
        port = 465  # For SSL
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("cristiansori2@gmail.com", "cryipomrjfssklkf")
            server.sendmail("cristiansori2@gmail.com",
                   "shaniafiallo@gmail.com",
                   "SIIIIIIII",
                   "Nos fuimos pa belgica pingaaaaaaaa")
        return "NOS FUIMOS PA BELGICA PINGAAAAAA"
     elif response.text.__contains__("REJET"):
        port = 465  # For SSL
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("cristiansori2@gmail.com", "cryipomrjfssklkf")
            server.sendmail("cristiansori2@gmail.com",
                   "shaniafiallo@gmail.com",
                   "APELAR",
                   "De pinga hay que Apelar")
        return "De pinga hay que APELAR"
     elif response.text.__contains__("En traitement"):
        time.sleep(60.0 - ((time.time() - starttime) % 60.0)) 
    return "ERROR"