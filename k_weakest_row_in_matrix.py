from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return list(dict(sorted(((i, sum(mat[i])) for i in range(len(mat))), key=lambda x: x[1])).keys())[:k]


if __name__ == '__main__':
    print(Solution().kWeakestRows([[1, 1, 0, 0, 0],
                                   [1, 1, 1, 1, 0],
                                   [1, 0, 0, 0, 0],
                                   [1, 1, 0, 0, 0],
                                   [1, 1, 1, 1, 1]]))
