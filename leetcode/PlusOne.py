class Solution:
    def plusOne(self, digits):
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    break
            if digits[0] == 0:
                digits = [1] + digits
            return digits

if __name__ == '__main__':
    print(Solution().plusOne([9, 9, 9, 9, 9, 9, 9, 9, 9]))
    print(Solution().plusOne([9]))