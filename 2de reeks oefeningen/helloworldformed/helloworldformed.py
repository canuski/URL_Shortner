from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('helloworld.html')


app.run(port=5000, debug=True)
