from flask import Flask, render_template, request
import check_func

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/check", methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        list = []
        age = request.form['age']
        workclass = request.form['workclass']
        education = request.form['education']
        occupation = request.form['occupation']
        sex = request.form['sex']
        race = request.form['race']
        hours_per_week = request.form['hours-per-week']
        list.append([int(age), workclass, education, occupation, sex, race, int(hours_per_week)])
        r = check_func.check(list)
        return render_template('check.html', r=r)
    return render_template('check.html')

if __name__ == '__main__':
    app.run(debug=True, host='203.236.209.98')

