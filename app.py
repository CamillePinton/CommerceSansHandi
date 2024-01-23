from flask import Flask
import os
import requests

app = Flask(__name__)
#Variable pour API acceslibre
key=""
API_acceslibre=""

#Variable pour API commerce
nb_res=20
API_Commerce="https://data.paysdelaloire.fr/api/explore/v2.1/catalog/datasets/commerces-export-openstreetmap-france/records?limit="+str(nb_res)+"&"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/commerces", methods=['GET'])
def all_commerces():
    all=requests.get(API_Commerce)
    return all.json()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)