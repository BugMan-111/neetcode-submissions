class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def map(s):
            l = [0] * 26
            for char in s:
                l[ord(char) - ord("a")] += 1
            return tuple(l)

        d = {}
        for s in strs: 
            mapped_s = map(s)
            if mapped_s in d:
                d[mapped_s].append(s)
            else:
                d[mapped_s] = [s]

        result = []
        for key in d:
            result.append(d[key])

        return result
        