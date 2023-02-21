StrVowel=input("Enter the string to get the count: ")
vowels='aeiou'
x=0
str1=""
n1=""
for i in StrVowel:
    if i==vowels[x]:
        str1=str1+i
    if x<(len(vowels)-1):
        if i==vowels[x+1]:
            str1=str1+i
            x=x+1
for i in StrVowel:
    if i not in n1:
        n1=n1+i
n1="".join(sorted(n1, key=str.lower))
if n1!=vowels:
    print(0)
    print(n1)
else:
    print(len(str1))

            
