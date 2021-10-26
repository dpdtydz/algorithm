# 문제
# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
#
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
#
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
#
# 출력
# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
a, b, c = map(int, input().split())

# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
result = ((a + b) % c)
result2 = ((a % c) + (b % c)) % c
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
result3 = ((a * b) % c)
resulf4 = ((a % c) * (b % c)) % c
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

print(result)
print(result2)
print(result3)
print(resulf4)