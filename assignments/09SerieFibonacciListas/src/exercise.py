def main():
    Lista1=[0,1]
    Lista3=[0]
    Lista2=[]
    i=-1
    while i<0:
        i=int(input())
        if i==0:
            print(Lista2)
        elif i>0:
            if i==1:
                print(Lista3) 
            elif i==2:
                print(Lista1)   
            elif i>2:
                for j in range (i-2):
                    Lista1.append(Lista1[j]+Lista1[j+1])  
                print(Lista1)         
if __name__=='__main__':
    main()
