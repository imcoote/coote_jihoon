'''
M과 N이 주어질 때 M이상 N이하의 자연수 중 완전제곱수인 것을 모두 골라 그 합을 구하고 그 중 최솟값을 찾는 프로그램을 작성하시오.
예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 완전제곱수는 64, 81, 100 이렇게 총 3개가 있으므로 그 합은 245가 되고 이 중 최솟값은 64가 된다.
M이상 N이하의 자연수 중 완전제곱수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다.
단, M이상 N이하의 자연수 중 완전제곱수가 없을 경우는 첫째 줄에 -1을 출력한다.
'''

first_input = int(input())
second_input = int(input())

M = 0
N = 0

if first_input > second_input :
    first_input = N
    second_input = M
else:
    first_input = M
    second_input = N

list = []
for i in range(M,N+1):
    for j in range(i+1):
        if i == j**2:
            list.append(i)

if len(list) == 0 :
    print(-1)
elif M==1 and N==1 :
    print('1')
    print('1')
else :
    print(sum(list))
    print(min(list))

# 처음 제출코드 => 오답
# first_input 과 second_input 중 큰 값을 N, 작은 값을 M 으로 만들고 싶었음
# 근데 안됨(왜요...?)

'---------------------------------------------------------------------------------------'


M = int(input())
N = int(input())

# M = 0
# N = 0
#
# if first_input > second_input :
#     first_input = N
#     second_input = M
# else:
#     first_input = M
#     second_input = N

list = []
for i in range(M,N+1):
    for j in range(i+1):
        if i == j**2:
            list.append(i)

if len(list) == 0 :
    print(-1)
elif M==1 and N==1 :
    print('1')
    print('1')
else :
    print(sum(list))
    print(min(list))

# 수정 후 제출코드 => 정답
# 그냥 작은값을 M으로 두고 처음에 작은값을 입력, 두번째에 큰 값을 입력하는것으로 둠
# ????? 왜 됨?(얼탱)
# 소요시간 : 15분
# 메모리 : 32412kb
# 시간 : 5244ms
