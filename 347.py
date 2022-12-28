class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        notes:  map is sortable w/ sorted by key, returns list
                or heapq
        '''
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            
        pairs = [(-freq[n], n) for n in freq]
        heapq.heapify(pairs)
                
        return [heapq.heappop(pairs)[1] for i in range(k)]