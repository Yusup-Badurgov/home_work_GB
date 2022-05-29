percent = int(input("Введите число процентов: "))
if percent == 1:
    word = "процент"
elif percent <= 4:
    word = "процента"
else:
    word = "процентов"
print(percent, word)
