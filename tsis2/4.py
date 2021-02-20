class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxx = i = now = 0
        for i in range(len(gain)):
            now += gain[i]
            maxx = max(maxx, now)
        return (maxx)
