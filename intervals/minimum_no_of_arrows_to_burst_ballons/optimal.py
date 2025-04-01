class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort the points with x start co-ordinate
        points.sort(key=lambda x: x[1])

        # min 1 arrow will be thrown
        arrows = 1
        end = points[0][1]

        for point in points[1:]:
            # there are no overlapping ballons
            if point[0] > end:
                arrows += 1
                end = point[1]

        return arrows


