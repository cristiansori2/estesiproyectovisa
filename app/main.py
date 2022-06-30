import flask
import requests
import smtplib, ssl

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    url = 'https://infovisa.ibz.be/ResultFr.aspx?place=HAV&visumnr=17125'
    response = requests.get(url)
    if response.text.__contains__("ACCORD"):
        return "NOS FUIMOS PA BELGICA PINGAAAAAA"
    elif response.text.__contains__("REJET"):
        return "De pinga hay que APELAR"
    elif response.text.__contains__("En traitement"):
        port = 465  # For SSL
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("cristiansori2@gmail.com", "cryipomrjfssklkf")
            server.sendmail("cristiansori2@gmail.com",
                   "cristiansori2@gmail.com",
                   "NADA",
                   "TODAVIA NADA")
        return "DE PINGA TODAVIA NADA"
    return "ERROR"