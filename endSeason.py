from datetime import date


def end_season():
    try:
        end_date = date(2020, 8, 6)
        today = date.today()
        difference = end_date - today

        if int(difference.days) > 0:
            print(f"Faltam {difference.days} dias para o final da season.")

        elif not difference:
            print(f"Acaba hoje")

        else:
            print(f"Já acabou a season.")

    except:
        print("data ainda indeterminada")


end_season()


