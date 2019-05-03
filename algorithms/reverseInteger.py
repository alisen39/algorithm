'''
整数反转
'''


class Solution:
    INT32_MAXVALUE = 2 ** 31 - 1
    INT32_MINVALUE = -2 ** 31

    def reverse(self, x: int) -> int:
        rev = ''
        if x < 0:
            rev = '-'
        for i in reversed(str(x).lstrip('-')):
            rev += i
        if int(rev) > self.INT32_MAXVALUE or int(rev) < self.INT32_MINVALUE:
            return 0
        return int(rev)
        # rev = 0
        # while x != 0:
        #     pop = x%10
        #     x = int(x/10)
        #
        #     rev = rev * 10 + pop
        #     print(x,rev)
        # print(rev)
        # print(self.INT32_MINVALUE)


if __name__ == '__main__':
    x = 123
    x = -123
    x = 0
    x = 1230
    # x = -1230
    # x = 1202
    # x = -2147483648
    a = Solution().reverse(x)
    print(a)
