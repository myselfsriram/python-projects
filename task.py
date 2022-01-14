import sys
if(sys.argv[1]=="help"):
    print("Welcome to our bank what would you like to do\n1.Add your account \n2. Send an email\n3.check for mail \n4.Remove your account\n")
elif(sys.argv[1]=="1"):
    acc=input("Enter your mail id to be created:")
    o=open("data.txt","r")
    r=o.readlines()
    c=0
    for i in r:
        if(i == acc):
            print("Account already exixts")
            c=1
    if(c==0):
        pas=input("Enter your password:")
        k=open("data.txt","a")
        k.write(acc)
        k.write("\t\t\t")
        k.write(pas)
        k.write("\n")
        k.close()
        print("your data inserted successfully")
    o.close()
elif(sys.argv[1]=="4"):
    acc=input("Enter your account name to be removed:")
    pas=input("Enter your password to be removed:")
    with open("data.txt","r") as f:
        k=f.readlines()
    with open("data.txt","w") as e:
        for i in k:
            if (acc not in i) and (pas not in i):
                e.write(i)
                e.close()
    print("Account successfully removed")
    f.close()
elif(sys.argv[1] == "2"):
    semail=input("Enter your mail id:")
    remail=input("Enter the receiver mail:")
    o=open("data.txt","r")
    r=o.readlines()
    c=1
    for i in r:
        if(semail==i) and (remail ==i):
            print("Both or either one of accounts not exist in our data base")
            c=0
    if(c==1):
        message=input("Type your message\n\n")
        f=open("mails.txt","a")
        f.write("\nFrom Mail address is\t:")
        f.write(semail)
        f.write("\t\t")
        f.write("Message is:\t")
        f.write(message)
        f.write("\t\t")
        f.write("To :\t")
        f.write(remail)
        f.close()
        print("\nMail sent\n")
    o.close()
elif(sys.argv[1]=="3"):
    print("You want to view your mail\n")
    your=input("Enter your mail id:")
    pas=input("Enter your pass word:")
    o=open("data.txt","r")

