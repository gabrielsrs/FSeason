from flask import Flask, render_template, request, flash, url_for, redirect, session, json
from API.LOL import Lol


app = Flask(__name__)
app.secret_key = "sadsadadas"


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
    print(region, name)
    if result is False:
        flash("Usuário não encontrado")
        return redirect(url_for("fseason"))
    else:
        for key, value in result.items():
            session[key] = value

        return render_template("home.html")


@app.route("/region")
def region():
    return render_template("region.html")


# @app.route("/select")
# def select():
#     return render_template("select.html")


if __name__ == "__main__":
    app.run(debug=True)


# @app.route("/fseason", methods=["POST", "GET"])
# def fseason():
#     if request.method == "POST":
#         name = request.form.get("playername")
#         print(name)
#         info_player = Lol(name)
#
#         flash(info_player.actual_elo())
#         return render_template("fseason.html")
#
#     else:
#         return render_template("fseason.html")