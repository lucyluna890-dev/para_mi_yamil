from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/carta')
def carta():
    return render_template('carta.html')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

@app.route('/juego')
def juego():
    return render_template('juego.html')

@app.route('/sorpresa')
def sorpresa():
    return render_template('sorpresa.html')

@app.route('/gatitos')
def gatitos():
    return render_template('gatitos.html')

@app.route('/musica')
def musica():
    return render_template('musica.html')

if __name__ == '__main__':
    print("💖 Servidor del amor de luna iniciado en http://127.0.0.1:5000/ 💖")
    app.run(debug=True)
