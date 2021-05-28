from flask import Flask, render_template, request, flash, url_for, redirect, session
from API.LOL import Lol


app = Flask(__name__)
app.secret_key = "SecretKey"


@app.route("/")
@app.route("/fseason", methods=["POST", "GET"])
def fseason():
    if request.method == "POST":
        region = request.form.get("region")
        name = request.form.get("player_name")

        return redirect(url_for("home", region=region, name=name))

    else:
        return render_template("fseason.html")


@app.route("/home/<region>/<name>")
def home(region, name):
    info_player = Lol(region=region, name=name)
    result = info_player.actual_elo()

    if result is False:
        flash("Usuário não encontrado")
        return redirect(url_for("fseason"))
    else:
        for key, value in result.items():
            session[key] = value

        return render_template("home.html")


if __name__ == "__main__":
    app.run()
