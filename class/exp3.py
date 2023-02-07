#Ankit Das
#SE4A
#Roll no: 10
#Write a python program to implement the following.a) Find the longest s in a list of str b) Reverse a list using recursion.

str = ["This", "is", "a", "wonderful", "world", "here"]   # list of str
longest = ""    
for s in str:  # iterate over str
    if len(s) > len(longest):    # if length of s is greater than length of longest s
        longest = s  
print("Longest word:", longest) 

str = ["This", "is", "a", "wonderful", "world", "here"]   
reversed_str = list(reversed(str))  # reverse the list
print("Reversed str:", reversed_str)


