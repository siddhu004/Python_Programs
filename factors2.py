
no = 0
print("enter number: ")
no = int(input())

for i in range(1,no,1):
    if(no % i == 0):
        print(i)
