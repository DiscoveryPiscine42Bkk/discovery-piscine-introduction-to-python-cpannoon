number = int(input("Enter a number to display its multiplication tabel: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
