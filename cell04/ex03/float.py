user_input = infut("Please enter a number: ")
try:
    number = float(user_input)
    if number.is_integer():
        print(f"the number {int(number)} is an integer.")
    elif '.' in user_input:
        print(f"The number {user_input} is a decimal.")
    else:
        print(f"the number {user_input} is not a decimal.")

except ValueError:
        print("That's not a vaild number.")