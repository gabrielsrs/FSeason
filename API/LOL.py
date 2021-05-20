from endSeason import Endseason
import requests


class Lol:

    def __init__(self, name, region):
        self.name = name
        self.region = region

    def actual_elo(self):
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
        # ../ usado devido o parametro de rota
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

        key = "RGAPI-c6e47ede-e228-4a62-82c6-1a8317bd43a4"
        try:
            url = requests.get(f"{link_region[self.region.lower()]}/lol/summoner/v4/summoners/by-name/{self.name}?api_key={key}")

            img_icon = f"http://ddragon.leagueoflegends.com/cdn/11.9.1/img/profileicon/{url.json()['profileIconId']}.png"
            items["profile_icon"] = img_icon

            player_name = requests.get(f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-puuid/{url.json()['puuid']}?api_key={key}")
            items["nickname"] = player_name.json()["gameName"]

            url_elo = requests.get(f"{link_region[self.region.lower()]}/lol/league/v4/entries/by-summoner/{url.json()['id']}?api_key={key}")


            # just the position in for statement
            for position, dict in enumerate(url_elo.json()):
                if url_elo.json()[position]["queueType"] in "RANKED_SOLO_5x5":
                    items["solo_duo_rank"] = url_elo.json()[position]["rank"]
                    items["solo_duo_lp"] = url_elo.json()[position]["leaguePoints"]
                    items["solo_duo_tier"] = images_elo[url_elo.json()[position]["tier"].lower()]

                elif url_elo.json()[position]["queueType"] in "RANKED_FLEX_SR":
                    items["flex_rank"] = url_elo.json()[position]["rank"]
                    items["flex_lp"] = url_elo.json()[position]["leaguePoints"]
                    items["flex_tier"] = images_elo[url_elo.json()[position]["tier"].lower()]

            for key, value in items.items():
                if key == "solo_duo_tier" and value == "default":
                    items["solo_duo_tier"] = images_elo["unranked"]

                elif key == "flex_tier" and value == "default":
                    items["flex_tier"] = images_elo["unranked"]

            # seek a data from the final season
            data = ()
            test = Endseason(data)
            items["end_season"]["type"] = test.date_calc()[1]
            items["end_season"]["status"] = test.date_calc()[0]

            print(items)
            return items

        except KeyError:
            return False

# test = Lol("gfdsgdgdfgdffd", "br1")
# test.actual_elo()
