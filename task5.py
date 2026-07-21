# task 1

count = int(input("How many numbers will you enter? "))

total = 0

for i in range(count):
    num = int(input("Enter a positive number: "))

    while num < 0:
        print("Negative numbers are not allowed.")
        num = int(input("Enter a positive number: "))

    total += num

print("Sum:", total)

# task 2

balance = 0
history = []

while True:
    print("\n1. Check Balance")
    print("2. Add Money")
    print("3. Withdraw Money")
    print("4. History")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amount = float(input("Enter amount: "))
        balance += amount
        history.append("Added: " + str(amount))

    elif choice == "3":
        amount = float(input("Enter amount: "))

        while amount > balance:
            print("Not enough balance.")
            amount = float(input("Enter a smaller amount: "))

        balance -= amount
        history.append("Withdrawn: " + str(amount))

    elif choice == "4":
        print("History:")
        for item in history:
            print(item)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")


# task 3

students = int(input("How many students? "))

for i in range(students):
    name = input("Student name: ")

    grades = []

    for j in range(3):
        grade = int(input(f"Grade {j + 1}: "))

        while grade < 0 or grade > 100:
            print("Grade must be between 0 and 100.")
            grade = int(input(f"Grade {j + 1}: "))

        grades.append(grade)

    average = sum(grades) / 3

    if average >= 60:
        result = "Passed"
    else:
        result = "Failed"

    print("\nName:", name)
    print("Average:", average)
    print("Result:", result)



# task 4


numbers = []

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("Sum:", sum(numbers))


# task 5

for i in range(6):
    word = input("Enter a word: ")
    print(word, "->", len(word))


# task 6

words = []

for i in range(5):
    word = input("Enter a word: ")
    words.append(word)

start_a = 0
end_a = 0
long_words = 0

for word in words:
    if word.startswith("a"):
        start_a += 1

    if word.endswith("a"):
        end_a += 1

    if len(word) > 5:
        long_words += 1

print("Starts with 'a':", start_a)
print("Ends with 'a':", end_a)
print("Length greater than 5:", long_words)



# task 7

words = []
upper_words = []

for i in range(5):
    word = input("Enter a word: ")
    words.append(word)

for word in words:
    upper_words.append(word.upper())

print("Uppercase words:")
print(upper_words)

