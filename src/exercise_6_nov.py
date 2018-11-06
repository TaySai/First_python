# we ask the user to tape a good value until he give the good answer
while True:
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
        break
    else:
        print(message)

# conversion to float
tester = True
length_sentence = len(sentence)
i = 0
power_pos = 0
power_neg = -1
float_number = float(0)
# print(length_sentence)
while i <= length_sentence-1:
    if sentence[i].isdecimal() and tester:
        float_number = float_number * (10 ** power_pos) + float(sentence[i])
        power_pos = 1
    elif not tester:
        float_number = float(sentence[i]) * (10 ** power_neg) + float_number
        power_neg -= 1
    else:
        tester = False
    i += 1
print(type(float_number))
print(float_number)

