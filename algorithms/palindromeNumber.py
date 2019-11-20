'''
回文数
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        nx = str(x)
        nx_len = len(nx)
        for i in range(nx_len):
            if i > nx_len - 1 - i:
                break

            if nx[i] != nx[nx_len-1-i]:
                return False
        return True


if __name__ == '__main__':
    x = 12321
    # x = -1
    # x = 0
    # x = 123321
    # x = 23233232

    a = Solution().isPalindrome(x)
    print(a)