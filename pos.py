list1=[]
n=int(input("Enter size of list:"))
for i in range(0,n):
    e=int(input("Enter element of list "))
    list1.append(e)

print("Positive numbers in",list1,"are:")

positive= [nu for nu in list1 if nu > 0]
print(positive)