from services.time_calculator_service import TimeCalculator
import requests
from app import app

link_region = {
    "br": "https://br1.api.riotgames.com",
    "eun": "https://eun1.api.riotgames.com",
    "euw": "https://euw1.api.riotgames.com",
    "jp": "https://jp1.api.riotgames.com",
    "kr": "https://kr.api.riotgames.com",
    "lan": "https://la1.api.riotgames.com",
    "las": "https://la2.api.riotgames.com",
    "na": "https://na1.api.riotgames.com",
    "oc": "https://oc1.api.riotgames.com",
    "ru": "https://ru.api.riotgames.com",
    "tr": "https://tr1.api.riotgames.com",
}

images_elo = {
    "unranked": "../../static/images/LolEmblemImages/emblem-unranked.webp",
    "iron": "../../static/images/LolEmblemImages/emblem-iron.webp",
    "bronze": "../../static/images/LolEmblemImages/emblem-bronze.webp",
    "silver": "../../static/images/LolEmblemImages/emblem-silver.webp",
    "gold": "../../static/images/LolEmblemImages/emblem-gold.webp",
    "platinum": "../../static/images/LolEmblemImages/emblem-platinum.webp",
    "diamond": "../../static/images/LolEmblemImages/emblem-diamond.webp",
    "master": "../../static/images/LolEmblemImages/emblem-master.webp",
    "grandmaster": "../../static/images/LolEmblemImages/emblem-grandmaster.webp",
    "challenger": "../../static/images/LolEmblemImages/emblem-challenger.webp",
}


class Lol:

    def __init__(self, name, region):
        self.name = name
        self.region = region

    def actual_elo(self):
        items = {
            "nickname": "",
            "profile_icon": "",
            "solo_duo_rank": "Unranked",
            "solo_duo_tier": "default",
            "solo_duo_lp": "default",
            "flex_rank": "Unranked",
            "flex_tier": "default",
            "flex_lp": "default",
            "end_season": {
                "type": "",
                "status": "",
            },
        }

        try:
            url = requests.get(
                f"{link_region[self.region.lower()]}/lol/summoner/v4/summoners/by-name/{self.name}",
                headers={
                    "X-Riot-Token": app.config["RIOT_KEY"]
                }
            ).json()

            items["nickname"] = url["name"]

            version = requests.get(f"https://ddragon.leagueoflegends.com/api/versions.json").json()
            img_icon = f"http://ddragon.leagueoflegends.com/cdn/{version[0]}/img/profileicon/{url['profileIconId']}.png"
            items["profile_icon"] = img_icon

            url_elo = requests.get(
                f"{link_region[self.region.lower()]}/lol/league/v4/entries/by-summoner/{url['id']}",
                headers={
                    "X-Riot-Token": app.config["RIOT_KEY"]
                }
            ).json()

            for json in url_elo:
                if json["queueType"] == "RANKED_SOLO_5x5":
                    items["solo_duo_lp"] = json["leaguePoints"]
                    items["solo_duo_tier"] = images_elo[json["tier"].lower()]

                    if json['tier'] == 'MASTER' or json['tier'] == 'GRANDMASTER' or json['tier'] == 'CHALLENGER':
                        items["solo_duo_rank"] = ""
                    else:
                        items["solo_duo_rank"] = json["rank"]

                elif json["queueType"] == "RANKED_FLEX_SR":
                    items["flex_lp"] = json["leaguePoints"]
                    items["flex_tier"] = images_elo[json["tier"].lower()]

                    if json['tier'] == 'MASTER' or json['tier'] == 'GRANDMASTER' or json['tier'] == 'CHALLENGER':
                        items["flex_rank"] = ""
                    else:
                        items["flex_rank"] = json["rank"]

            for key, value in items.items():
                if key == "solo_duo_tier" and value == "default":
                    items["solo_duo_tier"] = images_elo["unranked"]

                elif key == "flex_tier" and value == "default":
                    items["flex_tier"] = images_elo["unranked"]

            # fetch end date of season
            date = (14, 11, 2022, 23)
            data = TimeCalculator(date)
            items["end_season"]["status"] = data.date_calc()[0]
            items["end_season"]["type"] = data.date_calc()[1]

            return items

        except KeyError:
            return False
