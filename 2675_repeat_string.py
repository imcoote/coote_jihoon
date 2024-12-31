case_su = int(input())

for i in range(case_su):
    ipruk = list(input().split())
    ipruk_su = int(ipruk[0])
    ipruk_string = list(ipruk[1])

    for i in range(len(ipruk[1])):
        for j in range(ipruk_su):
            print(ipruk_string[i], end="")
    print('')


# end=""의 역할에 대해 학습
# 출력의 형태가
# 2
# 3 ABC
# AAABBBCCC
# 5 ABC
# AAAAABBBBBCCCCC
# 이렇게 나옴. for문을 조금 더 만져서 입력이 다 끝난 후에 한번에 출력하게 하고 싶지만?
# 일단? 돌아가니까? 냅둬. 건드리지마.
# 소요시간 : 30분
# 메모리 : 32412kb
# 시간 : 32ms