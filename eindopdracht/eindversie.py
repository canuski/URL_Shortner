import sqlite3
import hashlib
from flask import Flask, redirect, render_template, request, abort, url_for
from collections import OrderedDict
import logging

app = Flask(__name__)

app.config['STATIC_FOLDER'] = 'static'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # haalt favicon error weg

# config de logging naar file app.log
logging.basicConfig(filename='app.log', level=logging.INFO)

# Cache met OrderedDict
url_cache = OrderedDict()


def cache_decorator(max_size):
    def decorator(func):
        def wrapper(*args, **kwargs):
            key = args[0]  # gebruik het eerste arg als cache key
            if key in url_cache:
                # als de key al in de cache zitverplaats het naar het einde
                url_cache.move_to_end(key)
                return url_cache[key]
            else:
                # voer de originele functie uit
                result = func(*args, **kwargs)
                # voeg het result toe aan de cache
                url_cache[key] = result
                # controleer of de cache de max grootte heeft bereikt en verwijder het oudste item indien nodig
                if len(url_cache) > max_size:
                    url_cache.popitem(last=False)
                return result
        return wrapper
    return decorator


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
    # Log ingaven
    logging.warning(f"Input: {request.method}, {request.form}")

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
            result = redirect('/redirect')
        else:
            result = render_template(
                'main.html', error='Please enter a valid URL.')
    else:
        result = render_template('main.html')

    # Log uitput
    logging.warning(f"Output: {result}")

    return result


@cache_decorator(max_size=500)
@app.route('/<short_url>')
def redirect_to_original(short_url):
    con = sqlite3.connect('url.db')
    cur = con.cursor()

    cur.execute('SELECT base_url FROM urls WHERE short_url=?', (short_url,))
    res = cur.fetchone()

    con.close()

    if res:
        logging.warning(f"Cache hit! Redirecting to {res[0]}")
        return redirect(res[0])
    else:
        logging.warning("Cache miss! Performing database query.")
        return abort(404)


@app.route('/redirect')
def redirect_page():
    con = sqlite3.connect('url.db')
    cur = con.cursor()

    cur.execute('SELECT short_url FROM urls')
    urls = cur.fetchall()

    con.close()

    return render_template('redirect.html', urls=urls)


app.run(debug=True, port=5000)
