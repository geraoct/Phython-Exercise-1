
x=int(input("Enter First Number: "))
y=int(input("Enter Second Number: "))
z=int(input("Enter Third Number: "))
print(max(x,y,z))


p=float(input("Enter principal amount: "))
r=float(input("Enter the rate of interest: "))
t=float(input("Enter time in months: "))
a=p * (1+(r/100*t))
print(a)


Amount=int(input("Enter the amount:R"))
year1=4
total=Amount*(1+(5/100*year1))
print(total)
if total>10000:
 print("The loan repayment is high")
else:
 print("The loan repayment is manageable")

savings=15000
interest=7/100
years=3
finalAmnt=savings*(1+(interest*years))
interest1=finalAmnt-savings

if interest1>savings*(20/100):
  print("Great Investment")
else:
  print("Consider a longer Investment")

savingss=12500
interests=6/100
yearss=6
finalAmnts=savingss*(1+(interests*yearss))
print(finalAmnts)
if finalAmnts>15000:
  print("Significant funding secured")
else:
  print("The grant amount is moderate")

investment=float(input("Enter Investment amount:R"))
interest=float(input("Enter the rate of interest: "))
time=float(input("Enter time in years: "))
n=float(input("Enter number of times compounded yearly: "))

def totalAmount(investment,interest,time,n, compareAmount):
    totalAmnt=investment*(1+(interest/n))**time
    print(totalAmnt)
    if totalAmnt>compareAmount:
        print("Fantastic growth!")
    else:
        print("Investment growing")

totalAmount(investment,interest,time,n, 15000)

def finalAmount():
    savings=20000
    interest=0.25
    n=2
    time=3
    finalAmt=savings*(1+(interest/n))**time
    if finalAmt>savings*(25/100):
     print("Profitable savings!")
    else:
       print("Consider investing for a longer period")

finalAmount()

def amountTotal():
    savings=50000
    interest=0.5
    n=4
    time=6
    totalAmount=savings*(1+(interest/n))**time
    print(totalAmount)
    if totalAmount>70000:
        print("Huge profit!")
    else:
        print("Steady investment groth")
amountTotal()

def amountTotal():
    savings=10000
    interest=0.8
    n=1
    time=5
    totalAmount=savings*(1+(interest/n))**time
    if totalAmount>15000:
        print("Fantastic growing")
    else:
        print("Investment is growing")
amountTotal()


def totalInterest():
   p=25000
   initialRate=0.9
   initialTime=2
   rate=0.12
   time=3
   amountTotal=(p*initialRate*initialTime)/100
   amountTotal2=(p*rate*time)/100
   sumTotal=amountTotal+amountTotal2
   totalInter=(amountTotal-p)+(amountTotal2-p)
   print(amountTotal)
   print(amountTotal2)
   print(sumTotal)
   print(totalInter)

totalInterest()

def finalAmount():
   p=30000
   initialRate=0.8
   initialTime=2
   n1=4
   n2=4
   rate=0.10
   time=3
   amountTotal=p*(1+(initialRate/n1))**initialTime
   amountTotal2=amountTotal*(1+(rate/n2))**time
   sumTotal=amountTotal+amountTotal2
   totalInter=(amountTotal-p)+(amountTotal2-p)
   print(amountTotal)
   print(amountTotal2)
   print(sumTotal)
   print(totalInter)

finalAmount()

