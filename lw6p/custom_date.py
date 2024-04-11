class CustomDate:

    DAYS_IN_NON_LEAP_MONTHS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, day, month, year):
        self.set_year(year)
        self.set_month(month)
        self.set_day(day)

    @staticmethod
    def get_days_in_month(month, year):
        if month == 2 and CustomDate.is_leap_year(year):
            return 29
        else:
            return CustomDate.DAYS_IN_NON_LEAP_MONTHS[month - 1]

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    def get_day(self):
        return self.__day

    def get_month(self):
        return self.__month

    def get_year(self):
        return self.__year

    def set_day(self, day):
        if not (1 <= day <= CustomDate.get_days_in_month(self.__month, self.__year)):
            raise ValueError("Invalid day")
        self.__day = day

    def set_month(self, month):
        if not (1 <= month <= 12):
            raise ValueError("Invalid month")
        self.__month = month

    def set_year(self, year):
        if not (1 <= year <= 9999):
            raise ValueError("Invalid year")
        self.__year = year

    def next_day(self):
        if (
            self.__day == CustomDate.get_days_in_month(self.__month, self.__year)
            and self.__month == 12
            and self.__year == 9999
        ):
            raise ValueError("Not possible to increase")
        if self.__day == CustomDate.get_days_in_month(self.__month, self.__year):
            self.__day = 1
            if self.__month == 12:
                self.__month = 1
                self.__year += 1
            else:
                self.__month += 1
        else:
            self.__day += 1

    def previous_day(self):
        if self.__day == 1 and self.__month == 1 and self.__year == 1:
            raise ValueError("Not possible to decrease")

        if self.__day == 1:
            self.__day = CustomDate.get_days_in_month(self.__month, self.__year)
            if self.__month == 1:
                self.__month = 12
                self.__year -= 1
            else:
                self.__month -= 1
        else:
            self.__day -= 1

    def compare_to(self, other_date: "CustomDate") -> int:
        if self.__year > other_date.get_year():
            return 1
        elif self.__year < other_date.get_year():
            return -1
        elif self.__month > other_date.get_month():
            return 1
        elif self.__month < other_date.get_month():
            return -1
        elif self.__day > other_date.get_day():
            return 1
        elif self.__day < other_date.get_day():
            return -1
        else:
            return 0

    def difference_in_days(self, other):
        total_days = 0
        while self.compare_to(other) != 0:
            if self.compare_to(other) > 0:
                self.previous_day()
            else:
                self.next_day()
            total_days += 1
        return total_days

    def __str__(self):
        return "%02d.%02d.%04d" % (self.__day, self.__month, self.__year)
