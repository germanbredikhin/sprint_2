from random import randint

number = randint(1, 100)
print(f'Guess the number between 1 and 100 / {number}')

while True:
    guess = int(input('Your guess '))

    if guess < number:
        print('Too low, try again')
    elif guess > number:
        print('Too high, try again')
    elif guess == number:
        break

print(f'Bingo!, it is {number}!')