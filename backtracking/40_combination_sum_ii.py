class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start, remaining, path):
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted, no need to continue
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return res