import flask
import requests
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
        return "DE PINGA TODAVIA NADA"

    return "ERROR"