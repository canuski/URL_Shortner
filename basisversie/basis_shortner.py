import sqlite3
import hashlib
from flask import Flask, redirect, render_template, request, abort


app = Flask(__name__)


def create_table():
    con = sqlite3.connect('url.db')
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            base_url TEXT NOT NULL,
            short_url TEXT NOT NULL    
        )
    ''')
    con.commit()
    con.close()


create_table()


def maak_short_url(base_url):
    sha256_hash = hashlib.sha256(base_url.encode()).hexdigest()
    short_url = sha256_hash[:8]
    return short_url


@app.route('/', methods=['GET', 'POST'])
def load_main():
    if request.method == 'POST':
        base_url = request.form.get('input_url')
        if base_url:
            con = sqlite3.connect('url.db')
            cur = con.cursor()

            cur.execute('SELECT * FROM urls WHERE base_url=?', (base_url,))
            existing_url = cur.fetchone()

            if not existing_url:
                short_url = maak_short_url(base_url)
                cur.execute(
                    'INSERT INTO urls (base_url, short_url) VALUES (?, ?)', (base_url, short_url))
                con.commit()
            else:
                short_url = existing_url[2]

            con.close()
            # ga naar /redirect.html
            return redirect('/redirect')
        else:
            return render_template('main.html', error='Please enter a valid URL.')
    else:
        return render_template('main.html')


@app.route('/<short_url>')
def redirect_to_original(short_url):
    con = sqlite3.connect('url.db')
    cur = con.cursor()

    # haal de originele url waar de short url werd gemaakt
    cur.execute('SELECT base_url FROM urls WHERE short_url=?', (short_url,))
    res = cur.fetchone()

    con.close()

    if res:
        # ga terug naar de originele page
        return redirect(res[0])
    else:
        return abort(404)


@app.route('/redirect')
def redirect_page():
    con = sqlite3.connect('url.db')
    cur = con.cursor()

    # haaal alle shortned urls
    cur.execute('SELECT short_url FROM urls')
    urls = cur.fetchall()

    con.close()

    return render_template('redirect.html', urls=urls)


app.run(debug=True, port=5000)
