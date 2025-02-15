'''대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
입력 : 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다.
점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
출력 : 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다. 정답과 출력값의 절대/상대 오차는 10-3이하이면 정답이다.
'''

# 자 이게 무슨소릴까
# GPT선생의 문제 해설
# 평균을 넘는 학생들의 비율을 계산하여 출력하는 문제
# 평균이 전체의 몇% 인지만 구하면 된다라

input_case = int(input())

for _ in range(input_case):
    student_score = list(map(int, input().split()))
    student_su = student_score[0]
    scores = student_score[1:]

    avg_score = sum(scores) / student_su
    over_avg_student = len([score for score in scores if score > avg_score])
    percentage = (over_avg_student / student_su) * 100

    print(f"{percentage:.3f}%")

# 소요시간 : 30분
# 메모리 : 32412kb
# 시간 36ms

# input_case 문제를 너무 많이 접하다보니 이제는 술술 나옴
# 브론즈의 왕이 될 준비가 됐다