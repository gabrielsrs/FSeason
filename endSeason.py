from datetime import datetime


class Endseason:
    def __init__(self, date, month=False, day=False, hour=False):
        self.date = date
        self.month = month
        self.day = day
        self.hour = hour

    def calc_month(self):
        today = datetime.today()
        dates = datetime(self.date[0], self.date[1], self.date[2], self.date[3], self.date[4], self.date[5])
        difference = dates.month - today.month
        return difference

    def calc_day(self):
        today = datetime.today()
        dates = datetime(self.date[0], self.date[1], self.date[2], self.date[3], self.date[4], self.date[5])
        difference = dates - today
        return difference.days

    def calc_hour(self):
        # o calculo de horas n aceita 24h apenas ate 23, se resultado == 0 retorna none(no caso hora alual - hora atual)
        today = datetime.today()
        dates = datetime(self.date[0], self.date[1], self.date[2], self.date[3], self.date[4], self.date[5])
        difference = dates.hour - today.hour
        return difference

    def date_calc(self):
        try:
            # se setar tudo como true o resultado segue a ordem q foi feita abaixo
            if self.month and self.calc_month() > 0:
                return [self.calc_month(), "month"]

            elif self.day and self.calc_day() > 0:
                return [self.calc_day(), "day"]

            elif self.hour and self.calc_hour() > 0:
                return [self.calc_hour(), "hour"]

            elif self.month is False and self.day is False and self.hour is False:
                if self.calc_month() > 0:
                    return [self.calc_month(), "month"]
                elif self.calc_day() > 0:
                    return [self.calc_day(), "day"]
                elif self.calc_day() == 0 and self.calc_hour() is not None:
                    return [self.calc_hour(), "hour"]

            else:
                return ["Terminada", "null"]

        except:
            return ["Indefinido", "null"]


# d = (2021, 5, 16, 23, 0, 0)
# t = Endseason(date=d)
# print(t.date_calc())
