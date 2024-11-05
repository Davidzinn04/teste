from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Dados simulados para o conteúdo da página
    aviso = {
        "autor": "Jefferson Thawan da Silva",
        "data": "15/09/2022",
        "titulo": "RESULTADO FINAL DOS AUXÍLIOS",
        "conteudo": "A COAES divulgou o resultado dos auxílios estudantes. Segue anexos.",
        "anexos": 2,
        "comentarios": 2
    }
    return render_template('index.html', aviso=aviso)

if __name__ == '__main__':
    app.run(debug=True)