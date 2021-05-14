# def validator_of_response(inp):
#     """
#     Valida a continuação do loop.
#     :param inp: Mensagem do input que será vista pelo usuário.
#     :return: Resposta de sim ou não no caso s/n.
#     """
#     while True:
#         stop = str(input(inp)).lower().strip()
#         if stop not in "ns" or stop in "":
#             print("\033[31mThis isn't accept. try again!\033[m")
#             continue
#         else:
#             return stop
#
#
# def validator_of_name(inp):
#     """
#     Valida o nome inserido.
#     :param inp: Mensagem do input que será vista pelo usuário.
#     :return: Nome do usuário.
#     """
#     while True:
#         word_inp = str(input(inp)).strip().replace(" ", "")
#         if word_inp.isalpha() is False:
#             print("\033[31mThis isn't accept. try again!\033[m")
#         else:
#             return word_inp

items = {
            "nickname": "",
            "profile_icon": "",
            "solo_duo_rank": "default",
            "solo_duo_tier": "default",
            "flex_rank": "default",
            "flex_tier": "default",
            "days": "",
        }

images_elo = {
            "unranked": "static/images/LolEmblemImages/Emblem_Unranked.png",
            "iron": "static/images/LolEmblemImages/Emblem_Iron.png",
            "bronze": "static/images/LolEmblemImages/Emblem_Bronze.png",
            "silver": "static/images/LolEmblemImages/Emblem_Silver.png",
            "gold": "static/images/LolEmblemImages/Emblem_Gold.png",
            "platinum": "static/images/LolEmblemImages/Emblem_Platinum.png",
            "diamond": "static/images/LolEmblemImages/Emblem_Diamond.png",
            "master": "static/images/LolEmblemImages/Emblem_Master.png",
            "grandmaster": "static/images/LolEmblemImages/Emblem_Grandmaster.png",
            "challenger": "static/images/LolEmblemImages/Emblem_Challenger.png",
        }

for key, value in items.items():
    if key == "solo_duo_tier" and value == "default":
        items["solo_duo_tier"] = images_elo["unranked"]

    if key == "flex_tier" and value == "default":
        items["flex_tier"] = images_elo["unranked"]

print(items)