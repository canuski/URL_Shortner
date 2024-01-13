from flask import Flask, abort, render_template
import sqlite3


app = Flask(__name__)


def get_lastname(voornaam):
    con = sqlite3.connect('school.db')
    cur = con.cursor()
    query = 'SELECT LastName FROM Students WHERE FirstName = ?'
    cur.execute(query, (voornaam,))
    res = cur.fetchone()
    con.close()
    return res


@app.route('/<voornaam>')
def ga_ergens(voornaam):
    achternaam_res = get_lastname(voornaam)
    if achternaam_res:
        # als de voornaam in db staat stuur door naar pagina
        achternaam = achternaam_res[0]
        return render_template('redirect.html', achternaam=achternaam)
    else:
        abort(404)


app.run(debug=True, port=5000)
