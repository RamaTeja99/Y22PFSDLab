import random
random_color_hex = "#{:06x}".format(random.randint(0, 0xFFFFFF))
print("Random Color Hex:", random_color_hex)

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
random_alphabet_string = ''.join(random.choice(letters) for _ in range(8))
print("Random Alphabet String:", random_alphabet_string)

random_value = random.randint(5, 15)
print("Random Value between 5 and 15:", random_value)

random_multiple_of_seven = random.randint(0, 10) * 7
print("Random Multiple of 7 between 0 and 70:", random_multiple_of_seven)
