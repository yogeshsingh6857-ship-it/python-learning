mark1=float(input("enter the marks pf 1 :"))
mark2=float(input("enter the marks pf 2 :"))
mark3=float(input("enter the marks pf 3 :"))
total = mark1+mark2+mark3
per=(total/300)*100
if(total>=40 and mark1>=33):
    print("pass")
elif(total>=40 and mark2>=33):
    print("pass")
elif(total>=40 and mark3>=33):
    print("pass")
else:
    print("fail")