'''0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다.
먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다.
그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.
26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.
위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.
입력 : 첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.
출력 : 첫째 줄에 N의 사이클 길이를 출력한다.
'''


input_number = int(input())
cycle = 0
if len(str(input_number)) == 1:
    input_number = int(str(input_number) + "0")

while True:
    mock = input_number // 10
    namerge = input_number % 10
    new_number_namerge = (mock + namerge) % 10
    number = (namerge * 10) + new_number_namerge
    cycle += 1
    if number == input_number:
        break

print(cycle)

# 시간초과...
# 아 왜..


input_number = int(input())
cycle = 0
n = input_number

if len(str(input_number)) == 1:
    input_number = int(str(input_number) + "0")

while True:
    mock = number // 10
    namerge = number % 10
    new_number_namerge = (mock + namerge) % 10
    number = (namerge * 10) + new_number_namerge
    cycle += 1

    if number == n:
        break

print(cycle)

# 시간초과
# 아 왜ㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐㅐ
# 왜 그러는데 왜

# 시간초과는 GPT센세에게 물어봐
# 작성하신 코드에서 "시간 초과"가 발생하는 이유는 반복문(while True)이 올바르게 종료 조건을 만족하지 못해 무한 루프에 빠지기 때문일 가능성이 큽니다
# 무한 루프 종료 조건:
# while True 반복문에서 종료 조건을 if number == n으로 설정하여, 생성된 숫자가 초기 입력값과 같아지면 반복문을 종료하도록 수정했습니다.
# 무한 루프 내에서 계속 계산할 값을 저장하는 변수를 number로 설정해 혼란을 줄이고 명확히 했습니다.
# 무한 루프 종료 조건이 명확히 설정되었으므로 무한 루프에 빠지는 일이 없어졌습니다.

# => 초기값을 설정을 안해줘서 종료조건을 만족 못해서 무한루프에서 break를 못걸었다? ㅇㅋ

input_number = int(input())
cycle = 0
n = input_number

if len(str(input_number)) == 1:
    input_number = int(str(input_number) + "0")

number = input_number

while True:
    mock = number // 10
    namerge = number % 10
    new_number_namerge = (mock + namerge) % 10
    number = (namerge * 10) + new_number_namerge
    cycle += 1

    if number == n:
        break

print(cycle)

# 틀렸습니다
# 미쳤...?
# 왜 그러는건데
# 뭐가 틀린건지 알려라도 주든가
# 으ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ
# 민관아.. 잘하자...


input_number = int(input())
cycle = 0
n = input_number

if len(str(input_number)) == 1:
    input_number = int("0" + str(input_number))

number = input_number

while True:
    mock = number // 10
    namerge = number % 10
    new_number_namerge = (mock + namerge) % 10
    number = (namerge * 10) + new_number_namerge
    cycle += 1

    if number == n:
        break

print(cycle)

# 아..
# 갈통이슈;;
# input_number = int(str(input_number) + "0") => input_number = int("0" + str(input_number))
# 한글을 잘 읽자.
# 민관아 미안하다

# 소요시간 : 40분
# 메모리 : 32412kb
# 시간 : 36ms

# 무한루프에 빠지지 않게 break 걸 때 조건을 잘 설정하기.