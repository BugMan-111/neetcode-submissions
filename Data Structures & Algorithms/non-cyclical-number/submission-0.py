class Solution:
    def isHappy(self, n: int) -> bool:
        def nmap(n):
            s = str(n)
            total = 0
            for char in s:
                total += int(char) ** 2
            return total
        s = set()
        while n != 1:
            if n in s:
                return False
            s.add(n)
            n = nmap(n)

        return True






        
        
        