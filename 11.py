class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        notes:  at any index i, water = min(max_left, max_right) - v[i]
                we can take and increment the smaller ptr because
                as we travel l->r, lhs is forced < rhs and vice versa 
        '''
        l, r = 0, len(height)-1
        lhs, rhs, = 0, 0
        res = 0

        while l != r:
            if height[l] < height[r]:
                lhs = max(lhs, height[l])
                res += lhs - height[l]
                l += 1
            else:
                rhs = max(rhs, height[r])
                res += rhs - height[r]
                r -= 1

        return res
