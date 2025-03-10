sentence = input("enter the string to be reversed: ")
reversed_string =""
lenght = len(sentence)
for i in range(lenght-1,-1,-1):
    reversed_string+=sentence[i]
if sentence == reversed_string:
    print("pallindrom")
else:
    print("not pallindrom")
print(reversed_string)