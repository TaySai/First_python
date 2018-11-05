# Loop until the value entered by the user is not valid (is not an actual number)
while True:
    try:
        # try to convert text to int
        x = int(input("Please enter a number: "))
        print(str(x) + " is a number!")
        break
    except ValueError:
        # return error if in contains alphabetic chars
        print("Oops! this is not a number")
