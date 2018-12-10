''' Write code using find() and string slicing to extract the number at the end of the line below. Convert the
extracted value to a floting point number and print it out. 
The LINE example is: text = "X-DSPAM-Confidence:    0.8475";
'''

text = "X-DSPAM-Confidence:    0.8475";

first = text.find('0')
print(first)

second = text.find[first+2:]
print(second)

third = text[first:second]
print(third)

fourth = float(third)
print(fourth)

#Above works but this way is what the server wanted
text = "X-DSPAM-Confidence:    0.8475";
first = text.find(':')
second = text[first+2:]
third = float(second)
print(third)