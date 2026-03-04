class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for str in strs:
            array = [0] * 26
            for char in str:
                array[ord(char) - ord('a')] += 1
            hashmap[tuple(array)].append(str)

        return [val for val in hashmap.values()]
