class Solution:
    def reverse_word(self, s: str) -> str:
        s = list(s)
        l = 0

        for r in range(len(s)):
            if s[r] == " " or r == len(s) - 1:
                temp_r = r if (r == len(s) - 1 and s[r] != " ") else r - 1
                temp_l = l

                while temp_l < temp_r:
                    s[temp_l], s[temp_r] = s[temp_r], s[temp_l]
                    temp_l += 1
                    temp_r -= 1

                l = r + 1

        return "".join(s)


sol = Solution()
print(sol.reverse_word("Let's take LeetCode contest"))