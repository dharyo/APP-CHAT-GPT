from flask import Flask, render_template, request
from resumen import Resumentexto
import os
from dotenv import load_dotenv



idiomas = [
    {"codigo": "es", "nombre": "Español"},
    {"codigo": "en", "nombre": "Inglés"},
    {"codigo": "fr", "nombre": "Frances"},
    {"codigo": "de", "nombre": "Alemán"},
    {"codigo": "it", "nombre": "Italiano"},
    {"codigo": "pt", "nombre": "Portugués"},
    {"codigo": "ru", "nombre": "Ruso"},
    {"codigo": "ja", "nombre": "Japonés"},
    {"codigo": "ko", "nombre": "Coreano"},
    {"codigo": "zh", "nombre": "Chino mandarin"}
]

app = Flask(__name__)

load_dotenv()
gpt_resumen = Resumentexto(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html', idiomas=idiomas)


@app.route('/resumir', methods =['POST'])
def resumir():
    idioma = request.form['idioma']
    texto = request.form['texto']
    resumen = gpt_resumen.resumen(idioma,texto)
    return render_template('index.html', resumen=resumen,idiomas=idiomas,idiomasleccionado=idioma)


if __name__ == '__main__':
    app.run()
