import sys
class Solution:
    def longestConsecutive(self, nums):
        s = set(nums)
        ans = 0
        for x in s:
            if x-1 in s:
                continue
            
            y = x+1
            while y in s:
                y += 1
            ans = max(ans,y-x)
        
        return ans

def main():
    line = sys.stdin.read().strip().split()
    nums = list(map(int,line))

    sol = Solution()
    result = sol.longestConsecutive(nums)
    print(result)

if __name__ == "__main__":
    main()