from datetime import datetime, timedelta
import calendar


class TimeCalculator:
    def __init__(self, date, month=False, day=False, hour=False):
        self.date = str(date)
        self.month = month
        self.day = day
        self.hour = hour
        self.today = datetime.today()

    def calc_month(self):
        final_date = datetime.strptime(self.date, "(%d, %m, %Y, %H)")
        difference = final_date - self.today

        day_current_month = calendar.monthrange(self.today.year, self.today.month)[1]
        start_date_next_month = self.today + timedelta(days=day_current_month - self.today.day + 1)
        end_date = start_date_next_month
        days = difference.days
        count = 0

        while days >= 30:
            count += 1

            day_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
            end_date = end_date + timedelta(days=day_current_month)

            days -= day_current_month

        return count

    def calc_day(self):
        final_date = datetime.strptime(self.date, "(%d, %m, %Y, %H)")
        difference = final_date - self.today

        return difference.days

    def calc_hour(self):
        final_date = datetime.strptime(self.date, "(%d, %m, %Y, %H)")
        difference = final_date - self.today

        return difference.days * 24 + (difference.seconds // 60) // 60

    def date_calc(self):
        try:
            if self.month is False and self.day is False and self.hour is False:
                if self.calc_month() > 0:
                    return [self.calc_month(), "Mês"] if self.calc_month() > 1 else [self.calc_month(), "Meses"]
                elif self.calc_day() > 0:
                    return [self.calc_day(), "Dias"] if self.calc_day() > 1 else [self.calc_day(), "Dia"]
                elif self.calc_day() == 0 and self.calc_hour() > 0:
                    return [self.calc_hour(), "Horas"] if self.calc_hour() > 1 else [self.calc_hour(), "Hora"]
                else:
                    return ["Terminada", "null"]

            elif self.month and self.calc_month() > 0:
                return [self.calc_month(), "Mês"] if self.calc_month() > 1 else [self.calc_month(), "Meses"]

            elif self.day and self.calc_day() > 0:
                return [self.calc_day(), "Dias"] if self.calc_day() > 1 else [self.calc_day(), "Dia"]

            elif self.hour and self.calc_hour() > 0:
                return [self.calc_hour(), "Horas"] if self.calc_hour() > 1 else [self.calc_hour(), "Hora"]

            else:
                return ["Terminada", "null"]

        except:
            return ["Indefinido", "null"]
