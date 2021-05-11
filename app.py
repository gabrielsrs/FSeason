from flask import Flask, render_template, request, flash, url_for, redirect, session, json
from API.LOL import Lol


app = Flask(__name__)
app.secret_key = "sadsadadas"


@app.route("/fseason", methods=["POST", "GET"])
def fseason():
    if request.method == "POST":
        region = request.form.get("region")
        name = request.form.get("player_name")
        print(name)
        info_player = Lol(name, "br1")
        result = info_player.actual_elo()

        if result is False:
            flash("Usuárion não encontrado, tente novamente ou volte mais tarde")
            return render_template("fseason")
        else:
            session["nickname"] = name
            for key, value in result.items():
                session[key] = value

            return redirect(url_for("home"))


        # return flash(info_player.actual_elo()["tier"])
        # return redirect("home", info_player.actual_elo()["summonerNmae"])

        # return redirect(url_for("home", name=name))

    else:
        return render_template("fseason.html")


@app.route("/home")
def home():
    print(session)
    return render_template("home.html")


# @app.route("/region")
# def region():
#     return render_template("region.html")


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