class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            print(s)
            if token == "+":
                s.append(s.pop() + s.pop())
            elif token == "-":
                s1 = s.pop()
                s2 = s.pop()
                s.append(s2 - s1)
            elif token == "*":
                s.append(s.pop() * s.pop())
            elif token == "/":
                d1 = s.pop()
                d2 = s.pop()
                s.append(int(float(d2)/d1))
            else:
                s.append(int(token))
        return s.pop()  
    
        