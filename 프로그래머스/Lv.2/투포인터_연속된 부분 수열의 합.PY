# https://school.programmers.co.kr/learn/courses/30/lessons/178870

# 참고 : https://unie2.tistory.com/312
#        https://konkukcodekat.tistory.com/83

# 비내림차순으로 정렬된 수열이 주어질 때, 다음 조건을 만족하는 부분 수열을 찾으려고 합니다.

# 기존 수열에서 임의의 두 인덱스의 원소와 그 사이의 원소를 모두 포함하는 부분 수열이어야 합니다.
# 부분 수열의 합은 k입니다.
# 합이 k인 부분 수열이 여러 개인 경우 길이가 짧은 수열을 찾습니다.
# 길이가 짧은 수열이 여러 개인 경우 앞쪽(시작 인덱스가 작은)에 나오는 수열을 찾습니다.
# 수열을 나타내는 정수 배열 sequence와 부분 수열의 합을 나타내는 정수 k가 매개변수로 주어질 때, 위 조건을 만족하는 부분 수열의 시작 인덱스와 마지막 인덱스를 배열에 담아 return 하는 solution 함수를 완성해주세요. 이때 수열의 인덱스는 0부터 시작합니다.

def solution(sequence, k):
    answer = []
    
    length = len(sequence)
    sum, end = 0, 0
    
    # 
    for start in range(length):
        while sum < k and end < length:
            sum += sequence[end]
            end += 1

        
        if sum == k:
            answer.append([start, end-1])
        sum -= sequence[start]

    answer.sort(key=lambda x:(x[1]-x[0], x[0]))
    
    return answer[0]


# 다른 사람 답
# def solution(sequence, k):
#     answer = []
    
#     length = len(sequence)
#     start, end, sum = 0, 0, 0

#     # sum = sequence[0]
    
#     while start <= length:
#         sum += sequence[start]
#         if start == k:
#             answer.append([i, i+count, count])
            
# 2중 for문 -> 시간 초과
# def solution(sequence, k):
#     # for i in range(length):
#     #     count, sum = 0, 0
        
#     #     sum += sequence[i]
#     #     if sum == k:
#     #         answer.append([i, i+count, count])
#     #         continue
#     #     elif sum > k or i > k:
#     #         continue
        
#     #     for j in range(i+1, length):
#     #         count += 1
#     #         sum += sequence[j]
#     #         if sum == k:
#     #             answer.append([i, i+count, count])
#     #             break
#     #         elif sum > k:
#     #             break
    
#     answer.sort(key=lambda x:(x[2], x[0]))
    
#     return answer[0][0],answer[0][1]



sequence = [2, 2, 2, 2, 2]
k = 6
print(solution(sequence, k))