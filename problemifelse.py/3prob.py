message = input("enter the word : ")
a = "make a lot money"
b= "buy now"
c = "subscribe"
if((a in message) or (b in message) or (c in message)):
    print("spam detect")
else:
    print("no spam")