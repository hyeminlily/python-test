from flask import Flask, render_template, request
import ex04

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        list = []

        Slength = request.form['Slength']
        Swidth = request.form['Swidth']
        Plength = request.form['Plength']
        Pwidth = request.form['Pwidth']

        list.append(float(Slength))
        list.append(float(Swidth))
        list.append(float(Plength))
        list.append(float(Pwidth))

        name, ac_score = ex04.returnName(list)
        return render_template('predict.html', name=name, ac_score=ac_score)
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True, host='203.236.209.98')

