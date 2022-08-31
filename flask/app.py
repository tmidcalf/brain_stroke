from cgi import test
from unittest import result
from flask import Flask, request, render_template, redirect, url_for
import model

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        age = request.form['age']
        height = request.form['height']
        weight = request.form['weight']
        sex = request.form['sex']
        married = request.form['married']
        work = request.form['work']
        res = request.form['res']
        smoke = request.form['smoke']
        hyper = request.form['hyper']
        heart = request.form['heart']
        agl = request.form['agl']
        results = model.mlearn(age, height, weight, sex, married, work, res, smoke, hyper, heart, agl)
        return render_template('index.html', test=results)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug = True)