class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        curr = sum(cardPoints[:k])
        ans = curr
        for i in range(k):
            curr -= cardPoints[k - 1 - i]
            curr += cardPoints[n - 1 - i]
            ans = max(ans, curr)

        return ans