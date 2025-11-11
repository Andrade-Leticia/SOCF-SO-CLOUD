import os
import platform
import psutil

from flask import Flask, json, jsonify

app = Flask(__name__)
NOME_EQUIPE = "Alana da Conceição de Queiroz e Leticia Maria Maia de Andrade Vieira"

@app.get('/')
def get_root():
    return '<h1> Bem Vindo <h1>'

@app.get('/info')
def info():
    return jsonify({"Nome": NOME_EQUIPE})

@app.get('/metricas')
def metricas():
    pid = os.getpid()
    memoria_mb = psutil.virtual_memory().used / (1024 ** 2)
    cpu_percent = psutil.cpu_percent(interval=0.5)
    sistema = platform.platform()

    dados = {
        "Sistema Operacional": sistema,
        "PID": pid,
        "Uso CPU": f"{cpu_percent:.1f}%",
        "Memoria MB": f"{memoria_mb:.1f} MB"
    }

    return jsonify(json.dumps(dados, ensure_ascii = False))

APP = app

if __name__ == '__main__':
    app.run(debug=True)