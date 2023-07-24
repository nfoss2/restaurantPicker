"""
Authors: Natalie
Purpose: Natalie And Austin's very cute and awesome restaurant picker
"""

import json
from datetime import datetime

def load_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def get_current_day():
    days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    return days_of_week[datetime.now().weekday()]

def recommend_item(data, category):
    current_day = get_current_day()

    if category not in data:
        print("Invalid category input. Please choose from 'restaurants', 'coffee_shops', 'attractions', or 'other'.")
        return

    open_items = [item for item in data[category] if current_day in item['open_hours']]
    
    if not open_items:
        print("No open items found in the selected category on the current day.")
        return

    print(f"Recommendation for {category}:")
    recommendation = open_items[0]
    print("Name:", recommendation['name'])
    print("Address:", recommendation['address'])
    print("Phone:", recommendation['phone'])
    if 'cuisine' in recommendation:
        print("Cuisine:", recommendation['cuisine'])
    if 'specialty' in recommendation:
        print("Specialty:", recommendation['specialty'])
    if 'type' in recommendation:
        print("Type:", recommendation['type'])
    print("Rating:", recommendation['rating'])
    print("Opening Hours on", current_day.capitalize() + ":", recommendation['open_hours'][current_day])

if __name__ == "__main__":
    filename = "database.json"
    data = load_data(filename)

    print("Categories available: 'restaurant', 'coffee shop', 'attraction', 'other'")
    category = input("Please enter a category: ").lower()

    recommend_item(data, category)
