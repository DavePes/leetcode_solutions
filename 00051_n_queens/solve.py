class Solution:
    def setTrue(self,h,v,j, vertical_d, diagonal, vertical_list):
        vertical_d[v] = True
        diagonal["diff"][h-v] = True
        diagonal["sum"][h+v] = True
        # just to make it constant time
        vertical_list[j], vertical_list[-1] = vertical_list[-1], vertical_list[j]
        vertical_list.pop()
    
    def recurse(self,x,horizontal_d, vertical_d, diagonal, vertical_list,n):
        if x == 0:
            return 1
        total = 0
        h = n - x 
        for j, v in enumerate(vertical_list):
            if vertical_d[v] == False:
                diff = h - v
                sum = h + v
                if diagonal["diff"][diff] == False:
                    if diagonal["sum"][sum] == False:
                        self.setTrue(h,v,j, vertical_d, diagonal, vertical_list)
                        total += self.recurse(x-1,horizontal_d, vertical_d, diagonal, vertical_list,n)
                        vertical_list.append(v)
                        # do swaps
                        vertical_list[j], vertical_list[-1] = vertical_list[-1], vertical_list[j]
                        diagonal["diff"][diff] = False
                        diagonal["sum"][sum] = False
                        horizontal_d[h] = False
                        vertical_d[v] = False
        return total



    def totalNQueens(self, n: int) -> int:
        horizontal_d = {x:False for x in range(n)} # this means that for example horizontal_d[0] = False means that the horizontal line 0 is not occupied by a queen
        vertical_d = {x:False for x in range(n)}
        vertical_list = [x for x in range(n)]
        leftB = 1 - n
        rightB = n*2
        diagonal_diff = {x:False for x in range(leftB,rightB,1)}
        diagonal_summ = {x:False for x in range(leftB,rightB,1)}
        diagonal = {
            "diff": diagonal_diff,
            "sum": diagonal_summ
        }
        return self.recurse(n, horizontal_d, vertical_d, diagonal, vertical_list,n)
    

A = Solution()
print(A.totalNQueens(8))