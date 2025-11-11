from flask import Flask, jsonify
import psutil
import os
import platform

APP = Flask(__name__)

nome_equipe = "Leticia Maria Maia de Andrade Vieira"

@APP.get('/info')
def info():
    return f"Nome: {nome_equipe}"

@APP.get('/metricas')
def metricas():
    pid = os.getpid()
    memoria_mb = psutil.virtual_memory().used // 1024 ** 2
    cpu_percent = psutil.cpu_percent(interval=0.5)
    sistema_operacional = platform.platform()

    metricas = {
        'Sistema Operacional': sistema_operacional,
        'PID': pid,
        'Uso CPU': f"{cpu_percent:.1f}%",
        'Memoria MB': f"{memoria_mb} MB"
    }

    return jsonify(metricas)
if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))