from TimeCalculator import TimeCalculator
import requests
from credentials.LolAPI import apikey

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
    "unranked": "../../static/images/LolEmblemImages/Emblem_Unranked.png",
    "iron": "../../static/images/LolEmblemImages/Emblem_Iron.png",
    "bronze": "../../static/images/LolEmblemImages/Emblem_Bronze.png",
    "silver": "../../static/images/LolEmblemImages/Emblem_Silver.png",
    "gold": "../../static/images/LolEmblemImages/Emblem_Gold.png",
    "platinum": "../../static/images/LolEmblemImages/Emblem_Platinum.png",
    "diamond": "../../static/images/LolEmblemImages/Emblem_Diamond.png",
    "master": "../../static/images/LolEmblemImages/Emblem_Master.png",
    "grandmaster": "../../static/images/LolEmblemImages/Emblem_Grandmaster.png",
    "challenger": "../../static/images/LolEmblemImages/Emblem_Challenger.png",
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
            url = requests.get(f"{link_region[self.region.lower()]}/lol/summoner/v4/summoners/by-name/{self.name}", params=apikey).json()

            img_icon = f"http://ddragon.leagueoflegends.com/cdn/11.9.1/img/profileicon/{url['profileIconId']}.png"
            items["profile_icon"] = img_icon

            player_name = requests.get(f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-puuid/{url['puuid']}", params=apikey).json()
            items["nickname"] = player_name["gameName"]

            url_elo = requests.get(f"{link_region[self.region.lower()]}/lol/league/v4/entries/by-summoner/{url['id']}", params=apikey).json()

            for json in url_elo:
                if json["queueType"] == "RANKED_SOLO_5x5":
                    items["solo_duo_rank"] = json["rank"]
                    items["solo_duo_lp"] = json["leaguePoints"]
                    items["solo_duo_tier"] = images_elo[json["tier"].lower()]

                elif json["queueType"] == "RANKED_FLEX_SR":
                    items["flex_rank"] = json["rank"]
                    items["flex_lp"] = json["leaguePoints"]
                    items["flex_tier"] = images_elo[json["tier"].lower()]

            for key, value in items.items():
                if key == "solo_duo_tier" and value == "default":
                    items["solo_duo_tier"] = images_elo["unranked"]

                elif key == "flex_tier" and value == "default":
                    items["flex_tier"] = images_elo["unranked"]

            # fetch end date of season
            date = ()
            data = TimeCalculator(date)
            items["end_season"]["type"] = data.date_calc()[1]
            items["end_season"]["status"] = data.date_calc()[0]

            return items

        except KeyError:
            return False
