
# task 1
age = int(input("Enter your age :"))

if age > 18:
    print("Access granted")
else:
    print("Access denied")

# task 2

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

if num_1 > num_2:
    print("The larger number is:", num_1)
else:
    print("The larger number is:", num_2)

# task 3

score = int(input("Enter your score:"))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# task 4


number = int(input("Enter number: "))

if number > 0:
    print("The number is positive.")                            
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# task 5

month = int(input("Enter the month number(1-12): "))

if month in [12,1,2]:
    print("Winter")
elif month in [3,4,5]:
    print("Spring")
elif month in [6,7,8]:
    print("Summer")
elif month in [9,10,11]:
    print("Autumn")
else:
    print("Invalid month number.")

# task 6

username = input("Username: ")
password = input("Password: ")

if username == "Ayan" and password == "2468":
    print("Login successful")
else:
    print("Incorrect username or password")

# task 7

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# task 8

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a >= b and a >= c:
    print("The largest number is:", a)
elif b >= a and b >= c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)

# task 9

username = input("Username: ")
password = input("Password: ")

if username == "" and password == "":
    print("You did not enter a username or password.")
elif username == "":
    print("You did not enter a username.")
elif password == "":
    print("You did not enter a password.")
elif username != "Ayan" and password != "2468":
    print("Both username and password are incorrect.")
elif username != "Ayan":
    print("Incorrect username.")
elif password != "2468":
    print("Incorrect password.")
else:
    print("Welcome, Ayan!")


# task 10

name = input("Enter a name: ")

if name == "":
    print("You did not enter a name.")
elif name == "Aslan":
    print("Aslan is my uncle's son.")
elif name == "Imran":
    print("Imran is my maternal uncle's son.")
elif name == "Afaq":
    print("Afaq is my aunt's daughter.")
elif name == "Uzeyir":
    print("Uzeyir is my maternal aunt's son.")
elif name == "Shahin":
    print("Shahin is my close friend.")
else:
    print("Who is that? I don't know this person.") # burda bilmedim adi nece yazim

# task 11

height = float(input("Enter your height (m): "))
weight = float(input("Enter your weight (kg): "))

bmi = weight / (height * height)

print("BMI:", round(bmi, 2))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")