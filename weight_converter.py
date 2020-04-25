weight = float(input('Weight: '))
unit = input("(L)bs or (K)g: ")

if unit.upper() == 'L': 
    converted = round((weight / 2.2046226218488),2)
    print(f'You are {converted} kilos')
else: 
    converted = round((weight * 2.2046226218488),2)
    print(f'You are {converted} pounds')