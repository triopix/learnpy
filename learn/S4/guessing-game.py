answer = 5

print("Please enter a number between 1-10: ")
n = int(input())

if n != answer:
    if n > answer:
        print("Please guess lower")
    elif n < answer:
        print("Please guess higher")
    
    n = int(input())
    
    if n == answer:
        print("You got it!")
    else:
        print("You didn't get it :(")
else:
    print("Congratulations, you got it the first time!")

    
    