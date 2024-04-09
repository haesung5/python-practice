# https://school.programmers.co.kr/learn/courses/30/lessons/258712

import math

def solution(friends, gifts):
    # 1,2 <-> 2,1
    # 주고 받은 선물 list
    give = [[0] * len(friends) for _ in range(len(friends))]
    # print(give)
    # 선물지수
    give_point = [0] * len(friends)
    answer = [0] * len(friends)

    # print(give_point)

    # 주고 받은 선물
    for gift in gifts:
        gift = gift.split(' ')
        # print(gift)
        # print(friends.index(gift[0]))
        give[friends.index(gift[0])][friends.index(gift[1])] += 1

    # 선물 지수 계산
    for index in range(len(friends)):
        # print(index)
        take_point = list(zip(*give))[index]
        give_point[index] = sum(give[index]) - sum(take_point)

    # print(give_point)


    # 선물 주기
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            if i == j : continue

            a, b = give[i][j], give[j][i]
            if a > b:
                answer[i] += 1
            elif a < b:
                answer[j] += 1
            else:
                if give_point[i] > give_point[j]:
                    answer[i] += 1
                elif give_point[i] < give_point[j]:
                    answer[j] += 1
                else:
                    continue

    # print(max(answer))


    return max(answer)

friends = ["a", "b", "c"]
gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]
print(solution(friends, gifts))
