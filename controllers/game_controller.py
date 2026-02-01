from flask import url_for, redirect, render_template, session, flash
from  services import Lol, Tft


def game_controller(game, region, name):
    result = None

    if game == "lol":
        info_player = Lol(region=region, name=name)
        result = info_player.actual_elo()

    elif game == "tft":
        info_player = Tft(region=region, name=name)
        result = info_player.actual_elo()

    if result is False:
        flash("Usuário não encontrado")
        return redirect(url_for(f"handle.fseason"))
    else:
        for key, value in result.items():
            session[key] = value

        return render_template(f"{game}Home.html")
