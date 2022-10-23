from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        output = []
        for num in nums:
            if num not in output:
                output.append(num)
        length = len(output)
        output += list('_'*(len(nums)-len(output)))
        nums[:] = output
        return length

if __name__ == '__main__':
    print(Solution().removeDuplicates([1, 1, 2]))
