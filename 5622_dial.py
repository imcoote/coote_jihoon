'''전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

입력 : 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.

출력 : 첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.'''

dictionary = {1: ('A', 'B', 'C'), 2: ('D', 'E', 'F'), 3 : ('G', 'H', 'I'), 4 : ('J', 'K', 'L'),
              5 : ('N', 'M', 'O'), 6 : ('P', 'Q', 'R', 'S'), 7 : ('T', 'U', 'V'), 8 : ('W', 'X', 'Y', 'Z')}

alphabet = []
input_alphabet = input()
for char in input_alphabet:
    alphabet.append(char)

# input_alphabet = input()
# result = list(input_alphabet) 이렇게도 가능함. 전지전능하신 GPT시여..

# 이 밑으로는 --------- 까지 감도 안잡혀서 GPT의 도움을 받음

count_alphabet = 0
for char in alphabet:
    for key, value in dictionary.items():
        if char in value:
            count_alphabet += key
            break

# --------------------

count_second = count_alphabet + (len(alphabet) *2)
print(count_second)

# 처음 딕셔너리를 구성할 때
# 리스트[]: 수정 가능
# 튜플(): 수정 불가능
# for key, value in dictionary.items() => dictionary 안에서 key와 value값을 꺼내와 char에 저장
# if char in value => char가 value값 안에 포함되어 있으면
# count_alphabet += key => key값을 계속 더함

# 소요시간 : 30분
# 메모리 : 32412kb
# 시간 : 36ms