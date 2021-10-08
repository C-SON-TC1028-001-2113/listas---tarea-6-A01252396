def main():
    r=int(input())
    c=int(input())
    m=r*c
    Lista=[]
    for i in range (m):
        n=int(input())
        if n<10:
            Lista.append(n)
    print(Lista)        
if __name__=='__main__':
    main()
