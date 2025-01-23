'''땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.
달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.
입력 : 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)
출력 : 첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.
'''

# 쉽다

A, B, V = map(int, input().split())
cnt = 0
hight = 0
while True:
    for i in range(V):
        cnt += 1
        hight += A
        if hight >= V:
                print(cnt-1)
                break
        else :
            hight -= B

# 어렵다
# 너무 어렵게 생각하지 말자

A, B, V = map(int, input().split())
days = V // (A - B)
print(days)

# easy
# 틀렸습니다
# hard
# 어렵게 생각하자

A, B, V = map(int, input().split())
days = (V - B) // (A - B) + 1
print(days)

# 틀렸습니다
# 틀렸습니다
# 틀렸습니다
# 틀렸습니다
# 틀렸습니다
# 유연하게 생각하자

A, B, V = map(int, input().split())
days = (V - B) // (A - B) + 1
print(days)

# 틀렸습니다

A, B, V = map(int, input().split())
days = ((V - B - 1) // (A - B)) + 1
print(days)

# 맞았습니다!
# 소요시간 : 15분
# 메모리 : 32412kb
# 시간 : 36ms
# V에서 B를 빼고 1을 한번 더 빼줘야 바로 올림돼지 않아 마지막에 올림 될 +1과 충돌이 없지 않을까
# 설명을 잘 못하겠다
# 아무튼 돌아갑니다 ^~^b