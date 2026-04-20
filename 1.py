import sys

class Solution:
    def twoSum(self, nums, target):
        from collections import defaultdict
        dic = defaultdict(int)
        for i,v in enumerate(nums):
            if target - v in dic.keys():
                return [dic[target-v],i]
            
            dic[nums[i]] = i
        
        return []


def main():
    line = sys.stdin.read().strip().split()
    nums = list(map(int,line[0:-2]))
    target = int(line[-1])

    sol = Solution()
    result = sol.twoSum(nums,target)

    print(result)

if __name__ == "__main__":
    main()