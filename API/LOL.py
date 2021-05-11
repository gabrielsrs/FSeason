from time import strftime
import requests


class Lol:

    def __init__(self, name, region):
        self.name = name
        self.region = region

    link_region = {
        "br1": "br1.api.riotgames.com",
        "eun1": "eun1.api.riotgames.com",
        "euw1": "euw1.api.riotgames.com",
        "jp1": "jp1.api.riotgames.com",
        "kr": "kr.api.riotgames.com",
        "la1": "la1.api.riotgames.com",
        "la2": "la2.api.riotgames.com",
        "na1": "na1.api.riotgames.com",
        "oc1": "oc1.api.riotgames.com",
        "ru": "ru.api.riotgames.com",
        "tr1": "tr1.api.riotgames.com",
    }

    def actual_elo(self):
        key = "RGAPI-f71fcd46-bd7b-4626-b6a5-173dc9156446"
        # try:
        url = requests.get(f"https://{self.region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.name}?api_key={key}")

        profile_icon_id = url.json()["profileIconId"]
        img_icon = f"http://ddragon.leagueoflegends.com/cdn/11.9.1/img/profileicon/{profile_icon_id}.png"

        url_elo = requests.get(f"https://{self.region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{url.json()['id']}?api_key={key}")

        items = {
            "profile_icon": img_icon,
            "solo_duo_rank": "default",
            "solo_duo_tier": "default",
            "flex_rank": "default",
            "flex_tier": "default",
        }

        # just the position in for statement
        for position, dict in enumerate(url_elo.json()):
            if url_elo.json()[position]["queueType"] in "RANKED_SOLO_5x5":
                items["solo_duo_rank"] = url_elo.json()[position]["rank"]
                items["solo_duo_tier"] = url_elo.json()[position]["tier"]

            elif url_elo.json()[position]["queueType"] in "RANKED_FLEX_SR":
                items["flex_rank"] = url_elo.json()[position]["rank"]
                items["flex_tier"] = url_elo.json()[position]["tier"]

        return items
        # except KeyError:
        #
        #
        # except IndexError:
        #


# test = Lol("gfdsgdgdfgdffd", "br1")
# test.actual_elo()
