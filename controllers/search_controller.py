from flask import url_for, redirect, render_template, request


def search_controller(game):
    if request.method == "POST":
        region = request.form.get("region")
        name = request.form.get("player_name")

        return redirect(url_for("handle.home", game=game, region=region, name=name))
    
    elif game == 'lol' or game == 'tft':
        return render_template(f"{request.path.removeprefix('/')}.html")

    else:
        return render_template(f"lol.html")
