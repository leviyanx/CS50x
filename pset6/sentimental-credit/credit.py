from cs50 import get_string

# get card number
card_number = get_string("Number: ")
card_number_str_list = list(card_number)
card_number_list = []

# all are numbers?
if card_number.isdigit():
    for num in card_number_str_list:
        card_number_list.append(int(num))
else:
    # there is character which is not number
    print("INVALID\n")
    exit()

"""Luhn's algorithm"""
# reverse the sort of number
card_number_list.reverse()
reversed_card_number_list = card_number_list

# get all digit which need to multiply 2, and then multiply 2
tmp_list = []
for num in reversed_card_number_list[1::2]:
    tmp_list.append(num*2)

# add products' digits
sum1 = 0
for num in tmp_list:
    if num > 9:
        # split an integer into digit and add digits
        for num1 in str(num):
            sum1 += int(num1)
    else:
        sum1 += num

# get rest digits
sum2 = 0
for num in reversed_card_number_list[::2]:
    sum2 += num

# add two sum
sum = sum1 + sum2

# check the last digit if is 0
if list(str(sum))[-1] != '0':
    print("INVALID\n")
    exit()

# distinguish which card
first_letter = card_number_str_list[0]
first_two_letter = card_number[:2]

if first_letter == '4':
    print("VISA\n")
elif first_two_letter == '34' or first_two_letter == '37':
    print("AMEX\n")
elif first_two_letter == '51' or first_two_letter == '52' or first_two_letter == '53' or first_two_letter == '54' or first_two_letter == '55':
    print("MASTERCARD\n")
else:
    print("INVALID\n")
