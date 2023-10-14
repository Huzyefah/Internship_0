
MIDNIGHT_HOUR = 0
EVENING_START_HOUR = 16
EVENING_DISCOUNT = 0.5  
OTHER_DISCOUNT = 0.1  
MIDNIGHT_PRICE = 0    
DAY_TOTAL = 0

def calculate_check_digit(number):
    total = 0
    for i in range(4):
        total += int(number[i]) * (i + 1)
    return total % 11

def calculate_price(day, arrival_hour, parking_hours, frequent_number):
    if frequent_number:
        check_digit = int(frequent_number[-1])
        frequent_number_without_check = frequent_number[:-1]
        if calculate_check_digit(frequent_number_without_check) != check_digit:
            return "Invalid frequent parking number. No discount applied."

    if arrival_hour < MIDNIGHT_HOUR or arrival_hour >= 8:
        return "No parking allowed between midnight and 08:00."
    if arrival_hour >= EVENING_START_HOUR:
        base_price = 6.00
    else:
        if day == "Sunday":
            base_price = 1.50
        else:
            base_price = 2.00

    if arrival_hour >= EVENING_START_HOUR:
        final_price = base_price * parking_hours * (1 - EVENING_DISCOUNT)
    else:
        final_price = base_price * parking_hours * (1 - OTHER_DISCOUNT)

    return final_price

while True:
    task = input("Enter a task (1 - Calculate Price, 2 - Add Payment, exit - Exit): ").lower()

    if task == '1':
        day = input("Enter the day of the week: ")
        arrival_hour = int(input("Enter the hour of arrival (0-23): "))
        parking_hours = int(input("Enter the number of hours to park: "))
        frequent_number = input("Enter frequent parking number (or leave empty): ")

        price = calculate_price(day, arrival_hour, parking_hours, frequent_number)
        if isinstance(price, str):
            print(price)
        else:
            print(f"Price to park: ${price:.2f}")
    elif task == '2':
        payment = float(input("Enter the amount paid (must be greater than or equal to the amount displayed): "))
        DAY_TOTAL += payment
        print(f"Payment of ${payment:.2f} added to daily total.")
    elif task == 'exit':
        break
    else:
        print("Invalid task. Please select 1, 2, or exit.")

print(f"Daily total: ${DAY_TOTAL:.2f}")
