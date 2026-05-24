import random 
import datetime


# Hard-Coded Passwords
passkey = "admin123"


# Pre-Defined Functions 
# __________________________________________________________________________________________________________________________________


def show_menu():
    menu = {
    1 : "Enter 1 for creating a new account.",
    2 : "Enter 2 to login to an existing account.",
    3 : "Enter 3 for Administrator Control.",
    4 : "Enter 4 for Help and Contacts.",
    5 : "Enter 5 for About.",
    6 : "Enter 6 to Exit."
      }
    print()
    for key in menu.keys():
        print(f"{menu[key]}")
    print()


def generate_accountnumber(name : str ):
                account_number = ""
                last_8_digits = str(int(random.uniform(10000000,99999999)))
                for n in name[0:3]:
                    account_number += str(ord(n))
                
                account_number +=  last_8_digits
                return account_number[0:11]


def create_new_account(name : str , age : str , account_type : str , password : str , balance = 0.00  ):
        
        account_number = generate_accountnumber(name) 

        user_account_details = (name, age ,account_type,account_number,password,balance)
        
        file = open("user_data.csv","a")
        file.write("\n")
        for data in user_account_details[0:-1]:
            file.write(str(data) + ",")
            file.flush()
        file.write(str(user_account_details[-1]))
        file.write("\n")
        file.close()

        return user_account_details


def login(user_id : str , password : str ):
    status = False
    uid = False
    pswrd = False
    with open("user_data.csv","r") as file:
          data = file.readlines()
          for d in data[1::]:
               an,p = d.split(",")[3:5]
               if user_id == an:
                    uid = True 
                    if password == p:
                         status = True
                         pswrd = True 
                         break
          return status 


def find_balance(user_id : str , password : str ):
    balance = 0 
    with open("user_data.csv","r") as file:
          data = file.readlines()
          for d in data[1::]:
               an,p,b = d.split(",")[3:6]
               if user_id == an:
                    uid = True 
                    if password == p:
                         balance = b 
                         break
          return balance


def update_balance(user_id : str  ,amt : float , mode : int ):
     
     r,c = 0,5
     balance = 0 
     with open("user_data.csv","r") as file:
          data = file.readlines()

          for d in data[1::]:
               an,p,b = d.split(",")[3:6]
               r += 1 
               if user_id == an:
                    
                    balance = b 
                    break
          target_row = data[r].strip().split(",")
          if mode == 1:
              target_row[c] = str(float(balance) + amt)
          elif mode == -1:
               target_row[c] = str(float(balance) - amt)
               
          data[r] = ",".join(target_row) + "\n"

     with open("user_data.csv","w") as file:
          file.writelines(data)
          r,c = 0,5 


def view_userdata():
    with open("user_data.csv","r") as file:
          data = file.read()
          return data 


def  delete_user(user_id : str ):
     r = 0
     c = 3
     result = False
     
     with open("user_data.csv","r") as file:
          data = file.readlines()

          for d in data[1::]:
               acno  = d.split(",")[c]
               r += 1 
               if user_id == acno:
                    result = True 
                    break
        
          if result :
               del data[r]
               with open("user_data.csv","w") as file:
                    file.writelines(data)
     return  result 


def log_transactions(user_id , user_id_receiver  , amt , time,mode ):
     details = {"Sender's Account Number": user_id ,"Receiver's Account Number":user_id_receiver, "Type": mode, "Amount" : amt , "Time" : time}

     with open("transactions.txt","a+") as file:
         file.write(str(details) + "\n")
          

def show_transactions():
    with open("transactions.txt","r") as file:
        data = file.readlines()
        for d in data:
            print(d)


def  check_account(user_id : str ):
     
     c = 3
     result = False
     
     with open("user_data.csv","r") as file:
          data = file.readlines()

          for d in data[1::]:
               acno  = d.split(",")[c]
               if user_id == acno:
                    result = True 
                    break
     return  result 


#___________________________________________________________________________________________________________________________________

# Main Part 
          
print("                                    Welcome to VAHSIR Bank                              ")


