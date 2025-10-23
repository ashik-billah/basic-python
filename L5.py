year = int(input('Enter the year (4 digit) to check'))

if (year%400==0 or (year%4==0 and year%100!=0)):
    print(year,'is leap year')
else:
    print(year,'is not leap year')
                 
