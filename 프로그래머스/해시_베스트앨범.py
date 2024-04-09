# 베스트앨범
# 문제 설명
# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
#
# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.
#
# 제한사항
# genres[i]는 고유번호가 i인 노래의 장르입니다.
# plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
# genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
# 장르 종류는 100개 미만입니다.
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
# 모든 장르는 재생된 횟수가 다릅니다.
# 입출력 예
# genres	plays	return
# ["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]
# 입출력 예 설명
# classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.
#
# 고유 번호 3: 800회 재생
# 고유 번호 0: 500회 재생
# 고유 번호 2: 150회 재생
# pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.
#
# 고유 번호 4: 2,500회 재생
# 고유 번호 1: 600회 재생
# 따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.
#
# ※ 공지 - 2019년 2월 28일 테스트케이스가 추가되었습니다.

def solution(genres, plays):
    answer = []

    # genres dictionary 선언
    song_dic = {genres_item : 0 for genres_item in genres}

    # genres, plays list 선언
    song_list = list(zip(genres, plays))
    song_list.sort()

    # 더 많이 들은 genres 구하기
    for k in range(0, len(genres)):
        song_dic[song_list[k][0]] += song_list[k][1]

    # 많이 들은 순서로 정렬
    song_dic = dict(sorted(song_dic.items(), key=lambda x: x[1], reverse=True))

    # 장르별 많이들은 2곡 선정
    temp = []
    for k in song_dic.items():
        temp = []
        for l in range(len(genres)):
            if k[0] == genres[l]:
                temp.append((l, plays[l]))
        # 들은 횟수로 정렬
        temp.sort(key=lambda x: -x[1])
        # 많이 들은 2위까지 선정
        answer.append(temp[0][0])
        # 장르별 곡이 1곡일 떄
        if len(temp) >= 2:
            answer.append(temp[1][0])

    return answer


import collections

# def solution(genres, plays):
#     answer = []
#
#     # 1
#     sumOfGenres = collections.defaultdict(int)  # 장르별 총 재생 횟수
#     playsListDict = collections.defaulttemdict(list)  # 장르별로 나눠서 재생횟수와 인덱스 리스트로 저장
#
#     # 2
#     for i, genre, play in zip(range(len(genres)), genres, plays):
#         sumOfGenres[genre] += play
#         playsListDict[genre].append([i, play])  # 장르(키)의 밸류에 리스트를 계속 추가함: [인덱스, 재생횟수] 형태
#
#     # 3
#     items = sorted(sumOfGenres.items(), key=lambda x: x[1], reverse=True)  # 밸류기준 내림차순 정렬
#
#     # 4
#     for key, val in items:
#         # 4-1
#         # 해당 장르의 (인덱스, 재생횟수)를 재생횟수 기준 정렬
#         playTimes = sorted(playsListDict[key], key=lambda x: x[1], reverse=True)
#         # 4-2
#         for idx, play in playTimes[:2]:
#             answer.append(idx)
#
#     return answer


if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "classic"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres,plays))
