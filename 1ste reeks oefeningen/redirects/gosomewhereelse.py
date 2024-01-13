from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def ga_ergens():
    return redirect('https://www.ap.be')


app.run(debug=True, port=5000)
