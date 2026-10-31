class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # create a map that maps digits with letters
        if len(digits) == 0:
            return []
        digit_map = {
            "2" : "ABC",
            "3" : "DEF",
            "4" : "GHI",
            "5" : "JKL",
            "6" : "MNO",
            "7" : "PQRS",
            "8" : "TUV",
            "9" : "WXYZ"
        }
        result = []

        def recur(digits, prev, counter, result):
            if counter >= len(digits):
                result.append("".join(prev).lower())
                return
            current_digit = digits[counter]
            possible_chars = digit_map[current_digit]

            for char in possible_chars:  
                Next = deepcopy(prev)
                Next.append(char)
                recur(digits, Next, counter + 1, result)

        recur(digits, [], 0, result)

        return result

        