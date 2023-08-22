# Python Program to count occurrences of a character in below string and create a dictionary with keys as
# letters and values as count of occurrences of that letter.

str= "fhdflshbfslkhfbslkfbhslfjhbsdvsJKBEFWEGWUYRTWGRUWOFWGEUIFBWDFWDBFHWJDVFHJKasdwtuknfiitngjt75378595hf75hr74h"
d={}
for ch in str:
    if ch in d:
        d[ch]+=1

    else:
        d[ch]=1
print(d)

