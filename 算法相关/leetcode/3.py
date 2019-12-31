def lengthOfLongestSubstring(s):
    ss = []
    length = 0
    max_length = 0
    for i in range(len(s)):
        if s[i] in ss:
            pos = ss.index(s[i])
            # print(pos)
            length = length - pos - 1
            ss = ss[pos + 1:]
        ss.append(s[i])
        length = length + 1
        if length > max_length:
            max_length = length
    if length > max_length:
        return length
    return max_length


i = lengthOfLongestSubstring("asjrgapa")
print(i)