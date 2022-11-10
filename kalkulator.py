
operation = input('Kakšno operacijo želiš izvajati (+-*/)')

num1 = int(input('Vnesi prvo število '))
num2 = int(input('Vnesi drugo število '))

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)
else:
    print('Nisi podal pravilne operacije')

