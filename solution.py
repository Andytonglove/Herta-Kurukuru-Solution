"""
黑塔转圈圈问题
1.有若干怪物的血量是正整数，怪物血量变为0时判定死亡。
2.玩家单次攻击可以对—个怪物造成一点伤害。
3.怪物生命值削减到最大生命值一半时会对所有怪物造成一点伤害。
给出一个算法，输入一个整形数组代表怪物的血量，求令所有怪物死亡的最少攻击次数。
测试用例：{1，1，1，1，5}, {1，6}, {5, 5, 5, 5, 5}
"""

import heapq


def minimum_normal_attack(nums):
    normal_attack_count = 0
    n = len(nums)

    enemies = [(hp, hp) for hp in nums]  # 每个元素为（当前血量，初始血量）

    aoe_count = 0  # 统计已经触发过AOE的次数

    for i in range(n):
        enemy = enemies[i]
        if (
            enemy[1] > n
        ):  # 如果敌人的初始血量大于n，这些超过n的血量值早晚要用普攻打，先进行这些普攻，有利于更早触发AOE
            normal_attack_count += enemy[1] - n
            enemies[i] = (n, n)  # 将当前血量设为n

            if n <= enemy[1] // 2:
                aoe_count += 1

    pq = []  # 使用一个最小堆来存储当前血量最接近初始值一半的敌人
    for enemy in enemies:
        if enemy[0] > enemy[1] // 2:
            heapq.heappush(pq, (enemy[0] - enemy[1] // 2, enemy))

    while pq:
        # 每次取出当前血量最接近初始值一半的敌人
        _, enemy_nearest_to_half = heapq.heappop(pq)

        # 考虑已经触发过的AOE能否把这个敌人的血量打到初始值一半以下，如果不能，就用普攻打到触发AOE为止
        if enemy_nearest_to_half[0] - aoe_count > enemy_nearest_to_half[1] // 2:
            normal_attack_count += (
                enemy_nearest_to_half[0] - enemy_nearest_to_half[1] // 2 - aoe_count
            )
        aoe_count += 1

        # 剩余多少血就不用管了，只要所有AOE都触发一遍，剩余的血量都会被打掉

    return normal_attack_count


# 测试用例
monsters1 = [1, 1, 1, 1, 5]
monsters2 = [1, 6]

print(
    "Minimum attacks to kill all monsters in test case 1:",
    minimum_normal_attack(monsters1),
)
print(
    "Minimum attacks to kill all monsters in test case 2:",
    minimum_normal_attack(monsters2),
)
