import random

n = random.randint(1, 100)
counter = 1
print(f"THIS IS A GUESSING GAME------OF 1 - 100------- YOU ONLY HAVE 5 TRIES")
while True:

    try:

        user_input = int(input(f'This is the {counter} Guess \n>  '))
        break
    except ValueError as er:
        print('Sorry the number must be integer')


while counter <= 4:

    if user_input == n and counter == 1:
        print('Amazing you got the number on your first try')
        dy = """

                    oooooooooo       oooooo
                    oo             oo      oo  
                    oo   ooooo     oo      oo
                    oo      oo     oo      oo
                    oooooooooo       oooooo

                    """
        print(dy)
        exit()

    if user_input > 100:
        print("THIS IS A GUESSING GAME------OF 1 - 100\n>  ")
        counter -= 1

    counter += 1

    if user_input == n:
        print(f'You have guessed correctly\tThe number is {n}')
        exit()
    else:
        print(f"{user_input} This number doesn't match")

    if user_input < n:
        print(f'The number {user_input} is less than the real number')
        print('TRY AGAIN!!!\n')

    elif user_input > n:
        print(f'The number {user_input} is greater than the real number')
        print('TRY AGAIN!!!\n')
    user_input = int(input(f'This is the {counter} Guess\n>  '))

    if user_input == n:
        print(f'You have guessed correctly\tThe number is {n}')
        exit()

print('SORRY 0_0 you ran out of guess numbers')
print(f'The right number is {n}')
