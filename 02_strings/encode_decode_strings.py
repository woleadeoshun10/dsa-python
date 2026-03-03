"""
Problem: Encode and Decode Strings

Design an algorithm to encode a list of strings into a single string,
and then decode it back to the original list.

Approach:
We prefix each string with its length followed by a delimiter (#).
During decoding, we read the length first, then extract that many characters.

Time Complexity:
    Encode: O(N)
    Decode: O(N)
Where N is total number of characters across all strings.

Space Complexity:
    O(N)
"""

class Solution:
    def encode(self, strs):
        """
        Encodes a list of strings to a single string.
        """
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s):
        """
        Decodes a single string back to a list of strings.
        """
        decoded = []
        i = 0

        while i < len(s):
            j = i

            # Move j until we find the delimiter '#'
            while s[j] != "#":
                j += 1

            # Extract length of the string
            length = int(s[i:j])

            # Move i to start of actual string
            i = j + 1

            # Extract the string using its length
            j = i + length
            decoded.append(s[i:j])

            # Move pointer to next encoded string
            i = j

        return decoded


# Example usage (for local testing)
if __name__ == "__main__":
    solution = Solution()
    data = ["cat", "dog", "hello"]
    encoded = solution.encode(data)
    decoded = solution.decode(encoded)

    print("Encoded:", encoded)
    print("Decoded:", decoded)