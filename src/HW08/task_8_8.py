# Даны три слова. Выяснить, является ли хоть одно из них палиндромом("перевертышем"),
# т.е. таким, которое читается одинаково слева направо и справа налево. (Определить функцию,
# позволяющую распознавать слова палиндромы)

def reverse(s):
    return s[::-1]

def ispalindrome(s):
    rev = reverse(s)
    if s == rev:
        return True
    return False

list = ['word', 'devel', 'level', 'keyboard', 'radar']
print(list)

for word in list:
    ans = ispalindrome(word)
    if ans == 1:
        print(f'{word} Yes')
    else:
        print(f'{word} No')
