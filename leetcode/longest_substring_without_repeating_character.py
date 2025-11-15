class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_ptr=0
        char_map = {}
        max_length=0
        for i, ch in enumerate(s):
            if ch in char_map and char_map[ch]>=left_ptr:
                left_ptr=char_map[ch]+1
            
            max_length=max(max_length,i-left_ptr+1)

            char_map[ch]=i
        return max_length

sol= Solution()
print(sol.lengthOfLongestSubstring("bbbbb"))

