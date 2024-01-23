from flask import Flask, request, render_template
import os
import requests

app = Flask(__name__)

#Variable pour API acceslibre
key=""
API_acceslibre=""

#Variable pour API commerce
nb_res=20
API_Commerce="https://data.paysdelaloire.fr/api/explore/v2.1/catalog/datasets/commerces-export-openstreetmap-france/records?limit="+str(nb_res)+"&"

#Documentation
SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Commerce Sans Handi"
    }
)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/commerces", methods=['GET'])
def all_commerces():
    all=requests.get(API_Commerce)
    return all.json()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)