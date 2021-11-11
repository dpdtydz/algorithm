# 알파벳 대소문자로 된 단어가 주어지면,
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오
# . 단, 대문자와 소문자를 구분하지 않는다.

string = input()
string = string.upper()
string_set = list(set(string))

a = []

for i in string_set:
    a.append(string.count(i))

if len(list(filter(lambda x: a[x] == max(a), range(len(a))))) > 1:
    print("?")
else:
    print(string_set[a.index(max(a))].upper())
