"""
stringjumble.py
Author: waSclthu1
Credit: I looked up string-related python commands and found this website: https://www.w3schools.com/python/python_ref_string.asp
Where I found the "split" command which was super useful. I also found a useful "join" commande here: https://www.decalage.info/en/python/print_list

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
text = input(str("Please enter a string of text (the bigger the better): "))
print('you entered "{}". Now jumble it:'.format(text))
#Putting the words in reverse order
spaces = text.count(' ')
strlist = text.split( )
x= spaces
modlist1=[]
while (x>=0):
    modlist1.append(strlist[x])
    x=x-1
print( ' '.join(modlist1))



