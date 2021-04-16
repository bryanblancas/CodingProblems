# Given a pattern s1 and the string s2:
# print True if any permutation of s1 is in s2

# s1 = coder
# s2 = credoc
# should be TRUE

# s1 = coder
# s2 = rfedoc
# should be FALSE

def permutatedSubstring(s1,s2):
    # Validations to avoid work more of necessary
    size_s1 = len(s1) # n
    size_s2 = len(s2) # m
    if(size_s2 < size_s1 or size_s2 == 0 or size_s1 == 0):
        return False
    
    # arrays to storage letters concurrencies
    letters = [0 for i in range(0,26)]
    cur_window = [0 for i in range(0,26)]
    
    # Fill the array of pattern letters
    # O(n)
    for letter in s1:
        letters[ord(letter)-97] += 1
    
    # Fill the initial window
    # O(n)
    for i in range(0, size_s1):
        cur_window[ord(s2[i])-97] += 1
    
    i = 0
    # O(m - n) 
    while(i < size_s2 - size_s1):
        
        if letters == cur_window:
            return True
        
        # Remove first letter in current window (s2) from cur_window
        cur_window[ord(s2[i])-97] -= 1
        # Add next letter from s2 to cur_window
        cur_window[ord(s2[size_s1+i])-97] += 1
        
        i += 1
        
    # Handle last validation
    if letters == cur_window:
        return True
    return False
    
s1 = "aabb"
s2 = "ccoderbbbbabbabbmm"

print(permutatedSubstring(s1, s2))
