class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ferry = [[] for i in range(len(nums) + 1)]

        for num in nums:
           count[num] = 1 + count.get(num,0)
        
        for num, cnt in count.items():
            ferry[cnt].append(num)


        output = []

        for j in range(len(ferry) - 1, 0, -1):
            for num in ferry[j]:
                output.append(num)
                if len(output) == k:
                    return output
