print('1:Feet to Meter, 2:Meter to foot')
choice=int(input('Enter choice'))

if choice ==1:
    num = float(input('Enter number of feet'))
    print('Meters',round((num/3.28),3))
    
else:
    num = float(input('Enter number of meter'))
    print('Meters',round((num*3.28),3))