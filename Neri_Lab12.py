foods = ["Chicken Wings", "Carbonara", "Fish", "Garlic Bread"]
food_prices = [4.99, 3.50, 1.99, 1.50]

def display_menu():
    print("Food Menu:")
    for i in range(len(foods)):
        print(f"{i + 1}. {foods[i]} - ${food_prices[i]:.2f}")


display_menu()


choice = int(input("Select the food you want by entering its number: "))

if 1 <= choice <= 4:
    selected_food = foods[choice - 1]
    selected_price = food_prices[choice - 1]
    print(f"You chose {selected_food}, which costs ${selected_price:.2f}.")

    payment = float(input("Enter your payment amount: $"))

    while payment < selected_price:
        payment = float(input("Insufficient amount. Please enter a valid payment: $"))

    print("Payment successful!")
    change = payment - selected_price
    print(f"Your change is ${change:.2f}")
else:
    print("Mali ka hahahaha Pili ka ulet between 1 and 4.")
