import sys

def main():
    line = sys.stdin.read().strip().split()
    nums = list(map(int,line))
    sol = Solution()
    result = sol.threeSum(nums)
    print(result)


class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n-2):
            x = nums[i]
            if i > 0 and x == nums[i-1]:
                continue
            if x + nums[i+1] + nums[i+2] > 0:
                break
            if x + nums[-1] + nums[-2] < 0:
                continue

            j = i + 1
            k = n - 1
            while j<k:
                sum = x + nums[j] + nums[k]
                if sum == 0:
                    ans.append([x, nums[j], nums[k]])
                    j+=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1

                    k-=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1

                elif sum < 0:
                    j+=1

                elif sum > 0:
                    k-=1
        return ans  
    
if __name__ == "__main__":
    main()