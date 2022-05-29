def thesaurus(*args):
    dict = {}
    for name in args:
        first_let = name[0]
        if first_let not in dict:
            dict[first_let] = []
        dict[first_let].append(name)
    return dict


print(thesaurus('Адам', 'Мария', 'Марина', 'Андрей', 'Антон'))
