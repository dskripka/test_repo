d = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
lengh_keys = len(dict.keys(d))
lengh_keys = [len(key) for key in d.keys()]
print(lengh_keys)
