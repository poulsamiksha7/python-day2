#Q1 Largest of 3 numbers

num1= int(input("Enter your number 1: "))
num2= int(input("Enter your number 2: "))
num3= int(input("Enter your number 3: "))

if (num1>num2) and (num1>num3):
    print("Number 1 is greatest")

elif (num2>num1) and (num2>num3):
     print("Number 2 is greatest")
else:
     print("Number 3 is greatest")

#Q2 Positive, Negative or Zero

num= int(input("Enter your number : "))

if (num>=0):
     print("Number  is positive")
elif (num<=0):
     print("Number  is Negative")
else :
 print("Number is Zero")          

# Q3 Leap year check

year = int(input("Enter your year"))

if year%4 == 0 :
    print("Year is leap year")
else:
    print("Year is not leap year")    

#Q4 Vowel or Consonant
ch = ['a','e','i','o','u']
alp= input("Enter a single charachter").lower()
if len(alp) == 1 and alp.isalpha():
    if alp in ch :
        print("The alphabet is Vowel")
    else:
        print("The alphabet is Consonant")
else:
    print("Invalid Input. Please enter single character alphabet")

#Q5 Electricity Bill Calculator
#Unit 0-100 Rate 10rs (100)
#Unit 101-200 Rate 20rs (100)
#Unit 201-300 Rate 30rs (100)
#Unit 301-400 Rate 40rs (100)
#Unit 401-500 Rate 50rs (100)

units= int(input("Enter Your Units"))
bill=0
if units<=100:
    bill=units*10
elif units<=200:
    bill=(100*10) + ((units-100)*20)
elif units<=300:
    bill=(100*10)+(100*20)+((units-200)*30)
elif units<=400:
    bill=(100*10)+(100*20)+(100*30)+((units-300)*40)
elif units<=500:
    bill=(100*10)+(100*20)+(100*30)+(100*40)+((units-400)*50)
else:
    print("Invalid Input (more than 500 units)")
    bill=None
if bill is not None:
    print(f"Your electricity bill is {bill}")

# Q6 Pass/Fail based on Marks

marks = int(input("Enter your Marks : "))
if (marks<=100 and marks>=91):
    print("Pass.Grade O")
elif (marks<=90 and marks>=81):
    print("Pass.Grade A+")
elif (marks<=80 and marks>=71):
    print("Pass.Grade A")
elif (marks<=70 and marks>=61):
    print("Pass.Grade B+")
elif (marks<=60 and marks>=51):
    print("Pass.Grade B")
elif (marks<=50 and marks>=30):
    print("Pass.Grade C")
else:
    print("Fail .Better Luck Next Time")

#Q7 Grade Calculator

marks = int(input("Enter your Marks : "))
if (marks<=100 and marks>=91):
    print("Pass.Grade O")
elif (marks<=90 and marks>=81):
    print("Pass.Grade A+")
elif (marks<=80 and marks>=71):
    print("Pass.Grade A")
elif (marks<=70 and marks>=61):
    print("Pass.Grade B+")
elif (marks<=60 and marks>=51):
    print("Pass.Grade B")
elif (marks<=50 and marks>=30):
    print("Pass.Grade C")
else:
    print("Fail .Better Luck Next Time")

#  Q8 Check divisibilty by 5 and 11

num=int(input("Enter your Number"))

if num%5==0 and num%11==0:
    print("The number is divisible by 5 and 11")
elif num%11==0:
    print("The number is divisible by 11")
elif num%5==0:
    print("The Number is divisible by 5")
else:
    print("Invalid input")

#Q9 Simple ATM Logic

balance=50000 

while True:
    print("\n====ATM Menu====")
    print("1. Check Balance")
    print("2. Money Withdrawn")
    print("3. Cash Deposit")
    print("4. Exit")

    choice=input("Enter your Input(1/2/3/4): ")

    if choice=='1':
        print(f"Your Current Balance is. {balance}")
    elif choice=='2':
        amt=float(input("Enter the amount: "))
        if 0<amt<=balance:
           balance-=amt
           print(f"Balance is withdrawn{balance}")
           print(f"Current balance is {balance}")
        else:
            print("Invalid Input. Please enter the amount correctly")
    elif choice=='3':
        amt=float(input("Enter the amount"))    
        if amt>0:
            balance+=amt
            print(f"Balace is deposited{amt}")
            print(f"Current balance is {balance}")
        else:
            print("Invalid Input.Please Enter amount correctly")  
    elif choice=='4':
        print("Thank You for using ATM")

        break

    else:
      print("Invalid choice! Please select 1,2,3 or 4")         

#Q 10 Number is even and multiple of 4

num=int(input("Enter your Number"))

if num%2==0 and num*4:
    print("Number is multiple of 4 and even")
elif num%2==0:
    print("Number is even only")
elif num*4:
    print("Number is multiplied by 4")
else:
    print("Invalid Input")

    


    

    


