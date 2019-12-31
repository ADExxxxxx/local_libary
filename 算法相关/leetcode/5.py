def dfs(results, result, level, s):
    pass

def isPailnd(s):
    temp = list(s)
    temp.reverse()
    temp = "".join(temp)
    return temp == s



if __name__ == '__main__':
    result = []
    results = []

    dfs(results ,result, 0, "bababa")