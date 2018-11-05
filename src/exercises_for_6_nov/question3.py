# Validate all strings with numbers and only one "." (point)

sentence = input('Type your text: ')
tester = None
message = "Good! Your text respect the conditions"
for letter in sentence:
    # testing if the letter is a point
    if letter == ".":
        # testing if it's the first point
        if not tester or tester is None:
            tester = True
        else:
            # if not first point
            tester = False
            message = 'you have more than one "."'
            break
    # testing if the letter is a decimal or not
    elif not letter.isdecimal():
        message = 'you must have only numbers and one and only one "."'
        tester = False
        break
# display text depending on the result
if tester is None:
    print('you forgot to add a "."')
elif tester:
    print(message)
else:
    print(message)
