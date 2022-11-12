from flask import url_for, redirect, render_template, request


def search_controller():
    region = request.form.get("region")
    name = request.form.get("player_name")
    game = request.form.get("game")

    if request.method == "POST":
        return redirect(url_for("handle.home", game=game, region=region, name=name))

    else:
        return render_template(f"fseason.html")
