'''두 영어 단어가 철자의 순서를 뒤바꾸어 같아질 수 있을 때, 그러한 두 단어를 서로 애너그램 관계에 있다고 한다.
예를 들면 occurs 라는 영어 단어와 succor 는 서로 애너그램 관계에 있는데, occurs의 각 문자들의 순서를 잘 바꾸면 succor이 되기 때문이다.
한 편, dared와 bread는 서로 애너그램 관계에 있지 않다.
하지만 dared에서 맨 앞의 d를 제거하고, bread에서 제일 앞의 b를 제거하면, ared와 read라는 서로 애너그램 관계에 있는 단어가 남게 된다.
두 개의 영어 단어가 주어졌을 때, 두 단어가 서로 애너그램 관계에 있도록 만들기 위해서 제거해야 하는 최소 개수의 문자 수를 구하는 프로그램을 작성하시오.
문자를 제거할 때에는 아무 위치에 있는 문자든지 제거할 수 있다.
입력 : 첫째 줄과 둘째 줄에 영어 단어가 소문자로 주어진다. 각각의 길이는 1,000자를 넘지 않으며, 적어도 한 글자로 이루어진 단어가 주어진다.
출력 : 첫째 줄에 답을 출력한다.
'''

# 이건 또 무슨소릴까...

# 그니까 두줄 합해서 몇개을 지워야 문자들의 숫자들이 맞아떨어질까? 인가?
# 그럼 두개 합해서 공통인거 빼면 되는거 아님?
# 지렸다
# ㅅㄱ

first_input = input()
second_input = input()

same = 0
for i in first_input:
    if i in second_input:
        same += 1

print((len(first_input)-same) + (len(second_input)-same))

# 틀렸습니다
# 아 왜요

# GPT
# ❌ 코드의 문제점
# 중복 문자 문제
# 만약 first_input에 같은 문자가 여러 번 등장하면, same이 여러 번 증가하여 잘못된 결과가 나올 수 있음.
# 예를 들어, first_input = "aabb", second_input = "ab"이면 same이 4로 계산됨 → 잘못된 값 발생.

# 아?
# Counter를 쓰셔라?

from collections import Counter

first_input = input()
second_input = input()

first_count = Counter(first_input)
second_count = Counter(second_input)

same = len((first_count & second_count))

print(len(first_input) + len(second_input) - 2 * same)

# first_count & second_count : 두 Counter 객체의 교집합을 구하여 공통으로 등장하는 문자 개수
# ㅇㅋㅇㅋ 감사합니다

# 틀렸습니다
# 하....

# len(first_count & second_count) → 공통 문자의 개수가 아니라, 공통 문자 종류의 개수만 반환
# len이 아니라 sum을 쓰셔야 합니다. 라네요?

from collections import Counter

first_input = input()
second_input = input()

first_count = Counter(first_input)
second_count = Counter(second_input)

same = sum((first_count & second_count))

print(len(first_input) + len(second_input) - 2 * same)

# 뭔가 이상한데 아직도 제대로 안나오는데?
# 틀렸습니다
# sum()에서 해당 Counter들의 키값을 더해주기 때문에 .values()를 써서 밸류값을 더해야한다?

from collections import Counter

first_input = input()
second_input = input()

first_count = Counter(first_input)
second_count = Counter(second_input)

same = sum((first_count & second_count).values())

print(len(first_input) + len(second_input) - 2 * same)

# 맞았습니다

# 소요시간 : 30분
# 메모리 : 34900kb
# 시간 : 56ms
# ez
