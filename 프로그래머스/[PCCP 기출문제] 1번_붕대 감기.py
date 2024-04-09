'''
마지막 공격시간까지 반복하며
공격받은 시간에 health 데미지만큼 차감,
공격받지 않은 시간마다 체크하여 체력 회복
공격받지 않은 연속 시간이 시전시간과 같을 시 추가 회복
'''

def solution(bandage, health, attacks):

    # 시전시간, 초당 회복량, 추가 회복량
    t, x, y = bandage

    # Max 체력량
    max_health = health
    # attack 배열 순서
    attack_order = 0
    # 연속 시전시간 체크
    continuous_time = 0

    # 몬스터의 마지막 공격시간까지 반복
    for i in range(1, attacks[-1][0]+1):
        # attack 시 그 데미지만큼 health 차감
        if attacks[attack_order][0] == i:
            health -= attacks[attack_order][1]

            # 체력 0될시 -1 return 하며 종료
            if health <= 0 :
                return -1

            # 체크할 attack 배열 순서 +1
            attack_order += 1
            # 연속 시전시간 초기화
            continuous_time = 0

        else:
            # 공격받지 않으면 초당 회복량으로 체력 회복
            # 단, 최대 체력을 넘을 수 없음
            if max_health > health:
                health += x

                if max_health < health:
                    health = max_health

            # 지속시간 체크
            continuous_time += 1

        if continuous_time == t:
            # 연속 시전시간 조건 충족시 체력 추가 회복

            if max_health > health:
                health += y

            # 연속 시전시간 초기화
            continuous_time = 0

        # 단, 최대 체력을 넘을 수 없음
        if max_health < health:
            health = max_health

    return health
