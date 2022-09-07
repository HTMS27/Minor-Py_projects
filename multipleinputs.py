while True:
    i=input("Enter Phrase:")
    s=i.split()
    st=""
    for i in s:
        st=st+i[0].upper()

    print(st)
    print("c-continue,q-quit")
    if input()=='q':
        break
        
    
    
