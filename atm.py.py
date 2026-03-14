balance=500
password= 12345

while True:

    print("welcome to the canara bank atm")

    print("1 - deposit")
    print("2 - withdraw")
    print("3 - balance")
    print("4 - exit")

    choice=(input("enter your choice[1-4] :"))

    if choice=="1":
        amount=float(input("enter your deposit amount: "))
        password=float(input("enter your password"))
        if password ==12345:
            balance += amount
            print(f"${amount} deposited successfully")
    
        else:
          print("your password is imcorrect")
    elif choice == "2" :
        amount=float(input("enter your withdraw amount"))
    

        if amount<=balance:
        
            password= float(input("enter your password"))
            if password == 12345 :
                balance -= amount
                print(f"${amount} withdraw succefully")
            
        else:
            print("insufficient balance")

    elif choice == "3":
        print(f"balace from your account is ${balance}.")

    elif choice == "4":
        print("exist the system")


    else:
        print("invalid option choose correct option")
