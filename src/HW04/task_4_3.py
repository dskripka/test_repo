dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
keys = dict.keys()
keys_list = list(keys)
i = 0
while i < len(keys_list):
    old_key = keys_list[i]
    lengh_keys =  len(keys_list[i])
    new_key = f' {old_key}{lengh_keys}'
    dict[new_key] = dict.pop(old_key)
    i += 1
print(dict)
