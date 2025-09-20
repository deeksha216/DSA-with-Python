word=input("enter a string")
vowels="aeiouAEIOU"
count_vowel=0
count_consonant=0

for i in word:
    if i.isalpha():
     if i in vowels:
        count_vowel +=1
     else:
        count_consonant +=1
print("number of vowels",count_vowel)
print("number of constants",count_consonant)