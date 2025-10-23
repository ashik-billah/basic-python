num1 = int(input('Enter integer number 1: '))
num2 = int(input('Enter integer number 2: '))
num3 = int(input('Enter integer number 3: '))

if (num1>num2) and (num1>num3):print(num1,'is larger number')
elif (num2>num1) and (num2>num3):print(num2,'is larger number')
else:
    print(num3,'is larger numnber')

#another logic
    num1 = int(input('Enter integer number 1: '))
num2 = int(input('Enter integer number 2: '))
num3 = int(input('Enter integer number 3: '))

largest = max(num1, num2, num3)
print(largest, 'is the largest number')
