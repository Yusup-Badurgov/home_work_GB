my_list = []

for i in range(1, 1000, 2):
    i **= 3
    my_list.append(i)
print(my_list)
#a
sum_number = 0
for i in my_list:
    j = i
    sum_digit = 0
    while j > 0:
        last_num = j % 10
        sum_digit += last_num
        j //= 10
    if sum_digit % 7 == 0:
        sum_number += i

print(f"{sum_number} = сумма чисел списка, сумма цифр которых делится нацело на 7")
#C
sum_number_2 = 0
for i in my_list:
    i += 17
    j = i
    sum_digit = 0
    while j > 0:
        last_num = j % 10
        sum_digit += last_num
        j //= 10
    if sum_digit % 7 == 0:
        sum_number_2 += i

print(f"{sum_number_2} = сумма чисел списка, к которому прибавлено 17 и сумма цифр которых делится нацело на 7")
