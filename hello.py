
print ("Hello, World!")
print ("Welcome to Python!")
color=(input("Enter Your favorite color:"))
print (f"Your favorite color is {color}!")

number1=float(input("Enter the first number: "))
number2=float(input("Enter the second number: "))

sum=number1+number1
print(sum)

product=number1*number2
print(product)

difference=number1-number2
print(difference)

quotient=number1/number2
print(quotient)

#3

name="Malethabo"
age=25
city="Johannesburg"

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")

a=5
b=10
a=a+b
b=a-b
a=a-b

print(f"a is {a}")
print(f"b is {b}")

#calculater

def calculator():
  numb=int(input("enter a number: "))
  numb1=int(input("enter a number: "))
  operator=(input("enter a operator: "))
  if operator == "+":
   print (numb+numb1)
  elif operator =="-":
   print (numb-numb1)
  elif operator == "*":
   print (numb* numb1)
  elif operator == "/":
   print (numb/numb1)
  else : 
   print ("Invalid operator")
    
calculator()


kilometer=float(input("Enter kilometers :"))
miles=(kilometer/0.621371)
print(f"Miles: {miles}")

num=int(input("Enter a  number: "))
if num%2==0:
 print ("Even Number")
else:
 print ("odd Number")

for x in range(1,11):
 print(x)

for x in range(1,51):
 if x%3==0 and x%5==0:
  print(f"FizzBuzz: {x}")
 elif x%3==0:
  print(f"Fizz: {x}")
 elif x%5==0:
  print(f"Buzz: {x}")

password=(input("Enter a password: "))
for x in password:
  if x == "admin123":
   print(x)
   break
  
   print("Enter the correct Password")

password=(input("Enter a password: "))
i="admin123"
while i==password:
 print(i)
else :
 print("incorrect password")

password=(input("Enter a password: "))
i="admin123"
while i!=password: 
 print("incorrect password")
 password=(input("Enter a password: "))
else :
 print("Correct password")

def add(a,b):
 return a+b
print(add(5,6))

def greet(name):
 return "Hello, "+name
print (greet("Malethabo"))

def is_prime(n):
 if n < 2 :
  return False
 for i in  range(2, int(n **  0.5) + 1):
    if n % i == 0:
      return False

print(is_prime(3))
print(is_prime(10))


def factorial(n):
    if n == 0 or n == 1:
      return 1
    else:
        return n * factorial( n - 1)
print(factorial(5))