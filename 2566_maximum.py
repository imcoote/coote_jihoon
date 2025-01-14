"""9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.
입력 : 첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉 개씩 수가 주어진다. 주어지는 수는 100보다 작은 자연수 또는 0이다.
출력 : 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 위치한 행 번호와 열 번호를 빈칸을 사이에 두고 차례로 출력한다. 최댓값이 두 개 이상인 경우 그 중 한 곳의 위치를 출력한다."""

input_number = []

for _ in range(9):
    row = list(map(int, input().split()))
    input_number.append(row)


max_number = max(max(row) for row in input_number)

row_index, col_index = [(i + 1, row.index(max_number) + 1) for i, row in enumerate(input_number) if max_number in row][0]

print(max_number)
print(row_index, col_index)


# for _ in range(9): 9번 반복해서 각 행을 입력
# map(int, ...) : 입력된 숫자를 정수형으로 변환
# ? 뭐지 왜 성공임? (최댓값 두개면 한곳의 위치를 출력 -> 이거 안했는데?)
# 감사합니다 감사합니다 성공했습니다
# 소요시간 : 45분
# 메모리 : 32412kb
# 시간 : 32ms
