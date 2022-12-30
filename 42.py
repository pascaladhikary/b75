class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        notes:  at any index i, water = min(max_left, max_right) - v[i]
                we can take and increment the smaller ptr because
                its lhs/rhs max so far is the min as the other ptr is forced larger
        '''
        l, r = 0, len(height)-1
        lhs, rhs, = 0, 0
        res = 0

        while l != r:
            if height[l] < height[r]:
                lhs = max(lhs, height[l])
                res += max(lhs - height[l], 0)
                l += 1
            else:
                rhs = max(rhs, height[r])
                res += max(rhs - height[r], 0)
                r -= 1

        return res


