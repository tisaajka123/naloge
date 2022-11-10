
secret_number = 42

guess = int(input('Ugani skrivno številko - med 1 in 50'))

if guess == secret_number:
    print('Uganil si - čestitamo! Številka je 42')
else:
    print('Oprosti, napačna številka...Skrita številka ni' + str(guess))
