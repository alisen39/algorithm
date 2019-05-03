'''
给定一个字符串，找出最长的无重复子字符串
s = 'asdfavzxasdf'
i = 0
dp_key = 0
has_str = {}

for s  # start_index
    if st in has_str:
         has_str[st]
'''


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#
#         has_str = {}
#         longest_len = 0
#         start_index = 0
#
#
#         while True:
#             if len(s) == longest_len:
#                 return longest_len
#             s_temp = s[start_index]
#             if s_temp not in has_str:
#                 has_str[s_temp] = start_index
#
#             else:
#
#                 start_index = has_str[s_temp]
#                 if len(has_str) > longest_len:
#                     longest_len = len(has_str)
#                 has_str = {}
#
#             start_index += 1
#
#             if start_index == len(s):
#                 break
#
#         print(longest_len if longest_len >= len(has_str) else len(has_str))
#         return longest_len if longest_len >= len(has_str) else len(has_str)

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                if i > st[s[j]]:
                    print()
                i = max(st[s[j]],i)

                # i = st[s[j]]
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans


if __name__ == "__main__":
    s = "sdzccaasdsafasdfzxcassaasaasaaasasdqwertyuopa"
    # s = 'asdfghjklg'
    # s = 'ababababac'
    # s = 'ababc'
    # s = ''
    l = Solution().lengthOfLongestSubstring(s)
    print(l)
