
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def Pattern(no1,no2):

    for i in range(no1):
        for j in range(no2):
            if i == j or i == 0 or i == no2-1 or j == 0 or j == no2-1:
                print(" *",end=" ")
            else:
                print(" ",end=" ")

        print()
            
def main():
    
    print("Enter Row  : ")
    row = int(input()) 
    
    print("Enter col  : ")
    col = int(input()) 
    
    Pattern(row,col)
    
if __name__ == "__main__":
    main()