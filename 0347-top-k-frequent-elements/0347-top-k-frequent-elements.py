class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        count = dict(sorted(count.items(), key= lambda item:item[1], reverse=True))
        mostFrequent = []
        for i in count.keys():
            mostFrequent.append(i)
            if len(mostFrequent) == k:
                return mostFrequent 