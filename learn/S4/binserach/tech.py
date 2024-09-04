# binary search:

high = 1000
low = 0
guess = 1   

print(f"I will try to guess your number!")
print(f"Please think of a number between {low} and {high} in your head")
input("Press ENTER to start! ")

while low != high:

    # debugging
    print(f"\t Guessing in the range of: {range(low, high)}")

    current = low + (high - low) // 2
    response = (
        input(
            f"My guess is {current}, should I guess higher or lower? - Type (h/l/c-for correct): "
        )
        .casefold()
        .strip()
    )

    if response == "h":
        # Guess higher, low end of range becomes 1 greater than current
        low = current + 1
    elif response == "l":
        # Guess lower, higher end of the guess 1 less than current
        high = current - 1
    elif response == "c":
        print(f"Your number is {current} and I got it in {guess} number of guesses!")
        break
    else:
        print("Please enter h/l/c")

    guess+=1
else:
    # runs if "c" was not pressed and loop completed
    print(f"You thought of the number {high} and I got it in {guess} number of guesses!")
