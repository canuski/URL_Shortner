from flask import Flask, request, url_for
import sqlite3

app = Flask(__name__)


def init_database():  # kleine functie om de database op te starten
    con = sqlite3.connect('formdata.db')
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Namen(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                voornaam TEXT NOT NULL,
                familienaam TEXT NOT NULL
        )
    ''')
    con.commit()
    con.close()


init_database()  # run de functie telkens als de app wordt gestart


@app.route('/')  # html en route voor home pagina
def home():  # als we op submit drukken submit de form en geef die mee dat een post moet gebeuren naar /greet
    return """ 
    <h1>Welkom bij de Greeter App</h1>
    <form method="post" action="/greet"> 
        <label for="voornaam">Voornaam:</label>
        <input type="text" name="voornaam">
        <br>
        <label for="familienaam">Familienaam:</label>
        <input type="text" name="familienaam">
        <br>
        <input type="submit" value="indienen">
    </form>
    """


@app.route('/greet', methods=['POST'])
def greet():

    voornaam = request.form.get('voornaam')
    familienaam = request.form.get('familienaam')

    # lsaag de namen op in de database
    slaag_op_database(voornaam, familienaam)

    begroeting = f'Hallo, {voornaam} {familienaam}'

    return f"""
    <h1>Begroeting:</h1>
    <p>{begroeting}</p>
    <p><a href="{url_for('home')}">Terug naar het home page</a></p>
    """


def slaag_op_database(voornaam, familienaam):
    con = sqlite3.connect('formdata.db')
    cur = con.cursor()
    cur.execute('INSERT INTO Namen (voornaam, familienaam) VALUES(?,?)',
                (voornaam, familienaam))  # sql query voor namen in database te steken xd
    con.commit()
    con.close()  # einde


app.run(debug=True, port=5000)
