from flask import Flask, request, url_for

app = Flask(__name__)


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

    begroeting = f'Hallo, {voornaam} {familienaam}'

    return f"""
    <h1>Begroeting:</h1>
    <p>{begroeting}</p>
    <p><a href="{url_for('home')}">Terug naar het home page</a></p>
    """


app.run(debug=True, port=5000)
