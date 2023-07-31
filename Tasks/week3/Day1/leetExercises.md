# LeetCode Exercises

###  <a href = "https://leetcode.com/problems/contains-duplicate"> 1. Contains Deuplicate</a>
> Code

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       
        return nums!=list(set(nums)) # we cast the list to set DataType so it
```



###  <a href = "https://leetcode.com/problems/valid-anagram/"> 2. Valid Anagram</a>
> Code

```python
   class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        return set(s) == set(t) # The order of items doesn't matter in set 
                                # so we turn the anagrams into sets and compare them to each other, if they contain the same letters, the output will be true
```

###  <a href = "https://leetcode.com/problems/two-sum/"> 3. Two Sums</a>
> Code

```python

  class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = 0
        
        while count < len(nums):
            if nums[count] + nums[count + 1] == target :
                return count, count + 1
            count = count + 1
```
