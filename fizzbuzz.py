
select = input("vnesi stevilo med 1 and 100: ")
select = int(select)

for num in range(1, select+1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)