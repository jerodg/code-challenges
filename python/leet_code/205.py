class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Create a dictionary to store the mapping of characters
        mapping = {}

        # Iterate over the characters in the strings
        for i in range(len(s)):
            # Check if the character in s is already mapped
            if s[i] in mapping:
                # Check if the mapping is correct
                if mapping[s[i]] != t[i]:
                    return False
            else:
                # Check if the character in t is already mapped
                if t[i] in mapping.values():
                    return False
                mapping[s[i]] = t[i]

        return True
