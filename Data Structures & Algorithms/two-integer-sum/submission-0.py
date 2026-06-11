class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  
        #creates a hashmap that will store numbers as keys with their indexes as values

        for i, n in enumerate(nums): 
            #loop through nums getting both their index i and values n
            diff = target - n 
            #find the difference between the target and the current value
            #to determine the number needed to reach the target
            if diff in prevMap and prevMap[diff]!= i: 
                #check if the diff is in the hashmap and that 
                #the index of the diff in the hashmap is not equal to the current index
                return [prevMap[diff], i] 
                # if the diff is in the hashmap and not the current index,
                #return the result which is the index of the diff from the hashmap
                #and the current index in nums
            prevMap[n] = i
            #if the diff is not in the hashmap or its index is the same as
            #the current num index, then store the current index in the hashmap
            #and continue iteration.