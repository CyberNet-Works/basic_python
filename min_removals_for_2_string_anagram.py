'''
Thought process:
Find Unique Letters: by combining both strings and converting them into a set
Account for Repeating Letters by iterating through the unique characters 
For each character, find the difference in counts between the two strings using the count() function. 
Since anagrams require the same number of each character in both strings, you take the absolute difference to account for any excess or missing occurrences.

Calculate Total Removals: Sum up all the absolute differences calculated in step 2 to find the total number of removals needed to make the strings anagrams of each other.


'''

def min_removals_to_anagram(str1, str2):
    all_chars = set(str1 + str2)

    removals = 0

    for char in all_chars:
        str1_cnt = str1.count(char)
        str2_cnt = str2.count(char)
    
        removals += abs(str1_cnt - str2_cnt)
    return removals


'''
Minimum Removals to Make Two Strings Anagrams
Medium
Problem Description
Write a program to calculate the minimum number of letter removals so that two strings can be anagrams of each other.

An anagram is any string that can be formed by shuffling the characters of the original string. For example, dab is an anagram of bad.

Define a function named min_removals_to_anagram() with two arguments: str1 and str2.
Inside the function, calculate the number of characters that must be removed from both strings to make them anagrams.
'''
