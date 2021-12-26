
class arrays():
    def __init__(self,array):
        self.array = array

    def move_zeros(self):
        array = self.array
        move_zeros_result = []
        zeros = 0

        for i in array:
            if i == 0 and type(i) != bool:  # not using `not i` to avoid `False`, `[]`, etc.
                zeros += 1
            else:
                move_zeros_result.append(i)

        move_zeros_result.extend([0] * zeros)
        return move_zeros_result

    def plus_one(self):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = self.array
        digits[-1] = digits[-1] + 1
        res = []
        ten = 0
        i = len(digits) - 1
        while i >= 0 or ten == 1:
            summ = 0
            if i >= 0:
                summ += digits[i]
            if ten:
                summ += 1
            res.append(summ % 10)
            ten = summ // 10
            i -= 1
        return res[::-1]

class string():
    def __init__(self,string):
        self.string = string

    def reverseString(self):
        s = self.string
        s[:] = s[::-1]
        return s[:]

    def reverseInteger(self):
        x = self.string
        nums = 0
        max_int = 2 ** 31 - 1
        min_int = -2 ** 31
        y = abs(x)
        while (y > 0):
            nums = nums * 10 + y % 10
            y //= 10
        if x < 0:
            nums *= -1
        if nums > max_int or nums < min_int:
            return 0
        return nums