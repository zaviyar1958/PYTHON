x = input("Enter a string: ")
di = {'vowel' : 0, 'consonent' : 0}
x = x.replace(" ","")
x = x.lower()
for char in x:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        di["vowel"] +=1
    else :
        di['consonent'] +=1
print(f"Number of vowels = {di['vowel']}")
print(f"Number of consonent = {di['consonent']}")
