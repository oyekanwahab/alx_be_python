number = int(input("Enter a number to see its multiplication table: "))
multiplier = range(1, 11)
for i in multiplier:
    result = (number * i )
    print(f"{number} * {i} = {result}")