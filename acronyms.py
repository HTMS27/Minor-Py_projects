while True:
    i=input("Enter Phrase:")
    s=i.split()
    st=""
    for i in s:
        if i[0].isupper()==True:
            st=st+i[0].upper()

    print(st)
    print("c-continue,q-quit")
    if input()=='q':
        break
        
    
    
