# 暴力解法
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(cost)):
            remain = gas[i] - cost[i]
            index = i + 1
            while (index % len(cost) != i):
                # mean that this index of i is impossible
                if remain < 0:
                    break
                remain += gas[index % len(cost)] - cost[index % len(cost)]
                index += 1
            
            if index % len(cost) == i  and remain >= 0:
                return i
        
        return -1
    
# 只需要一次循环的贪心算法
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        total_cost = 0
        remain = 0
        start_index = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            remain += gas[i] - cost[i]
            
            # If remain is negative, reset starting point to i+1
            if remain < 0:
                start_index = i + 1
                remain = 0
        
        # If the total gas is less than total cost, it is impossible to complete the circuit
        if total_gas < total_cost:
            return -1
        
        return start_index