from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('_site/cadastro.html')

@app.route('/dieta')
def dieta():
    return render_template('_site/dieta.html')

@app.route('/doacao')
def doacao():
    return render_template('_site/doacao.html')

@app.route('/fala')
def fala():
    return render_template('_site/fala.html')

@app.route('/login')
def login():
    return render_template('_site/login.html')

if __name__ == '__main__':
    app.run(debug=True)