class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = len(points)
        points.sort(key=lambda x:x[1])
        for i in range(1,len(points)):
            if points[i][0] <= points[i-1][1]:
                count-=1
                points[i][1]= points[i-1][1]
        return count