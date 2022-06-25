import re


def solution(s):
    st = s
    answer = 0
    st = re.sub('zero', '0', st)
    st = re.sub('one', '1', st)
    st = re.sub('two', '2', st)
    st = re.sub('three', '3', st)
    st = re.sub('four', '4', st)
    st = re.sub('five', '5', st)
    st = re.sub('six', '6', st)
    st = re.sub('seven', '7', st)
    st = re.sub('eight', '8', st)
    st = re.sub('nine', '9', st)
    answer = st
    print(answer)
    return answer


testcast = "one4seveneight"
solution(testcast)
