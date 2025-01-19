'''정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
명령은 총 다섯 가지이다.
- push X: 정수 X를 스택에 넣는 연산이다.
- pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- size: 스택에 들어있는 정수의 개수를 출력한다.
- empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
- top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력 : 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다.
둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다.
문제에 나와있지 않은 명령이 주어지는 경우는 없다.
출력 : 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
'''

list = []

def push(list,x):
    list.append(x)

# 스택 이니까? 맨 마지막에 온 녀석이 가장 위에있다? 가 되어야 한다? ㅇㅋ
def pop():
    check = len(list)
    if check == 0:
        return -1
    else:
        return list.pop()

# pop() : GPT 에게 물어봄
# list.pop() 동작:
    # 마지막 요소 접근:
        # 리스트의 마지막 요소는 인덱스 기반으로 접근합니다.
        # Python은 리스트의 길이를 추적하고 있으므로 마지막 요소의 인덱스는 len(list) - 1입니다.
    # 요소 제거:
        # 마지막 요소의 메모리 참조를 제거하여 더 이상 접근할 수 없도록 만듭니다.
    # 리스트 길이 업데이트:
        # 제거 후 리스트의 길이를 하나 줄여 내부적으로 관리합니다.
    # 반환:
        # 제거된 요소의 값을 반환합니다.

# => 뭔소리지..?


def size():
    return len(list)

def empty():
    if len(list) == 0:
        return 1
    else:
        return 0

def top():
    check = len(list)
    if check == 0:
        return -1
    else:
        return list[-1]

cycle = int(input())
for i in range(cycle):
    input_word = input().split(' ')

    if input_word[0] == 'push':
        push(list,int(input_word[1]))
    elif input_word[0] == 'pop':
        print(pop())
    elif input_word[0] == 'size':
        print(size())
    elif input_word[0] == 'empty':
        print(empty())
    elif input_word[0] == 'top':
        print(top())

# 소요시간 : 30분
# 결과 : 시간초과 (?)
# 왜요..?
# ------------------------------------------------------------------------------

# GPT 코드
# 시간 초과가 발생하는 이유는 list라는 이름으로 정의된 전역 변수를 직접 수정하면서 스택 연산을 수행하고 있기 때문입니다.
# Python의 전역 변수는 함수 호출 시 매번 접근 및 수정하는 데 비용이 들 수 있습니다.
# 따라서 전역 변수 사용을 줄이고, 입력과 출력 처리를 최적화해야 합니다
# ...?

import sys

# 스택을 저장할 리스트
stack = []

# 스택 명령 구현
def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    return 1 if len(stack) == 0 else 0

def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[-1]

# 입력과 출력 최적화
input = sys.stdin.read  # 입력을 한 번에 받음
data = input().strip().split('\n')  # 개행 문자로 분리

# 첫 줄은 명령의 개수
cycle = int(data[0])

# 결과를 저장할 리스트
results = []

# 명령 처리
for i in range(1, cycle + 1):
    command = data[i].split()

    if command[0] == 'push':
        push(int(command[1]))
    elif command[0] == 'pop':
        results.append(pop())
    elif command[0] == 'size':
        results.append(size())
    elif command[0] == 'empty':
        results.append(empty())
    elif command[0] == 'top':
        results.append(top())

# 결과를 한 번에 출력
# sys.stdout.write('\n'.join(map(str, results)) + '\n')

# sys.stdin.read로 입력 최적화:
# 한 번에 모든 입력을 읽어 리스트로 처리하여 반복적인 input() 호출을 줄임.

# 전역 변수 대신 로컬 변수 사용:
# stack은 명령 처리에만 사용되는 로컬 변수로 선언.

# 결과 리스트 사용:
# 모든 결과를 리스트에 저장하고 마지막에 한꺼번에 출력.

# sys.stdout.write로 출력 최적화:
# 출력도 한 번에 처리하여 반복적인 print() 호출을 줄임.

# ???
# 솔직히 이해 안됨.
# 하지만 나중에 다른 문제 풀 때도 이런 시간초과같은 런타임 문제가 나올테니 외워놓고 이해하기로 함.