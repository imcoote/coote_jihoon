# # 풀이
number_su = int(input())
number = list(map(int, input().rstrip()))
sum = sum(number)
if number_su == len(number):
        print(sum)
else:
    print('올바르지 않은 입력')


# GPT 도움 => 예외처리 포함 풀이
while True:
    try:
        number_su = int(input())  # 정수 입력
        number = list(map(int, input().rstrip()))  # 정수 리스트 입력
        if number_su != len(number):  # 숫자 개수 확인
            print("올바르지 않은 입력: 숫자의 개수가 맞지 않습니다.")
            continue
        print(sum(number))  # 합 출력
        break
    except ValueError:  # 정수가 아닌 값 입력 시 예외 처리
        print("올바르지 않은 입력: 정수를 입력해야 합니다.")
        continue

# 공백이 있는 숫자 입력 시 map(int, input().split())
# 공백이 없는 숫자 입력 시 map(int, input().rstrip()) / rstrip() : 문자열의 오른쪽 끝에 있는 공백이나 개행 문자를 제거
# list 요소가 모두 숫자형일 때 sum(list) => 리스트 내 요소의 합
# while 문에서 continue를 만났을 때 while 문 처음으로 올라간다
# 들여쓰기(인덴트)의 위치가 상당히 중요하다. 같은 라인에 있는게 전체 코드에 큰 영향을 준다
# 소요시간 : 15분