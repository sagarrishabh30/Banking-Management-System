import pickle
import os
import pathlib
class Account :
    accNo = 0
    name = ''
    deposit=0
    type = ''
    
    def MakeNewAccount(my):
        my.accNo= int(input("Enter A/C No. =  "))
        my.name = input("Enter Name of Account Holder =  ")
        my.type = input("Type of Account (Current/Savings) =  ")
        my.deposit = int(input("Enter initial amount(>=500 for Saving and >=1000 for current"))
        print("\n\n\nCongratulations, Your Account is created!!")
    
    def showAccount(my):
        print("Account Number = ",my.accNo)
        print("Name of Account Holder  = ", my.name)
        print("Type of Account",my.type)
        print("Balance in Account = ",my.deposit)
    
    def modifyAccount(my):
        print("Account Number = ",my.accNo)
        my.name = input("Change Name of Account Holder =")
        my.type = input("Change Type of Account =")
        my.deposit = int(input("Change Balance ="))
        
    def depositAmount(my,amount):
        my.deposit += amount
    
    def withdrawAmount(my,amount):
        my.deposit -= amount
    
    def report(my):
        print(my.accNo, " ",my.name ," ",my.type," ", my.deposit)
    
    def getAccountNo(my):
        return my.accNo
    def getAcccountHolderName(my):
        return my.name
    def getAccountType(my):
        return my.type
    def getDeposit(my):
        return my.deposit
    

def intro():
    print("\t\t\t\t-----------------------")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t-----------------------")

    print("\t\t\t\tMade By:-")
    print("\t\t\t\tRishabh Sagar")
    



def writeAccount():
    account = Account()
    account.MakeNewAccount()
    writeAccountsFile(account)

def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            print(item.accNo," ", item.name, " ",item.type, " ",item.deposit )
        infile.close()
    else :
        print("Can't find any data to show")
        

def displaySp(num): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num :
                print("Balance in your Account is = ",item.deposit)
                found = True
    else :
        print("No data to Search")
    if not found :
        print("No existing data with this number")

def depositAndWithdraw(num1,num2): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.accNo == num1 :
                if num2 == 1 :
                    amount = int(input("Deposit Amount = "))
                    item.deposit += amount
                    print("Your account is updated")
                elif num2 == 2 :
                    amount = int(input("Withdrawl Amount = "))
                    if amount <= item.deposit :
                        item.deposit -=amount
                    else :
                        print("You cannot withdraw larger amount")
                
    else :
        print("No data to Search")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

    
def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.accNo != num :
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
     
def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.accNo == num :
                item.name = input("Name of Account Holder = ")
                item.type = input("Type of Account = ")
                item.deposit = int(input("Enter the Amount = "))
        
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
   

def writeAccountsFile(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    
        
# start of the program
ch=''
num=0
intro()

while ch != 8:
    #system("cls");
    print("\tWHAT DO YOU WANT TO DO")
    print("\t1. OPEN A NEW ACCOUNT")
    print("\t2. DEPOSIT MONEY IN YOUR ACCOUNT")
    print("\t3. WITHDRAW AMOUNT FROM YOUR ACCOUNT")
    print("\t4. ENQUIRY FOR BALANCE ")
    print("\t5. ALL ACCOUNT HOLDER LIST")
    print("\t6. CLOSE AN ACCOUNT")
    print("\t7. MODIFY AN ACCOUNT")
    print("\t8. EXIT")
    print("\tSelect Your Choice (1-8) ")
    ch = input()
    #system("cls");
    
    if ch == '1':
        writeAccount()
    elif ch =='2':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        num = int(input("\tEnter The account No. : "))
        displaySp(num)
    elif ch == '5':
        displayAll();
    elif ch == '6':
        num =int(input("\tEnter The account No. : "))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("\tEnter The account No. : "))
        modifyAccount(num)
    elif ch == '8':
        print("\tThanks for using bank managemnt system")
        break
    else :
        print("Invalid choice")
    
    ch = input("Enter your choice : ")
    


    
    
    
    
    
    
    
    
    
    
