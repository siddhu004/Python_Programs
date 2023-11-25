import MarvellousFMR

CheakEven = lambda no : (no % 2 == 0)    
Increase =lambda no: no + 2
Add = lambda a,b:a+b    

def main():
    data = []
    print("enter the value you want to store: ")
    no = int(input())
    
    print("Enter value : ");
    for i in range(no):
        value = int(input())
        data.append(value)
        
    print("input data",data)
    output = list(MarvellousFMR.filterX(CheakEven,data))
    print("output after filter : ",output)
     
    output1 = list(MarvellousFMR.mapX(Increase,output))
    print("output after map : ",output1) 
    
    output2 = MarvellousFMR.ReduceX(Add,output1)
    print("output after reduce : ",output2)  
    
if __name__ == "__main__":
    main()