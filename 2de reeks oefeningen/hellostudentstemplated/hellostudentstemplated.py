from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def hello_students():
    # Verbinding maken
    con = sqlite3.connect('school.db')
    cur = con.cursor()

    # Query om namen op te halen
    query = 'SELECT FirstName, LastName FROM Students'
    cur.execute(query)
    students = cur.fetchall()

    # verbinding sluiten
    con.close()

    # html aanmaken
    return render_template('hello_students.html', students=students)


app.run(port=5000, debug=True)
