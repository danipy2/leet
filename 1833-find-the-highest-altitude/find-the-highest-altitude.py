class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(list(accumulate(gain,initial=0)))