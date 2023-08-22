# Get the character at position 1
a="hello gudmng"
print(a[1])
print()
# Loop through the letters in the word "banana":
for x in "banana":
    print(x)
# To get the length of a string, use the len() function. space also 
print(len(a))
# To check if a certain phrase or character is present in a string, we can use the keyword in.
print("hello"in a)
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
print(a[1:6])
# By leaving out the start index, the range will start at the first character:
# By leaving out the end index, the range will go to the end:
b = "Hello, World!"
print(b[2:])
# Use negative indexes to start the slice from the end of the string: