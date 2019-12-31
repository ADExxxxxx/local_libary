pos = 0
import copy
def display(chess):
    for i in range(len(chess)):
        for j in range(len(chess[i])):
            print(chess[i][j], end=" ")
        print()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Solution:

    @staticmethod
    def dfs(chess, point, flag):
        global pos
        orignal = copy.deepcopy(chess)
        while pos != len(point):
            # print("pos:", pos)
            for k in range(1, 10):
                # print("k:", k)
                if Solution.check(chess, point, k, pos, flag):
                    chess[point[pos].x][point[pos].y] = k
                    flag[pos].append(k)
                    break
            if chess[point[pos].x][point[pos].y] == 0:
                # print("yes")
                chess = copy.deepcopy(orignal)
                pos = pos - 1
                continue
            orignal = copy.deepcopy(chess)
            pos = pos + 1
        return

    @staticmethod
    def check(chess, point, k, pos, flag):
        # 一行中无相同
        for i in range(9):
            if chess[point[pos].x][i] == k:
                return False
        for i in range(9):
            if chess[i][point[pos].y] == k:
                return False

        for i in range(len(flag[pos])):
            if flag[pos][i] == k:
                return False
        for i in range((point[pos].x // 3) * 3, (point[pos].x // 3) * 3 +3):
            for j in range((point[pos].y // 3) * 3, (point[pos].y // 3) * 3 +3):
                if chess[i][j] == k:
                    return False
        return True

    @staticmethod
    def findEmpty(chess, point):
        for i in range(len(point)):
            if(chess[point[i].x][point[i].y]) == 0:
                return False
        return True



if __name__ == '__main__':
    point = [] # 记录当前填空的坐标点

    chess = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(9):
        m = input().split(" ")
        for j in range(9):
            chess[i][j] = int(m[j])
            if chess[i][j] == 0:
                point.append(Point(i, j))
    flag = [[0 for _ in range(1)] for _ in range(len(point))]
    Solution.dfs(chess, point, flag)
    display(chess)
