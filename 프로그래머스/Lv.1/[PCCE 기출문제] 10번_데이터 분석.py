# https://school.programmers.co.kr/learn/courses/30/lessons/250121

def solution(data, ext, val_ext, sort_by):
    answer = [[]]

    # code, date, maximum, remain
    data_index = ['code', 'date', 'maximum', 'remain']
    print(data_index.index("date"))

    # data에서 ext 값이 val_ext보다 작은 데이터만
    for i in data:
        print(i)
        if i[data_index.index(ext)] < val_ext:
            answer.append(i)

    # 빈 배열 제거
    answer = list(filter(None, answer))
    # sort_by에 해당하는 값을 기준으로 오름차순 정렬
    answer.sort(key = lambda x:x[data_index.index(sort_by)])

    print(answer)

    return answer


data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501
sort_by = "remain"
result = [[3,20300401,10,8],[1,20300104,100,80]]

print(solution(data, ext, val_ext, sort_by))