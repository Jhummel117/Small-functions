measurement = int(input('measurement: '))
unit = input('(G) or (O): ')
if unit.upper() == "G":
    converted = measurement / 28.35
    print(f"measurement is {converted} ounces.")
else:
    converted = measurement * 28.35
    print(f"measurement is {converted} grams.")



