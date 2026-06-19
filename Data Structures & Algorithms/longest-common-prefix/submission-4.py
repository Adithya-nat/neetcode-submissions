class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        reference = strs[0]

        for index in range(len(reference)):
            for word in strs:
                if index == len(word) or word[index] != reference[index]:
                    return reference[:index]
        
        return reference


        