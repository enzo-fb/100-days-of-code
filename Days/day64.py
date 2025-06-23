"""Autenticação do usuário"""

from flask import Flask, request, redirect, url_for, render_template_string, session

app = Flask(__name__)
app.secret_key = "chave-secreta"

# Usuários salvos manualmente
usuarios = {"admin": "1234", "admin": "senha"}


# Página de login
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        if usuario in usuarios and usuarios[usuario] == senha:
            session["usuario"] = usuario
            return redirect("/home")
        return "Usuário ou senha inválidos!"

    return """
        <h2>Login</h2>
        <form method="post">
            Usuário: <input name="usuario"><br>
            Senha: <input type="password" name="senha"><br>
            <button type="submit">Entrar</button>
        </form>
    """


# Página protegida
@app.route("/home")
def home():
    if "usuario" in session:
        return f'Bem-vindo, {session["usuario"]}! <a href="/logout">Sair</a>'
    return redirect("/")


# Logout
@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
