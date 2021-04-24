# Bucket Fill
# Given a picture represented as a 2-dimentional array of letters
# representing colors, find the minimum number of fills to completely
# repaint the picture

def print_matrix(m):
    for i in m:
        print(i)
    print('\n')
    
def bucket_fill(m, i, j, letter):
    # Check boundaries of the matrix
    if((j >= len(m[0]) or j < 0) or (i >= len(m) or i < 0)):
        return
    
    # Base case of recurtion
    if(m[i][j] == -1 or m[i][j] != letter):
         return 
    
    # Set the current node 
    m[i][j] = -1
    
    # With recurtion check for letter in left, right, up and down
    bucket_fill(m, i, j+1, letter)
    bucket_fill(m, i, j-1, letter)
    bucket_fill(m, i+1, j, letter)
    bucket_fill(m, i-1, j, letter)
    return

def repaint_picture(m):
    count = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if(m[i][j] != -1):
                count += 1
                bucket_fill(m, i, j, m[i][j])
    return count

if __name__ == "__main__":
    # Expected: 6
    m = [['b', 'b', 'b', 'a'], 
         ['a', 'b', 'b', 'a'], 
         ['a', 'c', 'a', 'a'], 
         ['a', 'b', 'a', 'c']]
    # Expected: 5
    m1 = [['a', 'a', 'b', 'b', 'a'], 
         ['a', 'a', 'b', 'b', 'a'], 
         ['a', 'a', 'a', 'c', 'b']]
    # Expected: 5
    m2 = [['a', 'a', 'a', 'b', 'a'], 
         ['a', 'b', 'a', 'b', 'a'], 
         ['a', 'a', 'a', 'c', 'a']]
    # Expected: 4
    m3 = [['b', 'b', 'b', 'a'], 
         ['a', 'b', 'b', 'a'], 
         ['a', 'c', 'a', 'a'], 
         ['a', 'a', 'a', 'c']]
    
    print("M:")
    print_matrix(m)
    print("number of fills: ",repaint_picture(m), "\n")
    print("M1:")
    print_matrix(m1)
    print("number of fills: ",repaint_picture(m1), "\n")
    print("M2:")
    print_matrix(m2)
    print("number of fills: ",repaint_picture(m2), "\n")
    print("M3:")
    print_matrix(m3)
    print("number of fills: ",repaint_picture(m3), "\n")
