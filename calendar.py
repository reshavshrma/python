class Calendar:
        def __init__(self) -> None:
                self.week_day_names = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
                self.months_name_code_daycount = ((0, "Jan", 31), (3, "Feb", 28), (3, "Mar", 31), (6, "Apr", 30),
                        (1, "May", 31), (4, "Jun", 30), (6, "July", 31), (2, "Aug", 31), (5, "Sep", 30), (0, "Oct", 31), (3, "Nov", 30), (5, "Dec", 31))

	#leap year 
        def is_leap_year(self, year: int) -> bool:
                if (year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0):
                        return True
                else:
                        return False

        def get_year_special_code(self, year: int) -> int:
                mod_year = year % 400
                if mod_year < 100 and mod_year >= 0:
                        return 6
                if mod_year < 200 and mod_year >= 100:
                        return 4
                if mod_year < 300 and mod_year >= 200:
                        return 2
                if mod_year < 400 and mod_year >= 300:
                        return 0

        def get_week_day_index_from_date(self, date: int, month: int, year: int) -> str:
                week_day_names_index = (date + self.months_name_code_daycount[month - 1][0] + self.get_year_special_code(year) + (year % 100) + (year % 100) // 4) % 7

                if self.is_leap_year(year) and (month <= 2 and month > 0):
                        week_day_names_index -= 1

                week_day_names_index = week_day_names_index % 7

                return week_day_names_index

        def print_week_day_horizontally(self): 
                for week_day in self.week_day_names:
                        print(week_day, end="|")
                print()

        def print_space(self, count):
                for i in range(count):
                        print("   ", end='|')

        def print_month(self, month: int):
                print(self.months_name_code_daycount[month][1].center(28, '-'))

        def print_month_days(self, start_week_day_index: int, month: int, year: int):
                days_in_month = self.months_name_code_daycount[month][2]
                if self.is_leap_year(year) and month == 1:
                        days_in_month += 1
                self.print_space(start_week_day_index)
                for i in range(1, days_in_month + 1):
                        if i >= 10:
                                print('', i, end='|')
                        else:
                                print(' ', i, end='|')
                        if ((start_week_day_index + i) % 7 == 0):
                                print()
                self.print_space(35 - (start_week_day_index + days_in_month)) 
                return (start_week_day_index + days_in_month) % 7

	# prit calendar
        def print_month_by_user_input(self):
                year = int(input("Enter the year: "))
                month = int(input("Enter the month (1-12): "))
                if 1 <= month <= 12:
                        week_day_index = self.get_week_day_index_from_date(1, month, year)
                        self.print_month(month - 1)
                        self.print_week_day_horizontally()
                        self.print_month_days(week_day_index, month - 1, year)
                        print()
                else:
                        print("Invalid month.")

cal = Calendar()
cal.print_month_by_user_input()
