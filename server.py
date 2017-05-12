from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'ThisIsSecret'

def sumCount():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1

@app.route('/')
def index():
    sumCount()
    return render_template('index.html')

@app.route('/plus', methods=['POST'])
def incrementByTwo():
    if request.form['action'] == 'plusTwo':
        session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    if request.form['action'] == 'reset':
        session['counter'] = 0
    return redirect('/')

app.run(debug = True)
