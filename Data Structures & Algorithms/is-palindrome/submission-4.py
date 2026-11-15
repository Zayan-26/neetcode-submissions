class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitise = ""
        for ch in s.lower():
            if ch.isalnum():
                sanitise += ch
        return sanitise == sanitise[::-1]

        
