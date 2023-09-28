class Two_sum():
    def __init__(self, nums: list, target: int):
        self.nums = nums
        self.target = target
    
    def brute_force(self) -> list:
        """
        O(N^2)
        """   
        n = len(self.nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if self.nums[i] + self.nums[j] == self.target:
                    return [i,j]
        return []

    def hash_map(self) -> list:
        """
        Hash map = dictionary
        O(N^2)
        """

        return list(next((i,j) for i,x in enumerate(self.nums) for j, y in enumerate(self.nums[i+1:], i+1) if x + y == self.target))
    
    def diff(self) -> list:
        """
        O(N) Approach - Most efficient implementation

        Initialize an empty dictionary (hash map) to store the values and their corresponding indices.
        Iterate through the input array nums from left to right.
        For each element nums[i], calculate the difference diff between the target and nums[i].
        Check if diff exists in the dictionary. If it does, you've found a pair of numbers that add up to the target. Return the indices of diff and i.
        If diff is not in the dictionary, store nums[i] in the dictionary with its index as the value.
        """
        num_indices = {}

        for i,num in enumerate(self.nums):
            diff = self.target - num
            if diff in num_indices:
                
                return [num_indices[diff], i]
            num_indices[num] = i
        
        return []