from flask import Flask, render_template
from gerador_de_frases import A1A_sentence_generator

generator = A1A_sentence_generator()

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    tipo, frase_pt, frase_en = generator.gerar_frases()
    return render_template('index.html', frase_en=frase_en, frase_pt=frase_pt)


if __name__ == "__main__":
    app.run(debug=True)