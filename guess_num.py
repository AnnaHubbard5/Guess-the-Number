import random

def guess(x):
    rand_num = random.randint(1,x)
    guess = 0
    while guess != rand_num:
        guess = int(input(f'Guess a number between 1 and {x}: ')) //number must be an int
        if guess < rand_num:
            print('Guess a higher number!')
        elif guess > rand_num
            print('Guess a lower number!')
    print(f'You guessed the number! It was {rand_num}.')

guess(10)
