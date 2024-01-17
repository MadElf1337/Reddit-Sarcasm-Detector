from config import app
from flask import render_template, request
from inference_code import Datapred


@app.route("/")
def hello():
    return render_template('home.html')


@app.route('/trial')
def test():
    return render_template(('index.html'))


@app.route("/analyze", methods=['POST'])
def analyze():
    if request.method == 'POST':
        sentence = request.form.get('text')

        score = Datapred(sentence)
        return render_template('analyze.html', score=score)
    return "Not built yet"


if __name__ == "__main__":
    app.run(debug=True)
