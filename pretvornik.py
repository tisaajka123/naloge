
while True:

    kilometri = int(input('vnesite razdaljo v kilometrih'))

    print(kilometri * 1.6)

    repeat = input('ali zelite ponoviti izracun (y/n)')

    if repeat == 'y':
        print(input('vnesite razdaljo v kilometrih'))
    elif repeat == 'n':
        print()
    break