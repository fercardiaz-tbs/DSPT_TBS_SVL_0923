#!/usr/bin/env python
# encoding: utf-8
import json

from flask import Flask, request, jsonify
from os import environ
app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({'message':"Hello perros! Welcome to Flask + Docker. Lets Rock and Roll"})

# Búsqueda de todos los usuarios. http://localhost:5000/user/all
@app.route('/user/all', methods=['GET'])
def all_records():
    
    with open('tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        
        return jsonify(records)
        return jsonify({'error': 'data not found'})


# Búsqueda por nombre. http://localhost:5000/user?name="alejandru"
@app.route('/user', methods=['GET'])
def query_records():
    name = request.args.get('name')

    with open('tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        f.close()
        for record in records:
            if record['name'] == name:
                return jsonify(record)
        return jsonify({'error': 'data not found'})

# Editar usuario
@app.route('/user', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    with open('tmp/data.txt', 'r') as f:
        data = f.read()
        f.close()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('tmp/data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
        f.close()
    return jsonify(record)

# Crear usuario
# POST http://localhost:5000/user
#
#{
#  "name": "muchelle",
#  "email": "muchelle@gmail.com"
#}

@app.route('/user', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    records = []
    with open('tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        f.close()

    records.append(record)

    with open('tmp/data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
        f.close()
    return jsonify(record)

# Borrar usuario
# POST http://localhost:5000/user
#
#{
#  "name": "miguel",
#  "email": "miguel@gmail.com"
#}
    
@app.route('/user', methods=['DELETE'])
def delte_record():
    record = json.loads(request.data)
    new_records = []
    with open('tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['name'] == record['name']:
                continue
            new_records.append(r)
    with open('tmp/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
        f.close()
    return jsonify(record)


if __name__ == '__main__':
  app.run(debug = True, host = '0.0.0.0', port=environ.get("PORT", 5000))