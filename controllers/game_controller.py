from flask import url_for, redirect, render_template, session, flash
from API import lol, tft


def game_controller(game, region, name):
    result = None

    if game == "lol":
        info_player = lol.Lol(region=region, name=name)
        result = info_player.actual_elo()

    elif game == "tft":
        info_player = tft.Tft(region=region, name=name)
        result = info_player.actual_elo()

    if result is False:
        flash("Usuário não encontrado")
        return redirect(url_for(f"handle.fseason"))
    else:
        for key, value in result.items():
            session[key] = value

        return render_template(f"{game}Home.html")
