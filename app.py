from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>Qui è Ennio che ti scrive, se stai leggendo vuol dire che funziona!</p>Grande Flask!</p>"

#Start with flask --app app run (dove app è il nome del file .py)