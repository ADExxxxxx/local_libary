class Solution:

    def solve(self, nums, target):
        hashmap = {}
        for ind, num in enumerate(nums):
            #print("ind:", ind, "num:", num)
            if hashmap.get(target - num) is not None:
                result = [ind, hashmap.get(target - num)]
                result.reverse()
                return result
            hashmap[num] = ind




if __name__ == '__main__':
    a = Solution()
    i = a.solve([2,7,11,15], 9)
    print(i)