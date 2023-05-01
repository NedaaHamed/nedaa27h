def edit_distance(s1, s2):# Define function  that takes in two strings as arguments

    if len(s1) > len(s2):# If the length of s1 is greater than the length of s2 
        differ = len(s1) - len(s2)# calculate the difference between their lengths and store it in differ
        s1[:differ]

    elif len(s2) > len(s1):
        differ = len(s2) - len(s1)
        s2[:differ]

    else:
        differ = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            differ += 1
#If the character at index i in s1 is not equal to the character at index i in s2 increment the differ variable by 1.
    return differ

print(edit_distance("kitten", "sitting")) 
print(edit_distance("medium", "median")) 
