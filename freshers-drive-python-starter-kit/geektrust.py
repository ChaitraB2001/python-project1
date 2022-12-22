from sys import argv
import os
def icost(item):
    switch={
      'T':1000,
      'J':2000,
      'C':500,
      'N':200,
      'P':300,
      'M':500
      }
    return switch.get(item,"Invalid input")

def idis(item):
    switch={
      'T':0.10,
      'J':0.05,
      'C':0.20,
      'N':0.20,
      'P':0.10,
      'M':0.05
      }
    return switch.get(item,"Invalid input")


def read_text_file(file_path):
    with open(file_path, 'r') as f:
        
        ans=[]
        for line in f:
            res=[]    
            for word in line.split():
                res.append(word)
            ans.append(res)      

    items=[]
    ta=0
    td=0
   
        
    for line in ans[:-1:]:
            # Add your code here to process input commands.
            #line=list(line.split())
           
        if line[1] in ['TSHIRT','JACKET','CAP']:
            if int(line[2])>2:
                print('ERROR_QUANTITY_EXCEEDED')
                continue
            else:
                print('ITEM_ADDED')
                items.append(line[2]+line[1])
                amt=icost(line[1][0])
                ta+=int(line[2])*amt
                td+=amt*idis(line[1][0])*int(line[2])
        else:
            if int(line[2])>3:
                print('ERROR_QUANTITY_EXCEEDED')
                continue
            else:
                print('ITEM_ADDED')
                items.append(line[2]+line[1])
                amt=icost(line[1][0])
                ta+=int(line[2])*amt
                td+=amt*idis(line[1][0])*int(line[2])
    if ta>3000:
        #An additional discount of 5% can be applied if the total amount to pay is 3000 rupees or more.
        td=td+ta*0.05
        print('TOTAL_DISCOUNT ',round(td,2))
        print('TOTAL_AMOUNT_TO_PAY ',round((ta-td)*1.10,2))
    elif ta>1000:
        #Discounts can be applied only if the total purchase amount is 1000 rupees or more.
        print('TOTAL_DISCOUNT ',round(td,2))
        print('TOTAL_AMOUNT_TO_PAY ',round((ta-td)*1.10,2))
    else:
        print('TOTAL_DISCOUNT ',round(0.00,2))
        print('TOTAL_AMOUNT_TO_PAY ',round(ta*1.10,2))
    print()    
    

def main():
    
    if len(argv)!=2:
        raise Exception("File path not entered")
    
    file_path=argv[1]
    f=open(file_path,'r')
    Lines=f.readlines()
    read_text_file(file_path)
     
        
    
if __name__ == "__main__":
    main()