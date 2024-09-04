LOW = 1
HIGH = 1000


def guess_binary(answer, low, high):
    guesses = 1
    while True:
        guess = low + (high - low) // 2
        if guess < answer:
            low = guess + 1
        elif guess > answer:
            high = guess - 1
        elif guess == answer:
            return guesses

        guesses += 1


correct_count = 0
max_guesses = 0

for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print(f"{number} guessed in {number_of_guesses} guesses")

    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses, 1
    elif number_of_guesses == max_guesses:
        correct_count += 1

print(f"I guessed without being told {correct_count} times. \
Max {max_guesses} guesses")
