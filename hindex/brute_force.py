class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = prev_h = 0
        n = len(citations)

        while h <= n:
            num_papers = 0

            for c in citations:

                if c >= h:
                    num_papers += 1

            if num_papers >= h:
                prev_h = h
            else:
                break

            h += 1

        return prev_h
