# https://school.programmers.co.kr/learn/courses/30/lessons/92335

# 문제 설명
# 양의 정수 n이 주어집니다. 이 숫자를 k진수로 바꿨을 때, 변환된 수 안에 아래 조건에 맞는 소수(Prime number)가 몇 개인지 알아보려 합니다.

# 0P0처럼 소수 양쪽에 0이 있는 경우
# P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
# 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
# P처럼 소수 양쪽에 아무것도 없는 경우
# 단, P는 각 자릿수에 0을 포함하지 않는 소수입니다.
# 예를 들어, 101은 P가 될 수 없습니다.
# 예를 들어, 437674을 3진수로 바꾸면 211020101011입니다. 여기서 찾을 수 있는 조건에 맞는 소수는 왼쪽부터 순서대로 211, 2, 11이 있으며, 총 3개입니다. (211, 2, 11을 k진법으로 보았을 때가 아닌, 10진법으로 보았을 때 소수여야 한다는 점에 주의합니다.) 211은 P0 형태에서 찾을 수 있으며, 2는 0P0에서, 11은 0P에서 찾을 수 있습니다.

# 정수 n과 k가 매개변수로 주어집니다. n을 k진수로 바꿨을 때, 변환된 수 안에서 찾을 수 있는 위 조건에 맞는 소수의 개수를 return 하도록 solution 함수를 완성해 주세요.

import math
import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r]
    else :
        return convert(q, base) + tmp[r]

def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False

    return True

def solution(n, k):
    answer = 0

    #n을 k진수로 바꾸기
    convert_n = convert(n,k)
    print(convert_n)

    #변환된 숫자 0으로 나누면..
    zero_slipt = convert_n.split('0')
    print('zero_slipt : ', zero_slipt)
    zero_list = ' '.join(zero_slipt).split()
    print('zero_list : ', zero_list)

    # 나눈값이 소수인지 확인
    for i in zero_list:
        print('i : ', i)
        if int(i) > 1:
            result = is_prime_num(int(i))
            if result:
                answer += 1

    return answer



if __name__=='__main__':
    n = 437674
    k = 3

    print(solution(n,k))