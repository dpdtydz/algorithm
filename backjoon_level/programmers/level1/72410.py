def solution(new_id):
    answer = ''
    # 1단계 모든 대문자를 소문자로 치환
    new_id = new_id.lower()
    # 2단계 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자를 제거
    for _ in new_id:
        if _.isalnum() or _ in "-_.":
            answer += _
    # 3단계 new_id에서 마침표가 두번이상 연속된 부분을 하나의 마침표로
    while ".." in answer:
        answer = answer.replace("..", ".")
    # 4단계
    if answer and answer[0] == ".":
        answer = answer[1:]
    if answer and answer[-1] == ".":
        answer = answer[:-1]
    # 5단계
    if not answer:
        answer += 'a'
    # 6단계
    if len(new_id) >= 16:
        if answer[14] == ".":
            answer = answer[:14]
        else:
            answer = answer[:15]
    # 7단계
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3 - len(answer))
    return answer

# 길이는 3자 이상 15자 이하
# 아이디는 알파벳,소문자 숫자,빼기,밑줄,마침표 문자만 사용
# 마침표는 청므과 끝에 사용 할 수 없다, 연속으로 사용 불가능
test = "dpdty22dz"
solution(test)
