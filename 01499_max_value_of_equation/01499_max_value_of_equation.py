from typing import List

# FIRST IS most LEFT
# LAST IS most RIGHT
class Node:
    # val are in format y-x,x
    def __init__(self,left,right,val):
        self.right = right
        self.left = left
        self.val = val

class monoQueue:
    def __init__(self,k):
        self.k = k
        self.n = 0
    def add(self,node):
        ## basically we eat all smaller ones than current y-x, but we need to left atleast two points
        if self.n == 0:
            self.first = node
            self.last = node
            self.n = 1
            return
        
        self.last.right = node
        node.left = self.last
        self.last = node
        while self.n > 0 and self.last.left.val[0] < self.last.val[0]:
            self.last.left = self.last.left.left
            self.n -= 1
        
        if self.last.left != None:
            self.last.left.right = self.last
        else:
            self.first = self.last
        self.n += 1
        ## also we need to eat all left that has |x-curr_x| > k 
        while self.n > 1 and abs(self.first.val[1] - self.last.val[1]) > self.k:
            self.first = self.first.right
            self.n -= 1
    def prune(self,x):
        while self.n > 0 and abs(self.first.val[1] - x) > self.k:
            self.first = self.first.right
            if self.first:
                self.first.left = None
            self.n -= 1
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max = -float("inf")
        monQ = monoQueue(k)
        for x,point in enumerate(points[:-1]):
            monQ.add(Node(None,None,(point[1]-point[0],point[0])))
            monQ.prune(points[x+1][0])
            if monQ.n > 0:
                firstP = monQ.first.val
                y1 = firstP[0] + firstP[1]
                x1 = firstP[1]
                x2 = points[x+1][0]
                y2 = points[x+1][1]
                res = y1 + y2 + abs(x1-x2)
                if res > max:
                    max = res
        return max
#[-12, 18] and [-7, 12].
points = [[-19,-12],[-13,-18],[-12,18],[-11,-8],[-8,2],[-7,12],[-5,16],[-3,9],[1,-7],[5,-4],[6,-20],[10,4],[16,4],[19,-9],[20,19]]
k = 6
sol = Solution()

print(sol.findMaxValueOfEquation(points,k))