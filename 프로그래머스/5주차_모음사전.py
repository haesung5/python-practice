# 문제 설명
# 사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다. 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.
#
# 단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# word의 길이는 1 이상 5 이하입니다.
# word는 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어져 있습니다.
# 입출력 예
# word	result
# "AAAAE"	6
# "AAAE"	10
# "I"	1563
# "EIO"	1189
# 입출력 예 설명
# 입출력 예 #1
#
# 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA", "AAA", "AAAA", "AAAAA", "AAAAE", ... 와 같습니다. "AAAAE"는 사전에서 6번째 단어입니다.
#
# 입출력 예 #2
#
# "AAAE"는 "A", "AA", "AAA", "AAAA", "AAAAA", "AAAAE", "AAAAI", "AAAAO", "AAAAU"의 다음인 10번째 단어입니다.
#
# 입출력 예 #3
#
# "I"는 1563번째 단어입니다.
#
# 입출력 예 #4
#
# "EIO"는 1189번째 단어입니다.


from itertools import product

def solution(word):
    answer = 0
    list_word = ['A', 'E', 'I', 'O', 'U']
    init_word = []

    # for i in list_word:
    #     init_word += [i]
    #     for j in list_word:
    #         init_word += [i+j]
    #         for k in list_word:
    #             init_word += [i+j+k]
    #             for l in list_word:
    #                 init_word += [i+j+k+l]
    #                 for m in list_word:
    #                     init_word += [i + j + k + l + m]

    init_word = sorted(["".join(str_word) for i in range(int(len(list_word))) for str_word in product(list_word, repeat=i+1)])

    print(init_word)
    answer = init_word.index(word) + 1

    return answer

print(solution('AAAE'))
#
# from itertools import product
#
# word = 'AAAE'
# list_word = 'AEIOU'
# solution = lambda word: sorted(["".join(c) for i in range(5) for c in product("AEIOU", repeat=i+1)]).index(word) + 1
#
# print(solution(word))
#
# init_word = sorted(["".join(c) for i in range(5) for c in product(list_word, repeat=i+1)])
#
# # print(init_word)
# test = ["".join(c) for c in product(list_word, repeat=2)]
# print(test)
#
# test1 = lambda c: [for c in product(list_word, repeat=2)]
# print(test1)
# print('-------------------------------------------')
# list_word = ['A','B']
# joiner = "".join(list_word)
# print(joiner)
