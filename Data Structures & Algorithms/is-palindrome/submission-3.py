class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = ""
        for ch in s.lower():
            if ch.isalnum():
                check += ch.lower()
        return (check == check[::-1])
