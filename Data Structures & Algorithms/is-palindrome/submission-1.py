class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers
        # from s[start] == s[end]

        # case insentive
        s = s.upper()

        # filter the given string
        string = []
        for char in s:
            if (ord(char) >= ord("A") and ord(char) <= ord("Z")) or (ord(char) >= ord("0") and ord(char) <= ord("9")) :
                string.append(char)

        start = 0
        end = len(string) - 1

        while start < end:
            if string[start] != string[end]:
                return False
            
            start += 1
            end -= 1

        return True



        