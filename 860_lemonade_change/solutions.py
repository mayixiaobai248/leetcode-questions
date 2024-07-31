# 直接用defaultdict实现
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        packet = defaultdict(int)
        for i in bills:
            if i == 5:
                packet[5] += 1
            if i == 10:
                if packet[5] > 0:
                    packet[5] -= 1
                    packet[10] += 1
                else:
                    return False
            if i == 20:
                if packet[10] > 0 and packet[5] > 0:
                    packet[5] -= 1
                    packet[10] -= 1
                    packet[20] += 1
                elif packet[5] >= 3:
                    packet[5] -= 3     
                    packet[20] += 1              
                else:
                    return False
            
        return True