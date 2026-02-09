# Scramble_String-problem
we  solve the  scramble string by given two strings s1 and s2.  our  task is to check whether s2 can be made from s1 by:  Cutting the string into two parts and Swapping the parts and  Repeating this process any number of times  If yes, return True. Otherwise, return False that  sring is scramlbe or not .

# Approach to slove the problem

1.If both strings are already the same,Then they are obviously scramble strings Return True

2.Use memory to avoid repeating work,We store results of already checked string pairs in a dictionary

3.This makes the solution much faster

4.Check characters first,If both strings don’t have the same characters, they can never be scrambles So we return False early

5.Try all possible ways to split
6.For every possible split Check without swapping and Check with swapping

7.If any split works, return True,If nothing works Store False in memory
and return it

# Time Complexity O(n2)

# space Complexity O(n) 
