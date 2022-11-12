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


class Tft:

    def __init__(self, name, region):
        self.name = name
        self.region = region

    def actual_elo(self):
        items = {
            "nickname": "",
            "profile_icon": "",
            "rank": "",
            "tier": "default",
            "points": "Unranked",
            "end_season": {
                "type": "",
                "status": "",
            },
        }

        try:
            url = requests.get(
                f"{link_region[self.region.lower()]}/tft/summoner/v1/summoners/by-name/{self.name}",
                headers={
                    "X-Riot-Token": app.config["RIOT_KEY"]
                }
            ).json()

            items["nickname"] = url["name"]

            version = requests.get(f"https://ddragon.leagueoflegends.com/api/versions.json").json()
            img_icon = f"http://ddragon.leagueoflegends.com/cdn/{version[0]}/img/profileicon/{url['profileIconId']}.png"
            items["profile_icon"] = img_icon

            url_elo = requests.get(
                f"{link_region[self.region.lower()]}/tft/league/v1/entries/by-summoner/{url['id']}",
                headers={
                    "X-Riot-Token": app.config["RIOT_KEY"]
                }
            ).json()

            for json in url_elo:
                if json["queueType"] == "RANKED_TFT":
                    items["points"] = json["leaguePoints"]
                    items["tier"] = images_elo[json["tier"].lower()]

                    if json['tier'] == 'MASTER' or json['tier'] == 'GRANDMASTER' or json['tier'] == 'CHALLENGER':
                        items["rank"] = ""
                    else:
                        items["rank"] = json["rank"]

            for key, value in items.items():
                if key == "tier" and value == "default":
                    items["tier"] = images_elo["unranked"]

            # fetch end date of season
            date = (7, 12, 2022, 12)
            data = TimeCalculator(date)
            items["end_season"]["type"] = data.date_calc()[1]
            items["end_season"]["status"] = data.date_calc()[0]

            return items

        except KeyError:
            return False
