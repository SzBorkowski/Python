def duplicate_remover_sets(x):
    new_list = [*set(x)]
    return new_list

def duplicate_remover_sets_v2(x):
    return list(set(x))

def duplicate_remover_loop(x):
    new_list = []
    for element in x:
        if element not in new_list:
            new_list.append(element)
    return new_list

a = [1, 1, 2, 5, 3, 4, 5, 6]
print(duplicate_remover_sets(a))
print(duplicate_remover_sets_v2(a))
print(duplicate_remover_loop(a))