from flask import Flask
import sqlite3
import logging

app = Flask(__name__)

# basic logging config
logging.basicConfig(filename='flask_experiment.log',
                    encoding='utf-8', level=logging.DEBUG)


@app.route('/')
def hello_students():
    # log info bezoek aan app
    logging.info('De app is bezocht')

    # Verbinding maken
    con = sqlite3.connect('school.db')
    cur = con.cursor()

    # Query om namen op te halen
    query = 'SELECT FirstName, LastName FROM Students'
    cur.execute(query)
    students = cur.fetchall()

    # verbinding sluiten
    con.close()

    # log debug
    logging.debug(f'Res body: {students}')

    # html aanmaken
    html_content = "<h1>Studentenlijst</h1><ul>"
    for first, last in students:
        html_content += f"<li>{first} {last}</li>"
    html_content += "</ul>"

    return html_content


app.run(debug=True, port=5000)
