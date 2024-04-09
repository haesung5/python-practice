'''
이모티콘마다 할인율은 다를 수 있으며, 할인율은 10%, 20%, 30%, 40% 중 하나로 설정됩니다.
'''

from itertools import product

def solution(users, emoticons):
    answer = []
    discount_rate = [40, 30, 20, 10]
    discount_arr = product(discount_rate, repeat=len(emoticons))

    # 모든 할인율 case만큼 반복
    for dis_arr in discount_arr:
        # print(dis_arr)

        # 할인율 적용한 이모티콘 가격
        emoticons_price = [y * (100 - x) // 100 for x, y in zip(dis_arr, emoticons)]
        # print(emoticons_price)
        # 이모티콘 플러스 가입자수, 총 구매가격
        plus, total_price = 0, 0

        # 각 할인율의 이모티콘 가격의 합
        for user in users:
            # 개인별 구매 가격
            price = 0

            # 개인별 구매 유무
            for idx, i in enumerate(dis_arr):
                if i >= user[0]:
                    price += emoticons_price[idx]

            if price >= user[1]:
                plus += 1
            else:
                total_price += price

        answer.append([plus, total_price])
        # print(answer)

    answer.sort(key=lambda x: (-x[0], -x[1]))

    return answer[0]

# users = [[40, 10000], [25, 10000]]
# emoticons = [7000, 9000]
users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
print(solution(users, emoticons))
