from time import strftime
import requests
import Validator


def line():
    print("-" * 44)


def end_season():
    """
    Dias para o final da season.
    :print: Saída de de antes, no dia, e depois, em relação ao dia final da season.
    """
    day = strftime("%d")
    hours = strftime("%H")
    minutes = strftime("%M")
    last_day = 3
    if int(day) < last_day:
        end = last_day - int(day)
        print(f"Faltam {end} dias para o final da season.")

    elif int(day) == last_day:
        print(f"Faltam {24 - int(hours)}:{60 - int(minutes)}")

    elif int(day) > last_day:
        print(f"Já acabou a season.")


def actual_elo(name):
    """
    Elo e divisão do jogador.
    :param name: Nome do usuário no game.
    :print: Saída de elo e divisão da solo duo e flex respectivamente.
    """
    try:
        url = requests.get("https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=RGAPI-9f127b4e-ff42-4cd1-a0da-fca38e779fee")
        url_elo = requests.get("https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + url.json()["id"] + "?api_key=RGAPI-9f127b4e-ff42-4cd1-a0da-fca38e779fee")
        print('\033[32m-Solo duo {} {}.'.format(url_elo.json()[0]["tier"], url_elo.json()[0]["rank"]))
        print('-Flex {} {}.\033[m'.format(url_elo.json()[1]["tier"], url_elo.json()[1]["rank"]))
    except KeyError:
        print("\033[31mNome de usuário não aceito, tente novamente.\033[m")

    except IndexError:
        print("\033[32m-Unranked.\033[m")


line()
print(f"Dia {strftime('%d')}/{strftime('%m')}/{strftime('%Y')}{strftime('%H:%M'):>22}")
end_season()
while True:
    name_account = Validator.validator_of_name("Digite o nome da sua conta: ")
    print(f"Os elos na fila solo duo são: ")
    actual_elo(name_account)
    continue_names = Validator.validator_of_response("Quer conferir mais alguma conta? ")
    if continue_names in "n":
        break
    line()
