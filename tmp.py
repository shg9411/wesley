'''
각 집마다 제한시간과 그 시간 안에 가면 받을 수 있는 팁이 2차원 리스트에 존재,
총 제한시간이 주어지고 한 칸 이동시마다 1초 소요
최대로 팁을 받을 수 있는 경우에 팁을 출력
'''

# 문제를 풀 방법이 생각나지 않아서 가중치 작업 알고리즘 글을 보면서 시도했지만 시간안에 풀지 못함
# 솔직히 너무 어려웠음


def solution(r, delivery):
    # 선택 한번 했으면 다시 탐색하는 경우가 없게 하려고 함
    selected = [[False for _ in range(r)] for _ in range(r)]
    time = [[0 for _ in range(r)] for _ in range(r)]
    tip = [[0 for _ in range(r)] for _ in range(r)]

    now = 0
    maxTime = 0
    answer = 0

    for i in range(r**2):
        time[i//r][i % r] = delivery[i][0]
        maxTime = max(maxTime, delivery[i][0])
        tip[i//r][i % r] = delivery[i][1]

    def possible(x, y):
        if now == time[x][y]:
            return False
        return True

    def dfs(x, y, now, answer):
        selected[x][y] = True
        now += 1

    dfs(0, 0)
    return answer


delivery = [[1, 10], [8, 1], [8, 1], [3, 100], [8, 1], [8, 1], [8, 1], [
    8, 1], [8, 1], [8, 1], [8, 1], [8, 1], [9, 100], [8, 1], [8, 1], [8, 1]]
print(solution(4, delivery))
