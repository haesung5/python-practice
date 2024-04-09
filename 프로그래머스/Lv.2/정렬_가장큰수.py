# https://school.programmers.co.kr/learn/courses/30/lessons/42746

# 문제 설명
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.


# 숫자를 문자열로 바꾸어 사전역순으로 정렬한 뒤 조합

def solution(numbers):
    answer = list(map(str, numbers))
    answer.sort(key=lambda x:x*3, reverse = True)
    answer = str(int(''.join(answer)))
    
    return answer

number = [6, 10, 2]
print(solution(number))
