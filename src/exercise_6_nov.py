# Validate all strings with numbers and only one "." (point)
sentence = input('Type your text: ')
tester = None
message = "Good! Your text respect the conditions"
for letter in sentence:
    # testing if the letter is a point
    if letter == "." or letter == ",":
        # testing if it's the first point
        if not tester or tester is None:
            tester = True
        else:
            # if not first point
            tester = False
            message = 'you have more than one "." or ","'
            break
    # testing if the letter is a decimal or not
    else:
        try:
            # try to convert text to int
            x = int(letter)
        except ValueError:
            # return error if in contains alphabetic chars
            message = 'Alphabetic char detected, you must have only numbers and one and only one "." or ","'
            tester = False
            break
# display text depending on the result
if tester is None:
    print('this is an integer and not a float')
elif tester:
    print(message)
else:
    print(message)
