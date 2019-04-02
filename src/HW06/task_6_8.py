# В заданой строке расположить в обратном порядке все слова.
# Разделителем  слов считаются пробелы.
string = input('enter the string')
string = string.split()

i = 0
l = int(len(string))
j = l -1
new_string = []
while i < l and j >= 0:
    new_string.append(string[j])
    i += 1
    j -= 1

result = ' '.join(new_string)
print(result)