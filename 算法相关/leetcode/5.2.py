max_length = 1

def isPailnd(s):
    temp = list(s)
    temp.reverse()
    temp = "".join(temp)
    return temp == s

def findMax(s):
    global max_length
    mid = len(s) // 2

    if isPailnd(s[mid-1:mid+1]):
        for i in range(2, len(s)):
           findMax(s[mid-i: mid+i])



