'''
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오(단, 대문자와 소문자를 구분하지 않는다.)
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''

input_word = input()

word = input_word.upper()

# def solution(array):
#     cnt = [0] * (max(array) + 1)
#
#     for i in array:
#         cnt[i] += 1
#
#     m = 0
#     for j in cnt:
#         if j == max(cnt):
#             m += 1
#
#     if m > 1:
#         return print('?')
#     else:
#         return cnt.index(max(cnt))

# 위 define 함수는 실패(사유 : 문자열에 적합하지 않음)

from collections import Counter


def modefinder(items):
    if not items:
        return '?'

    c = Counter(items)
    order = c.most_common()
    maximum = order[0][1]

    modes = []
    for item in order:
        if item[1] == maximum:
            modes.append(item[0])

    if len(modes) > 1:
        return '?'
    else:
        return modes[0]

result = modefinder(word)
print(result)

# upper() : 알파벳을 대문자로 변환
# lower() : 알파벳을 소문자로 변환
# 문자열의 최빈값을 구하는 방법을 몰라서 구글링(ㅠ)
# define 해놓은 함수를 긁어와서 수정
# define 함수에는 return이 있어야 마지막에 None이 출력되지 않음
# 소요시간 : 30분
# 메모리 : 36252kb
# 시간: 116ms
