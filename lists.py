# Program 1: Create a list of integers and compute their sum
def sum_of_integers():
    numbers = []
    while True:
        user_input = input("Enter an integer (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            numbers.append(int(user_input))
        except ValueError:
            print("Please enter a valid integer.")
    
    total = sum(numbers)
    print(f"The list of integers: {numbers}")
    print(f"Sum of all integers: {total}")

# Program 2: Create a tuple of favorite books and print each
def print_favorite_books():
    favorite_books = (
        "To Kill a Mockingbird",
        "1984",
        "Pride and Prejudice",
        "The Great Gatsby",
        "The Hobbit"
    )
    print("\nMy favorite books:")
    for book in favorite_books:
        print(book)

# Program 3: Store person information in a dictionary
def person_info():
    person = {}
    person['name'] = input("\nEnter your name: ")
    person['age'] = input("Enter your age: ")
    person['favorite_color'] = input("Enter your favorite color: ")
    print("\nPerson information:")
    print(person)

# Program 4: Create two sets and find common elements
def common_elements():
    set1 = set()
    set2 = set()
    
    print("\nEnter integers for the first set (enter 'done' to finish):")
    while True:
        user_input = input("Enter an integer: ")
        if user_input.lower() == 'done':
            break
        try:
            set1.add(int(user_input))
        except ValueError:
            print("Please enter a valid integer.")
    
    print("Enter integers for the second set (enter 'done' to finish):")
    while True:
        user_input = input("Enter an integer: ")
        if user_input.lower() == 'done':
            break
        try:
            set2.add(int(user_input))
        except ValueError:
            print("Please enter a valid integer.")
    
    common = set1.intersection(set2)
    print(f"\nFirst set: {set1}")
    print(f"Second set: {set2}")
    print(f"Common elements: {common}")

# Program 5: Filter words with odd number of characters
def odd_length_words():
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
    odd_length = [word for word in words if len(word) % 2 != 0]
    print("\nOriginal list of words:", words)
    print("Words with odd number of characters:", odd_length)

# Run all programs
if __name__ == "__main__":
    sum_of_integers()
    print_favorite_books()
    person_info()
    common_elements()
    odd_length_words()