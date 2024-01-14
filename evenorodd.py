#A program that checks if a number is even or odd 

print("Hey there!")

while True:
    try:
        userInput = int(input("Enter the number you would like to check: "))

        if userInput % 2 == 0:
            print("This is an even number")
        else:
            print("This is an odd number")

    except ValueError:
        print("Error! This is not a number")

    end = input("Thank you for using this program! Would you like to go again? (Yes/No): ")

    if end.lower() != 'yes':
        print("Bye-Bye")
        break
