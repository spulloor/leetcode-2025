class Solution:
    def candy(self, ratings: List[int]) -> int:
        candyCounts = [1] * len(ratings)

        # go through the ratings list from left to right and 
        # check if left child is less than current child 
        # if it is than the current child will get one more candy

        for i in range(1, len(ratings)):

            if ratings[i] > ratings[i - 1]:
                candyCounts[i] = candyCounts[i - 1] + 1

        # now go through the ratings array from right to left 
        # if current child is > the right child then the no. of candy 
        # to the current child needs to be atleast greater than the right child

        for i in range(len(ratings) - 2, -1, -1):

            if ratings[i] > ratings[i + 1]:
                candyCounts[i] = max(candyCounts[i], candyCounts[i + 1] + 1)

        
        return sum(candyCounts)