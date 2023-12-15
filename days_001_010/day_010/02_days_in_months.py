def is_leap_year(year):
    leap_year = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True
        else:    
            leap_year = True

    return leap_year

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days = month_days[month - 1]

    if month == 2 and is_leap_year(year):
        days += 1

    return days

#year = int(input("Enter a year: "))
#month = int(input("Enter a month: "))
#days = days_in_month(year, month)

for y in range(5):
    year = 2020 + y

    for n in range(12):
        month = 1 + n
        
        days = days_in_month(year, month)

        print(f"{year}-{str(month).zfill(2)}: {days}")
    