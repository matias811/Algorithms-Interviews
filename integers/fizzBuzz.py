"""
FIZZ BUZZ
It's a challenge where you have to print find numbers that are divisible by 3 and 5
If the number is divisible by 3 you print FIZZ
If the number is divisible by 5 your print BUZZ
If the number is divisible by 3 and 5 you print FIZZ BUZZ
As an extra addition we put user input and handle exceptions
"""


def get_user_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


end = get_user_input("Enter the end of the range: ")

for i in range(1, end + 1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
