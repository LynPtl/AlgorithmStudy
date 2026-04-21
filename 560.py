import sys
from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        count = defaultdict(int)
        count[0] = 1
        ans = 0
        s = 0

        for x in nums:
            s+=x
            ans += count[s-k]
            count[s] += 1

        return ans

def main():
    lines = sys.stdin.read().strip().split()
    nums = list(map(int,lines))
    k = nums[-1]
    nums = nums[:-1]
    sol = Solution()
    result = sol.subarraySum(nums, k)
    print(result)

if __name__ == "__main__":
    main()