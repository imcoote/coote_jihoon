'''두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
입력 : 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다
출력 : 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
'''

# 구글링 하다보니 math함수에 최대공약수랑 최소공배수가 있네요?
# 바로갑니다

import math

first_number, second_number = map(int, input().split())

gcd = math.gcd(first_number, second_number)

lcm = (first_number * second_number) // gcd

print(gcd)
print(lcm)

# 틀렸습니다
# 왜요

# 아 제출을 잘못함;
# 맞았습니다

# 소요시간 : 8분
# 메모리 : 34536kb
# 메모리: 44ms
# ez