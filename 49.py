import sys

class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        dic = defaultdict(list)
        for word in strs:
            w = "".join(sorted(word))
            dic[w].append(word)
        return list(dic.values())
    
def main():
    line = sys.stdin.read().strip().split()
    strs = list(map(str,line))

    sol = Solution()
    result = sol.groupAnagrams(strs)
    print(result)

if __name__ == "__main__":
    main()