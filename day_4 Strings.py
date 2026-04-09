#Reversing a String
string="Python Programming"
string_reverse=string[::-1]
print(string_reverse)

#count vowels
count =0
for ch in string:
    if ch in "aeiou":
        count+=1
print(count)


#Check Palindrome
name="madam"
if name[0:] == name[::-1]:
    print("Its a Palindrome")
else:
    print("Its not a palindrome")