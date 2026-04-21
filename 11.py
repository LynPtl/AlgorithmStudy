import sys

class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            ans = max(ans,area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans

def main():
    line = sys.stdin.read().strip().split()
    nums = list(map(int,line))

    sol = Solution()
    result = sol.maxArea(nums)

    print(result)

if __name__ == "__main__":
    main()