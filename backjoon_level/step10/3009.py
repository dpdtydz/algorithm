# 문제
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
#
# 입력
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.
#
# 출력
# 직사각형의 네 번째 점의 좌표를 출력한다.

x_points, y_points = [], []
return_x, return_y = None, None
for _ in range(3):
    x_point, y_point = input().split()
    x_points.append(x_point)
    y_points.append(y_point)
for i in range(3):
    if x_points.count(x_points[i]) == 1:
        return_x = x_points[i]
    if y_points.count(y_points[i]) == 1:
        return_y = y_points[i]
print(f"{return_x} {return_y}")