status_main = True  # Main Control Switch 
while status_main:
    print("------------------------------------------------------------------------------------------------")
    print("_______________ Menu_________________")
    (show_menu())
    print("------------------------------------------------------------------------------------------------")
    

    while True:
        try:
            ch = int(input("Enter choice: "))
            break
        except:
          print("Enter numbers only.")
        
    if ch == 1:
            # Account Creation for new users.
            print()
            print("Enter the following details.")
            print()
        
         
            # Input from user 
            name = input("Enter your name :").strip()
            age = int(input("Enter your age in numbers :"))
            print()
        
            # Age Criterion 
            if age <  18:
                print("You are a minor and not eligible for opening the account.")
            else:
                acc_type = None
                while True: 
                    account_types = ("savings","current","business")
                    print()
                    acc_type = input(f"Enter preferred account type { account_types} :").strip().lower()
                    print()

                    if acc_type  not in account_types:
                        print(f"Enter correct account type from {account_types}")
                    else:
                        print(f"Account type Chosen : {acc_type}")
                        print()
                        break
               
                print()
                print("Set your account password.")
                print()

                password = input("Enter your password :")
                print()
            
                while True:
                    password_2  = input("Re-Enter your password :")
                    if password_2 != password:
                        print("Enter matching password.")
                    else:
                        print()
                        print(f"Password Set to: {password}")
                        print()
                    
                        break
                generate_accountnumber(name)
                details = create_new_account(name,age,acc_type,password)

                print("_____________________________________________")
                print("Your account is successfully created with us.")
                print()
                print("The details are as follows:")
                print()
                print(details)
            
                print("______________________________________________")
                print()
    
    
    elif ch == 2:

        print("Account Login ")
        print()

        user_id = input("Enter your account number :").strip()
        password = input("Enter your password:").strip()
        print()

        if login(user_id,password):
            print()
            print("Logged in Successfully.")
            print()
            print("Choose an action from the following menu.")
            print()
          
            while True:

                print("Enter 1 for withdrawal.")
                print("Enter 2 for deposit.")
                print("Enter 3 for payment.")
                print("Enter 4 to check balance.")
                print("Enter 5 to logout.")

                while True:
                    try:
                        choice = int(input("Enter choice: "))
                        break
                    except:
                        print("Enter numbers only.")
            
                if choice == 1:
                    # Withdraw Process Initiated

                    mode = -1          # Default Mode -1 for withdrawal
                    withdrawal = True  
                    print("Withdrawal Selected.")
                    print()

                    # User Input 
                    balance = float(find_balance(user_id,password))
                    print(f"Current Balance : $ {balance}")
                    print()

                    while withdrawal:
                        amt = float(input("Enter amount to withdraw :"))
                        if amt > balance:
                            print()
                            print("Insufficient Balance.")
                            print()
                            print(f"Enter amount less than or equal to ${balance}")
                            continue
                    
                        else:
                            print("Please verify to continue.")
                            print()
                            while True:
                                p = input("Enter the password:")
                                if p == password:
                                    withdrawal = False
                                
                                    # Final update of balancee in data file 
                                    update_balance(user_id,amt,mode)
                                    time = datetime.datetime.now()
                                    log_transactions(user_id,user_id,amt,time,mode = -1)

                                    print()
                                    print(f"Withdraw of $ {amt} Confirmed. ")
                                    print()
                                    print(f"Final Balance : $ {find_balance(user_id,password)}")

                                
                                    break
                                else:
                                    print("Enter correct password.")
                                    continue

                elif choice == 2:   
        
                    print("Deposit Selected")
                    print()
                
                    deposit  = True  
                    mode = 1  # Default mode 1 for deposit 
                    print("Deposit Selected.")
                    print()

                    balance = float(find_balance(user_id,password))
                    print(f"Current Balance : $ {balance}")
                    print()

                    while deposit:
                        amt = float(input("Enter amount to deposit : "))
                        if amt <= 0:
                            print()
                            print("Enter correct amount (amount must be > 0)")
                            print()
                            continue
                    
                        else:
                            print("Please verify to continue.")
                            print()
                            while True:
                                p = input("Enter the password:")
                                if p == password:
                                    deposit = False
                               
                                    # Final update of balancee in data file 
                                    time = datetime.datetime.now()
                                    log_transactions(user_id,user_id,amt,time,mode=1)
                                    update_balance(user_id,amt,mode)


                                    print()
                                    print(f"Deposit of $ {amt} Confirmed. ")
                                    print()
                                    print(f"Final Balance : $ {find_balance(user_id,password)}")

                                
                                    break
                                else:
                                    print("Enter correct password.")
                                    continue
                
                elif choice  == 3:
                    print("Payments Selected.")
                    print()
                    print(f"Your current balance is $ {find_balance(user_id,password)}")

                    payment = False
                    while not payment:
                        reciever_uid = input("Enter the recievers account number :").strip()
                        if reciever_uid == user_id:
                            print("Self Transfer is not allowed.")
                            print("Enter a different account number.")
                            continue
                        else:
                             if check_account(reciever_uid):
                                  while True:
                                       amt = float(input("Enter the amount to send:"))
                                       if amt > float(find_balance(user_id,password)):
                                            print(f"Enter amount <= $ {find_balance(user_id,password)}")
                                            continue
                                       else:
                                            pkey = input("Enter password to confirm the transaction:")
                                            if pkey == password:
                                                 print("Transaction Completed.")
                                                 update_balance(user_id,amt,mode = -1)
                                                 update_balance(reciever_uid,amt,mode = 1)
                                                 time = datetime.datetime.now()
                                                 log_transactions(user_id,reciever_uid, amt,time,mode = 1 )
                                                 
                                                 payment = True
                                                 break
                                            else:
                                                 print("Wrong Password.")
                                                 continue
                                            

                             else:
                                  print("Enter coreect receiers account number.")
                                  continue
                             
                         
                                       
                elif choice == 4:
                    print("Checking Balance ...")
                    print()
                    print(f"Your current balance is : $ {find_balance(user_id,password)}")
                    print()
                
                elif choice  == 5:
                     print("Logging Out")
                     break
                
                else:
                     print("Incorrect choice.")
        
        else:
            print("Wrong Credentials.")
            print("Retry the process with correct credentials.")
    



    
    elif ch == 3:
        print("Admin Control Mode")
        print()

        admin_password = input("Enter the password : ").strip()
        if admin_password == passkey:
            print("Accesss Granted.")
            print()
            while True:
                print("     Menu     \n1 : To view Account details\n2 : To delete user account.\n3 : To exit\n4 : To view transaction history.")
                ad_chocie = input("Enter choice:").strip()
                if ad_chocie == "1":
                    print(view_userdata())

                    
                
                elif ad_chocie == "2":
                    print("Delete User Account.")
                    print()
                    user_id = input("Enter user account number:").strip()
                    result = delete_user(user_id)

                    if result:
                         print("Deleted.")
                    else:
                         print("Account does not exist.")
                    
                elif ad_chocie == "3":
                    print("Exiting Admin Control Mode.")
                    break

                elif ad_chocie == "4":
                    print("List of all transactions.")
                    show_transactions()

                    
                    
                else:
                   print("Wrong choice.")
        else:
            print("Enter correct password.")
    
        
    
    elif ch == 4:
        print("For any queries or suggestions, feel free to reach us at:\nEMAIL: abc@gmail.com\nContact: 1234567890")
        print("Your feedback and suggestions will be highly appreciated, as they help us improve our service.")
        print()
        print("Disclaimer: We do not reveal your identity and maintain complete anonymity.")

    
    elif ch == 5:
       print("_____About_____")
       print("""This is a simple Python project that includes a few features of a banking system.

This project was created by Rishav Kumar.

All Rights Reserved © 2026""")
       
    
    elif ch == 6:
        print("ThankYou for using our service.")
        print("Help us improve our service by your valuable feedback.")
        fbck = input("Enter your suggestion or press enter to end:")
        
        if fbck :
            with open("feedback.txt","a") as file:
                file.write(fbck + "\n")
                
            print("Thanks for your feedback.")
            status_main = False
        else:
            print("Exiting")
            status_main  = False
    
    else:
         print("Wrong Choice.")



    