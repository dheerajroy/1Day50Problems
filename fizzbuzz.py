from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ["Fizz"*(d%3==0)+"Buzz"*(d%5==0) or f"{d}" for d in range(1,n+1)]

if __name__ == '__main__':
    print(Solution().fizzBuzz(n=5))
