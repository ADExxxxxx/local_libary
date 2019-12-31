class Solution:
   @staticmethod
   def dfs(results, path, level, capacity):
      if level > 100:
         return

      if path[level-1][0] == 5 and path[level-1][1] == 5:
         results.append(path)
         return

      else:
         for i in range(3):
            for j in range(3):
               if Solution.isVisiuable(path, level, capacity, i, j):
                  Solution.dfs(results, path, level+1, capacity)

   @staticmethod
   def isVisiuable(path, level, capacity, i, j):
      if len(results) > 0:
         return False
      if path[level - 1][i] <= 0:
         return False
      elif path[level - 1][j] >= capacity[j]:
         return False
      elif i == j:
         return False

      else:
         Solution.pourOil(path, level, capacity, i, j)
         for temp in range(level):
            if path[temp] == path[level]:
               path.pop()
               level = level-1
               return False
         return True
   @staticmethod
   def pourOil(path, level, cacpcity, i, j):
      temp = path[level-1].copy()
      if temp[i] > capacity[j] - temp[j]:
         temp[i] = temp[i] - (cacpcity[j] - temp[j])
         temp[j] = capacity[j]
      else:
         temp[j] = temp[j] + temp[i]
         temp[i] = 0
      path.append(temp)

if __name__ == "__main__":
   path = [[10, 0, 0]] # 记录每一次倒油时三桶油的油量
   results = [] # 记录所有的解
   capacity = [10, 7, 3]
   Solution.dfs(results, path, 1, capacity)
   print(path)
