class Solution:
    def numberOfSteps(self, num: int) -> int:
        bitstring = bin(num)[2:]; return len(bitstring) - 1 + bitstring.count('1')

if __name__ == '__main__':
    print(Solution().numberOfSteps(5))
