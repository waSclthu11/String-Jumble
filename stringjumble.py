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
while (x>=0): #A loops that makes a list in reverse of the origional strlist
    modlist1.append(strlist[x])
    x=x-1
j1 =  ' '.join(modlist1) #Turns list to string and puts spaces between list elements
print(j1)
#putting the words backwards in reverse order
j2 =  '_'.join(j1)#This sets it up so the split command will put spaces in the list
jree =  ' '.join(j1)
spaces2 = jree.count(' ')
strlist2 = j2.split("_") #Makes a list with some spaces so the results will have spaces too
y=spaces2-(spaces)
modlist2=[]
while (y>=0): #reverses the strlist2 list
    modlist2.append(strlist2[y])
    y=y-1
j2=  ''.join(modlist2) #gets rid of extra spaces and also turns the list into string
print(j2)

strlist3=j2.split( )
print=strlist3
z=spaces
modlist3=[]
while (z>=0): #A loops that makes a list in reverse of the origional strlist
    modlist3.append(strlist3[z])
    z=z-1
j3=' '.join(modlist3)
print(j3)



