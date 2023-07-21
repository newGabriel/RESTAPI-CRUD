from flask import Flask, jsonify, request

app = Flask(__name__)

alunos = dict()

@app.route('/')
def index():
    return '<h1>TESTE</h1>'

@app.get('/aluno')
def aluno_get():
    if request.is_json:
        data = request.get_json()
        id = data.get('id')
        print(id)
        if type(id) is list:
            l = list()
            for i in id:
                if i in alunos:
                    l.append(alunos[i])
            return jsonify(l)
        elif id in alunos:
            return jsonify(alunos[id])
        else:
            return jsonify({'mensagem': 'Error'}), 404
    else:
        return jsonify(alunos)
    

@app.post('/aluno')
def aluno_post():
    if request.is_json:
        data = request.get_json()
        id = int(data.get('id'))
        nome = data.get('nome')
        nota = data.get('nota')

        alunos[id] = {'nome': nome, 'nota': nota}

        return jsonify(alunos[id]), 200
    else:
        return jsonify({'mensagem': 'Error'}), 400
