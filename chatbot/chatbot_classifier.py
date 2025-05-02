import re

MEATY_KEYWORDS = [
    "fish", "tuna", "salmon", "shrimp", "chicken", "beef",
    "pork", "steak", "meat", "lamb", "turkey", "bacon", "ham", "crab", "lobster"
]

ANIMAL_PRODUCT_KEYWORDS = [
    "cheese", "milk", "butter", "cream", "yogurt", "egg"
]

PLANT_MILK_KEYWORDS = [
    "almond milk", "soy milk", "oat milk", "coconut milk", "cashew milk", "rice milk"
]

def classify_food(text):
    dishes = re.split(r'\d+\.', text)[1:]
    results = []

    for dish in dishes:
        dish_lower = dish.lower()

        if any(meat_word in dish_lower for meat_word in MEATY_KEYWORDS):
            results.append("non-vegetarian")
        elif any(dairy_word in dish_lower for dairy_word in ANIMAL_PRODUCT_KEYWORDS):
            if any(plant_milk in dish_lower for plant_milk in PLANT_MILK_KEYWORDS):
                results.append("vegan")
            else:
                results.append("vegetarian")
        else:
            results.append("vegan")

    if "non-vegetarian" in results:
        return "non-vegetarian", results
    elif "vegan" in results:
        return "vegan", results
    else:
        return "vegetarian", results
