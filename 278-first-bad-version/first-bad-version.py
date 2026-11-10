# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lower_bound = 1
        upper_bound = n

        while lower_bound <= upper_bound:
            midpoint = (upper_bound + lower_bound) // 2
            
            if isBadVersion(midpoint) == False:
                lower_bound = midpoint + 1
            else:
                upper_bound = midpoint - 1
        return lower_bound