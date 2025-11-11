from flask import Flask, jsonify
import psutil
import os
import platform
import json

APP = Flask(__name__)

nome_equipe = "Leticia Maria Maia de Andrade Vieira"

@APP.get('/info')
def info():
    return "fNome: {nome_equipe}"

@APP.get('/metricas')
def metricas():
    #obtem versao s.o subjacente
    print(platform.platform())
    #obtem pid
    print( os.getpid())
    #uso cpu%
    print( psutil.cpu_percent())
    #uso memoria MB
    print( psutil.virtual_memory().used // 1024 ** 2)

    metricas = { #cria dicionario
        'Sistema Operacional': platform.platform(),
        'PID': os.getgid(),
        'Uso CPU': psutil.cpu_percent(),
        'Memoria MB': psutil.virtual_memory().used // 1024 ** 2
    }
    return jsonify(metricas)#transforma p/ json

if __name__ == "__main__":
    APP.run(host = "0.0.0.0", port = int(os.environ.get("PORT", 5000)))