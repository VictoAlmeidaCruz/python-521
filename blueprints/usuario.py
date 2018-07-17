from flask import Blueprint,jsonify,request
from config.mongo import db
import json

#app = Flask()

usuario = Blueprint('usuarios',__name__)

@usuario.route('/usuarios',methods = ['GET','POST'])
def usuarios():
    if request.method == 'GET':
        return jsonify([json.loads(bdumps(u)) for u in db.usuarios.find()]) 
    else:
        usuario = request.get_json()
        keys = usuario.keys() 
        for k in ('nome', 'email'):
            if k not  in keys or not usuario[k].strip():  
                return make_reponse(jsonify({'message' :'Propriedade {0} obrigatoria'.format{k}),400) 
        db.usaurio.insert(usuario)
    return jsonify({"messagem" : "Usuario cadastrado com sucesso"})
