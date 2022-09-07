a=input("Enter email:")
for i ,j in enumerate(a):
    if j=="@":
        print(" username:{}\n".format(a[:i]),"domain:{}".format(a[i+1:]))
