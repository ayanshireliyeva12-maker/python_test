# task 1

def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero!"
    else:
        return "Wrong operation!"
    
# task 2

def calculate_salary(hourly_pay, hours):
    if hours > 50:
        extra_hours = hours - 50
        salary = (40 * hourly_pay) + (extra_hours * hourly_pay * 1.5)
    else:
        salary = hours * hourly_pay
    return salary

# task 3

def check_password(password):
    has_upper = False
    has_lower = False
    has_digit = False

    for character in password:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True

    if len(password) >= 8 and has_upper and has_lower and has_digit:
        return "Strong Password"
    else:
        return "Weak Password"
    
# task 4

def sale(price, customer_type):
    if customer_type == "Gold":
        discount = 0.20
    elif customer_type == "Silver":
        discount = 0.10
    elif customer_type == "Bronze":
        discount = 0.05
    else:
        discount = 0

    final_price = price - (price * discount)
    return final_price

# task 5

def cinema_ticket(age, student):
    if age < 12:
        price = 6
    elif age >= 65:
        price = 8
    else:
        price = 12

    if student:
        price = price * 0.9   

    return price   
