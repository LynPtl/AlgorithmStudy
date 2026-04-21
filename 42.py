import sys

class Solution:
    def trap(self, height):
        left = 0
        right = len(height) - 1

        pre = suf = 0
        ans = 0
        while left < right:
            pre = max(pre,height[left])
            suf = max(suf,height[right])

            if pre < suf:
                ans += pre - height[left]
                left += 1
            else:
                ans += suf - height[right]
                right -=1
        return ans

def main():
    line = sys.stdin.read().strip().split(',')
    nums = list(map(int,line))

    sol = Solution()
    result = sol.trap(nums)
    print(result)

if __name__ == "__main__":
    main()