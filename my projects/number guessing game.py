import random
max_number = 100
low_number = 0
playing = True
guesses = 0
answer = random.randint(low_number, max_number)
while playing:
    guess = int(input(f"enter your guess between {low_number} and {max_number}: "))
    guesses += 1
    if guess < low_number or guess > max_number:
        print(f"invalid guess!!! please enter a number between{low_number} and {max_number}")
        print(f"try again")
    elif guess > answer:
        print(f"your number is too high")
    elif guess < answer:
        print(f"your number is too low ")
    elif guess == answer:
        print(f"guessed correct number is {answer}")
        print(f"it took you {guesses} guesses")
    else:
        print(f"enter valid input between {low_number} and {max_number}")
playing = False
