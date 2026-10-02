import math
#from typing import list
class Solution:
    @staticmethod
    def inDict(unit_diff,slope_dict):
        if (unit_diff) in slope_dict:
            slope_dict[unit_diff] += 1
        else:
            # add 2 for two points at beginning
            slope_dict[unit_diff] = 2
        return slope_dict[unit_diff]
    def maxPoints(self, points: list[list[int]]) -> int:
        # edge cases
        if len(points) <= 1:
            return(len(points))
        longestLine = 0
        # we do it in reverse order so that we can avoid double counting the same line
        for f_point in reversed(points):
            slope_dict = {}
            for s_point in points:
                if s_point == f_point:
                    continue
                # for each point we find the slope of the line between it and the first point, 
                # that slope will be the same for all points on the sane line
                diff = (f_point[0] - s_point[0],f_point[1] - s_point[1])
                if (diff[0] != 0):
                    diff = (diff[0]/diff[0],diff[1]/diff[0])
                else:
                    # this is special case where the line is vertical, we can just use a unit vector to represent it
                    diff = (0,1)
                longestLine = max(self.inDict(diff,slope_dict),longestLine)
            # remove last point from the list so that we don't double count it
            points.pop()
        return longestLine



solution = Solution()
#points = [[4,5],[4,-1],[4,0]]
print(solution.maxPoints(points))
#Output: 3

