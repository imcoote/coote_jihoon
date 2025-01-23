'''에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾는 유명한 알고리즘이다.

이 알고리즘은 다음과 같다.
2부터 N까지 모든 정수를 적는다.
    1. 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
    2. P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
    3. 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.
    4. N, K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램을 작성하시오.
입력 : 첫째 줄에 N과 K가 주어진다. (1 ≤ K < N, max(1, K) < N ≤ 1000)
출력 : 첫째 줄에 K번째 지워진 수를 출력한다.
'''

n, k = map(int, input().split())

eratos = [i for i in range(2, n+1)]

delete_nums = []
while eratos:
    delete_num = eratos.pop(0)
    # pop() : 꺼내기 -> 저번에 썻던거 끌어다 써버리기
    delete_nums.append(delete_num)
    # eratos에서 꺼내서 delete_num에 추가

    multi_num = delete_num
    while multi_num <= n:
        if multi_num in eratos:
            eratos.remove(multi_num)
            delete_nums.append(multi_num)
            # 여기서도 pop 썻다가 안돌아가서 빠꾸
            # 건실하게 살자. 항상 겸손해라.
        multi_num += delete_num

print(delete_nums[k-1])

# 소요시간 : 25분
# 메모리 : 32412kb
# 시간 : 40ms
# 문제가 좀 복잡해서 구현과정에서 살짝 머리가 아팠음