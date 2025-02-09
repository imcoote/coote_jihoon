'''상근이는 매일 아침 영자 신문을 학교에 가져와서 읽는다. 하지만, 상근이의 눈은 점점 나빠졌고, 더 이상 아침 신문을 읽을 수 없는 상황에 이르렀다.
상근이는 스캐너를 이용해서 글자를 확대한 다음에 보려고 한다.
신문 기사는 글자로 이루어진 R*C 행렬로 나타낼 수 있다. 글자는 알파벳과 숫자, 그리고 마침표로 이루어져 있다.
스캐너는 ZR과 ZC를 입력으로 받는다. 이렇게 되면, 스캐너는 1*1크기였던 각 문자를 ZR*ZC크기로 확대해서 출력해 준다.
신문 기사와 ZR, ZC가 주어졌을 때, 스캐너의 스캔을 거친 결과를 구하는 프로그램을 작성하시오.
입력 : 첫째 줄에 R, C, ZR, ZC가 주어진다. R과 C는 1과 50 사이의 정수이고, ZR과 ZC는 1과 5 사이의 정수이다.
다음 R개 줄에는 신문 기사가 주어진다.
출력 : 스캐너에 스캔된 결과를 총 R*ZR개 줄에 걸쳐서 C*ZC개 문자씩 출력한다.
'''

# 문제만 봐도 어질어질하다
# 민관아.. 잘하자...

R, C, ZR, ZC = map(int, input().split())
# R, C, ZR, ZC 나왔고
# R행 C열 받아야하니까
input_rows = []

# 2차원 배열을 이해하면 쉽게 풀 수 있다.
# 신문 기사의 글자를 리스트로 저장하여
# ZC의 수만큼 사용하여 해당 글자들을 곱해준 뒤
# ZR의 수만큼 늘려주면 된다.
# 완벽히 이해했어

for _ in range(R):
    input_rows.append(input())

for i in range(R):
    letters = []
    for j in range(C):
        letters.append(input_rows[i][j] * ZC)

print(letters)

# 음 그래그래 틀렸고~
# 왜일까~ 뭐가 틀렸을까~
# 이제는 시간초과만 아니여도 마음이 놓임


R, C, ZR, ZC = map(int, input().split())
input_rows = []
# 인풋로우는 있고 따로 정답 출력할 뭥가뭥가가 필요하다(?)(아마도)
scanner = []

for _ in range(R):
    input_rows.append(input())

for i in range(R):
    letters = []
    for j in range(C):
        letters.append(input_rows[i][j] * ZC)
    # 스캐너 안에 넣으려니까 갑자기 두통이 옴
    for _ in range(ZR):
        scanner.append(letters)

print(scanner)

# 컴파일에러



R, C, ZR, ZC = map(int, input().split())
input_rows = []
scanner = []

for _ in range(R):
    input_rows.append(input())

for i in range(R):
    letters = []
    for j in range(C):
        letters.append(input_rows[i][j] * ZC)
    for _ in range(ZR):
        scanner.append(letters)

for j in scanner:
    for _ in range(ZR):
        print(scanner)

# 출력 초과
# ? 초과는 또 뭐임(얼탱)


R, C, ZR, ZC = map(int, input().split())
input_rows = []
scanner = []

for _ in range(R):
    input_rows.append(input())

for i in range(R):
    letters = []
    for j in range(C):
        letters.append(input_rows[i][j] * ZC)
    for _ in range(ZR):
        scanner.append(letters)

for j in scanner:
    for _ in range(ZR):
        print(j)

# 출력 초과

# GPT 선생님
# letters 리스트가 이중 리스트 형태:
# scanner에 추가된 letters는 이중 리스트로 저장됩니다. 이로 인해 출력 시 중첩된 반복이 발생할 수 있습니다.
# 리스트에 리스트를 쓰지 말라고 하시는건가?
# 어케하는데요??


R, C, ZR, ZC = map(int, input().split())
input_rows = []
scanner = []

for _ in range(R):
    input_rows.append(input())

for i in range(R):
    letters = ''
    for j in range(C):
        letters += input_rows[i][j] * ZC
    for _ in range(ZR):
        scanner.append(letters)

for j in scanner:
    for _ in range(ZR):
        print(j)

# 출력 초과
# 크아아아아아아아아아아아ㅏ아아아아아아아아악

# GPT 선생님
# 작성하신 코드에서 출력 초과가 발생하는 이유는 마지막 출력 반복 부분에서
# for j in scanner 내부에 다시 for _ in range(ZR) 반복이 추가되어 불필요한 중복 출력이 발생하기 때문입니다

# 아 한번만 해도 돼요?

R, C, ZR, ZC = map(int, input().split())
input_rows = []
scanner = []

for _ in range(R):
    input_rows.append(input())

for i in range(R):
    letters = ''
    for j in range(C):
        letters += input_rows[i][j] * ZC
    for _ in range(ZR):
        scanner.append(letters)

for j in scanner:
        print(j)

# 맞았습니다!
# 소요시간 : 1시간
# 메모리 : 32412kb
# 시간 : 36ms

# 민관아 잘하자

# 조현준 :
# num = ''.join() 머 이런거
# # mul, 곱이 되는 가로줄
#     # join 메서드 : 각 문자열에 포함된 각 문자를 지정한 횟수만큼 반복한 새로운 문자열 생성
#     # '' 은 구분자, '_' 이면 a_b_c 이런식으로 붙음
#     mul = ''.join(char*zc for char in article[line])
#                 #  article[line]의 각 문자를 zc 번 반복한 결과를 리스트로 만든 뒤 하나로 합침
# join써야하더라
# 안쓰면 진짜 어렵던데

# 왜 이제 알려주는건데

R, C, ZR, ZC = map(int, input().split())
input_rows = []
scanner = []

for _ in range(R):
    input_rows.append(input())

for i in range(R):
    letters = ''.join([input_rows[i][j] * ZC
                       for j in range(C)])
    for _ in range(ZR):
        scanner.append(letters)

for j in scanner:
    print(j)

# 메모리 : 32412kb
# 시간 : 40ms
# 잘 된것만 남겨둔 건 비밀.