from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Dados simulados para o conteúdo da página
    aviso = {
        "autor": "David André Souza de lima",
        "data": "06/11/2024",
        "titulo": "RESULTADO FINAL DOS AUXÍLIOS",
        "conteudo": "A COAES divulgou o resultado dos auxílios estudantes. Segue anexos.",
        "anexos": 2,
        "comentarios": 2
    }
    return render_template('index.html', aviso=aviso)

@app.route('/chats')
def chats():
    itens = [
        {'titulo': 'Minha Turma', 'notificacoes': 2},
        {'titulo': 'Matemática - Seminário sobre...', 'notificacoes': 2},
        {'titulo': 'Grupo aleatório de estudos', 'notificacoes': 2},
        {'titulo': 'Davi', 'notificacoes': 2},
        {'titulo': 'Lucas', 'notificacoes': 2},
    ]
    return render_template('chats.html', itens=itens)



@app.route('/grupos')
def grupos():
    # Dados fictícios para os itens na lista
    items = [
        {'title': 'Seminário sobre Apostas', 'subject': '2024 - Matemática', 'due': 'Amanhã', 'group': 'Abrir chat'},
        {'title': 'Seminário sobre Socialismo', 'subject': '2024 - Filosofia Política', 'due': 'Amanhã', 'group': 'Entrar em grupo'},
        {'title': 'Trabalho de Física', 'subject': '2024 - Física', 'due': '20/11', 'group': 'Entrar em grupo'}
    ]
    return render_template('grupos.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)