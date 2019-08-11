class Solution:
    def toLowerCase(self, str: str) -> str:
        return ''.join([chr(ord(i) + 32) if ord(i) >= 65 and ord(i) <= 91 else i for i in str])
    
        # letters = set(str)
        # for letter in letters:
        #     if letter.isupper():
        #         str = str.replace(letter, letter.lower())
        # return str
    
        # return str.lower()
