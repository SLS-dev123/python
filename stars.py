num = int(input("Enter the number of stars:"))
n = num
nums = num
y=num
for i in range (1,nums):
    print(sep = "\n")
    for t in range(1,y):
        print(end =" ")
    for j in range(1, i+1):
        print(end = " *") 
    y=y-1
while num >= 0:
    print(sep = "\n")
    for i in range(1,n+1-num) :
        print(end =" ")
    for j in range(1, num+1):
        print(end = " *") 
    num = num-1
#python stars.py