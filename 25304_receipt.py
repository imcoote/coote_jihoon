sum = int(input())
mulgun_su = int(input())

total_sum = 0
multi = 0
i=0

for i in range(mulgun_su):
    a, b = map(int, input().split())
    multi = a * b
    total_sum += multi

if sum == total_sum:
    print('Yes')
else:
    print('No')

# for문 돌아가는 과정에 대해 더 자세히 학습
# 무지성 while문 남발 x
# 변수이름 a,b,c,d 알파벳놀이 하다간 나중에 후회함. 처음부터 똑바로(알아볼 수 있게) 적을것
# 소요시간 : 30분