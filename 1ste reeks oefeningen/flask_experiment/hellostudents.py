from flask import Flask
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
    html_content = "<h1>Studentenlijst</h1><ul>"
    for first, last in students:
        html_content += f"<li>{first} {last}</li>"
    html_content += "</ul>"

    return html_content


app.run(port=5000)
