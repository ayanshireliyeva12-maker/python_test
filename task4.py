# task 1

data = {
    "name": "Ayan",
    "age": 18,
    "city": "Baku"
}

choice = input("Enter:\n 1 - Keys\n 2 - Values ")

if choice == "":
    print("You did not enter any information.")
elif choice == "1":
    print(data.keys())
elif choice == "2":
    print(data.values())
else:
    print("Invalid choice")

# task 2

#------ basa dusmedim

# task 3

products = {}

for i in range(5):
    name = input("Product: ")
    price = float(input("Price: "))
    products[name] = price

search = input("Enter product: ")

if search in products:
    print(products[search])
else:
    print("Product not found")

# task 4

students = {
    "Ali": 85,
    "Veli": 42,
    "Murad": 91,
    "Aysel": 58,
    "Nigar": 100
}

passed = {}

for name in students:
    if students[name] > 60:
        passed[name] = students[name]

print(passed)

# task 5

students = {
    "Ali": {"age": 20, "city": "Baku", "score": 85},
    "Veli": {"age": 21, "city": "Ganja", "score": 92},
    "Murad": {"age": 19, "city": "Sumgait", "score": 78}
}

best_student = ""
score = 0

for name in students:
    if students[name]["score"] > score:
        score = students[name]["score"]
        best_student = name

print(best_student)
print(students[best_student])

# task 6

user1 = {"Ali", "Murad", "Samir", "Aysel"}
user2 = {"Murad", "Nigar", "Ali", "Leyla"}

print(user1 & user2)

common = user1.intersection(user2)

print(common)

# task 7


users = {
    "admin": "12345",
    "user": "11111",
    "guest": "22222"
}

login = input("Login: ")
password = input("Password: ")

if login in users and users[login] == password:
    print("Welcome")
else:
    print("Login or password is incorrect")