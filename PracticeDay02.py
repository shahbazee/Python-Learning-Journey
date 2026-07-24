
def fruit_basket():
    fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
    print(fruits)
    print(fruits[0])
    print(fruits[-1])
    print(f"Total fruits: {len(fruits)}")

def shopping_cart():
    cart = []
    cart.append("Milk")
    cart.append("Bread")
    cart.append("Eggs")
    cart.append("Butter")
    print("After adding: ", cart)

    cart.remove("Bread")
    print("After removing bread: ", cart)

    cart.insert(0, "Cheese")
    print("Final Cart: ", cart)

def phone_book_lookup():
    phone_book = {
        "Alice": "555-0101",
        "Bob": "555-0202",
        "Charlie": "555-0303"
    }
    print("Bob's number:", phone_book["Bob"])

    if "David" in phone_book:
        print("David: Found")
    else:
        print("David: Not Found")

    print("Eve:", phone_book.get("Eve", "No number for Eve"))
    print("Names:", list(phone_book.keys()))
    print("Numbers:", list(phone_book.values()))

phone_book_lookup()