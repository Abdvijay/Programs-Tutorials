ch = input("Enter the character : ")[0]
if ch in 'aeiou':
    print("Character ",ch," is Vowel")
elif ch.isalpha():
    print("Character ",ch," is Consonant")
else:
    print("Character ",ch," is not a Letter")

"""

PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\If-Else-Programs> python VowelOrConsonant.py
Enter the character : 4
Character  4  is not a Letter
PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\If-Else-Programs> python VowelOrConsonant.py
Enter the character : i
Character  i  is Vowel
PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\If-Else-Programs> python VowelOrConsonant.py
Enter the character : r
Character  r  is Consonant

"""