import os, os.path
import time
import subprocess
balance = 0
def clear():
    
    time.sleep(3)
    
    CLEAR = subprocess.run(['clear'])


#check if file exists
def check_if_file_exists():
    check_file = os.path.exists("udata.txt")
    
    if check_file == True:
        pass
    else:
        
        print("looks like its your first time with om ahmed`s bank let us settle everything for you")
        
        time.sleep(5)
        
        file = open("udata.txt", "w")#if file does not exist create a new file
        print("done with files now you can continue with om ahmed`s bank")

#empty file checker
def check_if_file_empty():
    
    file = os.stat("udata.txt").st_size
    
    return file

#view user balance
def get_balnce():
    
    check_if_file_exists()
    
    if check_if_file_empty() == 0:
        return 0
    
    else:
        
        with open("udata.txt", "r") as file:
            
            balance = file.readline()
        return balance

#add to user balance
def add_balance():
    
    check_if_file_exists()
    
    while True:
        new_balance = (input("enter new balance: "))
        
        try:
            balance = get_balnce()
            total_balance = int(int(balance) + int(new_balance))
            
            with open("udata.txt", "w") as file:
                
                file.write(f"{total_balance}")
                
                print(f"done.\n total balance= {total_balance}")
                
                break
        except ValueError:
            print("invalid input please enter a number")

#withdrawl function
def withdraw_balance():
    check_if_file_exists()
    
    while True:
        
        amount = input("enter amount you want to withdraw: ")
        
        if amount.isdigit() == True:
        
            amount = int(amount)
        
            currunt_balance = get_balnce()
        
            currunt_balance = int(currunt_balance)
        
            new_balance = int (currunt_balance - amount)
        
            if new_balance < 0:
                print("sorry you dont have enough money to withdraw")
                break
            else:
            
                with open("udata.txt", "w") as file:
            
                    file.write(str(new_balance))
            
                print("withdrawl succeeded")
                break
def main():
    while True:
        choice = input("""what do you want to do
1->add
2->withdrawl
3->view
q->quit
$ """)
        if choice == "1":
            
            clear()
            
            add_balance()            
        elif choice == "2":
            
            clear()
            
            withdraw_balance()
        elif choice == "3":
            
            clear()
            
            print("balance=",get_balnce())
        elif choice == "q":
            
            break
        else:
            print("invalid choice please enter valid option: ")

main()