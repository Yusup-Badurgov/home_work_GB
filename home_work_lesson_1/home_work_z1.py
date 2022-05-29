duration = None

while True:
    duration = int(input("Введите количеству секунд: "))
    if duration < 60:
        sec = duration
        print(f"{sec} сек")
    elif 60 <= duration < 3600:
        minute = duration // 60
        sec = duration - (minute * 60)
        if duration == 60:
            print(f"{minute} мин")
        else:
            print(f"{minute} мин, {sec} сек ")
    elif 3600 <= duration < 86400:
        hour = (duration // 60) // 60
        minute = (duration // 60) - (hour * 60)
        sec = duration - (minute * 60) - ((hour * 60) * 60)
        if duration == 3600:
            print(f"{hour} ч")
        else:
            print(f"{hour} ч, {minute} мин, {sec} сек")
    elif duration >= 86400:
        day = ((duration // 60) // 60) // 24
        hour = ((duration // 60) // 60) - (day * 24)
        minute = (duration // 60) - (hour * 60) - ((day * 24) * 60)
        sec = duration - (minute * 60) - ((hour * 60) * 60) - (((day * 24) * 60) * 60)
        if duration == 86400:
            print(f"{day} д")
        else:
            print(f"{day} д, {hour} ч, {minute} мин, {sec} сек")