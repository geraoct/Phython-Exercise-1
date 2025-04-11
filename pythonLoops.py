
#1. Print numbers from 1 to 20 using a for loop. 
for nums in range(1,21):
 print(nums,end=" ")

print()
#2. Print the square of numbers from 1 to 10. 
for nums in range(1,11):
 print(nums**2,end=" ")

print()
#3. Print all even numbers between 1 and 50. 
for evenNums in range(1,51):
 if evenNums %2==0:
  print(evenNums,end=" ")

print()
#4. Print the first 10 multiples of 5. 
for multipleOf in range(5,51,5):
 print(multipleOf,end=" ")

print()
#5. Write a program to count how many vowels are in a given string.
word=input("Please enter a word: ")
count=0
for letter in word.lower():
    if letter== 'a' or \
        letter== 'e' or \
        letter== 'i' or \
        letter== 'o' or \
        letter== 'u' :
      count+=1
      
print(count,end=" ")

print()

#6. Write a program that takes a list of numbers and prints the sum of all numbers
sum = 0
for numbers in range (1,11):
 sum+=numbers
print(sum,end=" ")

print()

#7. Given a list of names, print only the names that start with the letter 'A'. 
names=["Alice","Reneilwe","Amogelang","Andile","Lethabo","Hlengiwe","amanda"]
for name in names:
  if name.startswith('A') or name.startswith('a') :
    print(name,end=" ")


print()

#while Loop
#1. Print numbers from 10 to 1 using a while loop.

num=10
while (num>=1):
  print(num,end=" ")
  num-=1

print()

#2. Keep asking the user to enter a number until they enter 0, then print the sum of all numbers entered. 
sum=0
numbers= int(input("Enter a number: "))
while (numbers!=0):
  
  sum+=numbers
  numbers=int(input("Enter a number: "))
else :
  
  print(sum)

#3. Print the Fibonacci sequence up to 10 terms. 
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci(10)

#4. Write a program that keeps asking the user for a password until they enter 'Python123'. 
password="Python123"
i=input("enter Password:")
while i !=password:
  i=input("wrong password ,enter Password again:")
  print(i)
else:
  print("the password is correct",end=" ")

print()

#5. Write a guessing game where the user must guess a randomly generated number between 1 and 50. Give hints if their guess is too high or too low. 
# import random

# number_to_guess = random.randint(1, 50)
# print("Guess the number between 1 and 50!")

# while True:
#     user_guess = int(input("Enter your guess: "))
    
#     if user_guess < number_to_guess:
#         print("Too low! Try again.")
#     elif user_guess > number_to_guess:
#         print("Too high! Try again.")
#     else:
#         print("Congratulations! You've guessed the number!")
#         break


#nested for loop

#1. Print the following pattern using nested loops:

for i in range(1, 6):
    # Print '*' for each column in the row
    print('*' * i)

#2. Print a multiplication table from 1 to 5. 

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print()

#3. Print a rectangle of '*' where the user enters the width and height. 
width = int(input("Enter the width of the rectangle: "))
height = int(input("Enter the height of the rectangle: "))
for i in range(height):
    print('*' * width)

#4. Create a program that generates a right-angled triangle of numbers: 
for i in range(1, 6):
  for n in range(1,i):
     print(n,end=" ") 

  print()
height = int(input("Enter the height of the triangle: "))

for i in range(1, height + 1):
    print(" ".join(str(x) for x in range(1, i + 1)))

#5. Write a program that prints a chessboard pattern using 'X' and 'O': 
def print_chessboard(rows=8, cols=8):
    for row in range(rows):
        line = ''
        for col in range(cols):
            if (row + col) % 2 == 0:
                line += 'X'
            else:
                line += 'O'
        print(line)

print_chessboard()


for primeNums in range(2,100):
 if primeNums %2 !=0 and primeNums%3!=0 and primeNums%5!=0 and primeNums%7!=0:
    print(primeNums)
 else:
    pass
 