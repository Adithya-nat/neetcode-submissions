class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        nToDigits = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []

        def backtrack(index, current):
            if index == len(digits):
                result.append("".join(current))
                return
            
            for letter in nToDigits[digits[index]]:
                current.append(letter)
                backtrack(index+1, current)
                current.pop()
            
        current = []
        backtrack(0, current)

        return result

        