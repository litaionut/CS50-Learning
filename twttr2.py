#get input
#look for vowel
# delete the vowels from string
# print the output

string = input("Enter any string: ")

newstr = string
print("\nRemoving vowels from the given string");
vowels = ('a', 'e', 'i', 'o', 'u');
for x in string:
    if x.lower() in vowels:
        newstr = newstr.replace(x,"");
print("New string after successfully removed all the vowels:");
print(newstr);
