from flask import Flask, render_template
app = Flask(__name__,static_folder='assets')

# Código feito por Joaquim e Pedro

# Rota raiz, HOME PAGE
@app.route("/")
def home_page():
    return render_template('home_page.html')

app.run()