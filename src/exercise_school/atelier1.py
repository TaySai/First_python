# import random
# print(random.randint(1, 12))
#
#
# def is_int():
#     nb = input('Choose a number: ')
#     return nb
#
#
# number = is_int()
#
# while not(number.isdigit()):
#         print("this is not a number")
#         number = is_int()
# print(number)
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         print(x)
#         break
#     except ValueError:
#         print("Oops! wrong number")
#
# print(number)


# def is_int_rec():
#     nb = input('Choose a number: ')
#     if not(nb.isdigit()):
#         return is_int_rec()
#     return nb
#
#
# print(is_int_rec())
b = 1
c = 0
a = 0
print(a)
try:
    a = b/c
except NameError as e:
    print("t'es null on peut pas diviser par 0")
finally:
    a = None
print(a)
# colors = {
#    '#ff9900': 'orange',
#    '#00ff00': 'vert',
#    '#ff0000': 'rouge',
#    '#ff00ff': 'violet',
#    '#0000ff': 'bleu',
#    '#000000': 'noir',
#    '#ffffff': 'blanc',
#    '#ffff00': 'jaune'
# }
#
# selected = ''
#
# print('<select name="colors">')
# for cnt in colors:
#     print('\t<option value="{}" {} />{}</option>'.
#           format(cnt, "selected" if colors[cnt] == 'rouge' else "", colors[cnt]))
# print('</select>')
#