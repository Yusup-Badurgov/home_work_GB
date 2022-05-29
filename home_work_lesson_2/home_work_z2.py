my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_2 = []

for i in my_list:
    if i.isdigit():
        list_2.extend(['"' + f'{int(i):02d}' + '"'])
    else:
        if i.startswith("+"):
            list_2.extend(['"' + f'{i[0]}{int(i[1]):02d}' + '"'])
        else:
            list_2.append(i)

print(list_2)
result = " ".join(list_2)
print(result)