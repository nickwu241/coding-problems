# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        array_total = sum(A)
        if array_total % 3 != 0:
            return False
        
        target_total = array_total // 3
        current_total = 0
        n_partition = 0
        for num in A:
            current_total += num
            if current_total == target_total:
                if n_partition == 3:
                    return False
                current_total = 0
                n_partition += 1
                
        return n_partition == 3
