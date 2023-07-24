import json
from datetime import datetime

def load_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

def add_new_item(data):
    categories = ['restaurants', 'coffee_shops', 'attractions', 'other']
    print("Categories available: 'restaurants', 'coffee_shops', 'attractions', 'other'")
    category = input("Please enter the category of the new item: ").lower()

    if category not in categories:
        print("Invalid category input. Please choose from the available categories.")
        return

    new_item = {
        "name": input("Enter the name of the new item: "),
        "address": input("Enter the address of the new item: "),
        "phone": input("Enter the phone number of the new item: "),
        "rating": float(input("Enter the rating of the new item (0.0 to 5.0): ")),
    }

    if category == 'restaurants':
        new_item["cuisine"] = input("Enter the cuisine type of the restaurant: ")
    elif category == 'coffee_shops':
        new_item["specialty"] = input("Enter the specialty of the coffee shop: ")
    elif category == 'attractions':
        new_item["type"] = input("Enter the type of attraction: ")
    elif category == 'other':
        new_item["type"] = input("Enter the type of other point of interest: ")

    open_hours = {}
    days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    for day in days_of_week:
        opening_hours = input(f"Enter the opening hours for {day.capitalize()} (e.g., 09:00 AM - 05:00 PM): ")
        open_hours[day] = opening_hours

    new_item["open_hours"] = open_hours

    data[category].append(new_item)
    print("New item added successfully!")

if __name__ == "__main__":
    filename = "database.json"
    data = load_data(filename)

    add_new_item(data)

    save_data(filename, data)