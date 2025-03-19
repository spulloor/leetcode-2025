class Solution:
    def isHappy(self, n: int) -> bool:

        slow = n
        fast = n

        while True:

            # slow is twice as slow as fast
            slow = self.squareDigits(slow)
            fast = self.squareDigits(self.squareDigits(fast))

            if slow == fast:
                break


        return slow == 1

        return False

    def squareDigits(self, n):
        res = 0
        while n > 0:
            digit = n % 10
            n //= 10

            # square the digit and add it to res
            res += digit ** 2

        return res
        