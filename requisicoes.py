#!/usr/bin/python3

import requests

headers = {'Content-Type':'application/json'}
#data ={"nome" : "João Batista" , "email" : "joao@bol.com.br"}

data ={"nome" : "Leonardo"}

response = requests.get('http://127.0.0.1:5000/usuarios')
data = response.json()


print('{0:.10}{1:.>30}'.format('ID','NOME'))
for x in data['usuarios']:
    if x['id']%2==0:
#        print('{0.>10}{1:.>30}'.format(x['id'],x['nome']))  
        print((x['id'],x['nome'])  

#response = requests.post('http://127.0.0.1:5000/usuarios',json=data)

#response = requests.put('http://127.0.0.1:5000/usuarios/7',json=data)

#response = requests.delete('http://127.0.0.1:5000/usuarios/7',json=data)



#response = requests.get('http://phpypesh.com.br')
#print(response.content)
#print(response.json())
