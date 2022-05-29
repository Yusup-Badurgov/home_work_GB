my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#вариант без создания нового списка
idx = 0
while idx < len(my_list):
    if my_list[idx].isdigit():
        my_list[idx] = f'{int(my_list[idx]):02d}'
        my_list.insert(idx, '"')
        my_list.insert(idx + 2, '"')
        idx += 2
    elif my_list[idx].startswith("+"):
        my_list[idx] = f'{my_list[idx][0]}{int(my_list[idx]):02d}'
        my_list.insert(idx, '"')
        my_list.insert(idx + 2, '"')
        idx += 2
    else:
        idx += 1

print(my_list)
result = " ".join(my_list)
print(result)
