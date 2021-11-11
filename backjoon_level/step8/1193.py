# 문제
# 무한히 큰 배열에 다음과 같이 분수들이 적혀있다.
#
# 1/1	1/2	1/3	1/4	1/5	…
# 2/1	2/2	2/3	2/4	…	…
# 3/1	3/2	3/3	…	…	…
# 4/1	4/2	…	…	…	…
# 5/1	…	…	…	…	…
# …	…	…	…	…	…
# 이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
#
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

n = int(input())
line = 0
end = 0
while n > end:
    line += 1
    end += line

diff = end - n
if line % 2 == 0:  # 짝수일때
    top = line - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff
print("%d/%d" % (top, bottom))
