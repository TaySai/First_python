# Reading a value on the command line and converting it into a float
try:
    # try to convert int to float
    x = int(input("Please enter a number: "))
    x = float(x)
    print(x)
except ValueError:
    # return error if in contains alphabetic chars
    print("Oops! this is not a number")
