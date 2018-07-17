#!/usr/bin/python3
from flask import Flask, jsonify,request,make_response
from datetime import datetime
import json

from bson.json_util import dumps as bdumps
from config.mongo import db
from blueprints.usuario import usuario
 

app = Flask(__name__)
app.register_blueprint(usuario)

@app.route('/')
def home():
   return jsonify({'status' : 'Runnig...'}) 


#isso é para rodar no servidor local.
#Quando subir para o servidor de produção o nome é diferente.
#Isso é um exemplo clássico, não é díficil encontrar exemplos.
if __name__ == '__main__':
    app.run(debug = True)
