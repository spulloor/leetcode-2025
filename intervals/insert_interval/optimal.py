class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals

        intervals2 = []
        interval_inserted = False

        start_ni = newInterval[0]
        end_ni = newInterval[1]

        # step 1: insert the interval at the right position
        for interval in intervals:
            start_i = interval[0]
            end_i = interval[1]

            if start_i > start_ni and not interval_inserted:
                intervals2.append(newInterval)
                intervals2.append(interval)
                interval_inserted = True
            else:
                intervals2.append(interval)

        # if it is the last interval in the list of intervals
        if not interval_inserted:
            intervals2.append(newInterval)

        # step 2: merge the intervals if there is an overlapp
        # same algorithm from the previous problem
        merged_intervals = []
        for interval in intervals2:
            
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

        return merged_intervals


        