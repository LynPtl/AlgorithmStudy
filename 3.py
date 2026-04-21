import sys

class Solution:
    def lengthOfLongestSubstring(self, s):
        left = right = 0
        n = len(s)
        st = set()
        l = 0
        ans = 0
        while right<n:
            if s[right] not in st:
                st.add(s[right])
                right += 1
                l += 1
                ans = max(ans,l)
            else:
                while s[right] in st:
                    st.remove(s[left])
                    left += 1
                    l -= 1
        
        return ans

def main():
    line = sys.stdin.read().strip()
    sol = Solution()
    result = sol.lengthOfLongestSubstring(line)
    print(result)

if __name__ == "__main__":
    main()