'''"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
입력 : 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다.
문자열은 O와 X만으로 이루어져 있다.
출력 :
각 테스트 케이스마다 점수를 출력한다.
'''

# 또 똑같은 input_case 문제

input_case = int(input())

for _ in range(input_case):
    input_OX = input()
    score = 0
    continue_O = 0

    for OX in input_OX:
        if OX == 'O':
            continue_O += 1

        else:
            continue_O = 0

    score += continue_O

print(score)

# 틀렸습니다
# 그래그래 그럼그렇지 한번에 될 리가 없지
# 아 한줄마다 print 해야하는
# 아아아아아ㅏ아아아앙ㅇㅇ아ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅇㅇㅇㅇㅇㅇㅇ아ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅇㅇㅇㅇㅇㅇㅇ아ㅏㅏㅏㅏㅏㅏㅏ

input_case = int(input())

for _ in range(input_case):
    input_OX = input()
    score = 0
    continue_O = 0

    for OX in input_OX:
        if OX == 'O':
            continue_O += 1

        else:
            continue_O = 0

    score += continue_O

    print(score)

# 틀렸습니다
# 틀렸습니다
# 틀렸습니다
# 다시해서 가져오세요

input_case = int(input())

for _ in range(input_case):
    input_OX = input()
    score = 0
    continue_O = 0

    for OX in input_OX:
        if OX == 'O':
            continue_O += 1
            score += continue_O

        else:
            continue_O = 0

    print(score)


# 소요시간 : 25분
# 메모리 : 32412kb
# 시간 : 40ms
# 캇캇캇캇캇
# CLear.
# 위치를 잘 맞추자. 또 엉뚱한데 가있어서 안됐네;