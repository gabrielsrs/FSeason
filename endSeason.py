from datetime import date


class Endseason:
    def __init__(self, end_date):
        self.end_date = end_date

    def end_season(self):
        try:
            end_date = date(self.end_date[0], self.end_date[1], self.end_date[2])
            today = date.today()
            difference = end_date - today

            if int(difference.days) > 0:
                return difference.days

            elif not difference:
                return difference.days

            else:
                return difference.days

        except:
            print("data ainda indeterminada")


# d = 2021, 5, 20
# print(d)
# t = Endseason(end_date=d)
# print(t.end_season())
