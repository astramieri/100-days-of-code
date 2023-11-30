# Check leap year

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
        else:
            leap_year = False
    else:    
        leap_year = True
else:
    leap_year = False    

if leap_year:
    print(f"The year {year} is a leap year")
else:
     print(f"The year {year} is NOT a leap year")   
