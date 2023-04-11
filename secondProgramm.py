import calendar

year = int(input("Введите год: "))

month_sums = {i: 0 for i in range(1, 13)}

for month in range(1, 13):
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        date_sum = sum(int(digit) for digit in str(year) + str(month).zfill(2) + str(day).zfill(2))
        month_sums[month] += date_sum

year_sum = sum(month_sums.values())

for month in range(1, 13):
    print(f"Месяц {month}: {month_sums[month]}")
print(f"Всего за год: {year_sum}")