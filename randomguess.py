
import random


def get_random():
    number_generate = random.randint(1, 100)
    return number_generate


def play_game():
    game_counter = 1
    game_chances = 5

    n = get_random()

    print(f"THIS IS A GUESSING GAME------OF 1 - 100------- YOU ONLY HAVE 5 TRIES")

    while True:

        try:
            print()
            print("*" * 30)
            print(f"Guess {game_counter} of {game_chances}")
            print("*" * 30)
            user_input = int(input('>  '))
            break
        except ValueError as er:
            print('Sorry the number must be integer')

    while game_counter < game_chances:

        if user_input == n and game_counter == 1:
            print('Amazing you got the number on your first try')
            dy = """
    
                        oooooooooo       oooooo
                        oo             oo      oo  
                        oo   ooooo     oo      oo
                        oo      oo     oo      oo
                        oooooooooo       oooooo
    
                        """
            print(dy)
            break

        if user_input > 100:
            print("THIS IS A GUESSING GAME------OF 1 - 100\n>  ")
            game_counter -= 1

        game_counter += 1

        if user_input == n:
            print(f'You have guessed correctly\tThe number is {n}')
            break
        else:
            print(f"{user_input} This number doesn't match")

        if user_input < n:
            print(f'The number {user_input} is less than the real number')
            print('TRY AGAIN!!!\n')

        elif user_input > n:
            print(f'The number {user_input} is greater than the real number')
            print('TRY AGAIN!!!\n')

        while True:

            try:
                print()
                print("*" * 30)
                print(f"Guess {game_counter} of {game_chances}")
                print("*" * 30)

                user_input = int(input('>  '))
                break
            except ValueError as er:
                print('Sorry the number must be integer')

        if user_input == n:
            print(f'You have guessed correctly\tThe number is {n}')
            break

    print('SORRY 0_0 you ran out of guess numbers')
    print(f'The right number is {get_random()}')


if __name__ == '__main__':
    play_game()
